# Relevant ArangoDB documentation

* Transactions: https://www.arangodb.com/docs/stable/transactions.html
* Write conflicts: https://github.com/arangodb/arangodb/issues/9430
* Transaction failures: https://github.com/arangodb/arangodb/issues/11424
* Sorting graph traversal results: https://github.com/arangodb/arangodb/issues/11260

# Data links

## Deleted objects / workspaces

* Currently links to deleted objects can be returned from `get_links_from_sample`.
  * Should this be changed? It means an extra workspace call.
  * It also has reproducibility issues - calls to the method with the same `effective_time` may
    not produce the same results.
    * That being said, changing permissions to workspaces can also change what links are returned
      over time.
  * If we don't return links to deleted objects, should the links be autoexpired if they aren't
    already?
    * This assumes `get_object_info3` with `ignoreErrors: 1` will only return `null` for deleted
      objects when called via `administer` - verify
  * What about expired links to deleted objects with an `effective_time` in the past? Return them?

* Links to deleted objects can be expired as long as the user has write access to the workspace.
  However, links to objects in deleted workspaces **cannot** be expired by anyone, including
  admins, given the current implementation.
  * This naively seems ok since the links aren't accessible by anyone other than admins.

## Creating / updating links

### 10k link limit

* The Sample Service allows no more than 10k non-expired links from any one version of a sample or
  from any one version of an object. That means that a single object version can have no more
  than 10k data IDs (e.g. column names for matrix data).
* This requirement was originally agreed upon because there appears to be no way to
  [efficiently sort and page results with graph queries in ArangoDB](https://github.com/arangodb/arangodb/issues/11260).
  Allowing the collection to grow without limit means that eventually sorted graph queries will
  OOM / hog CPU on the database (or be consistently killed if the DB has that capability). 10K
  is small enough that the results can be sorted in a small amount of memory in the DB,
  application, or UI.
* Link lookups are currently implemented without graph traverals and so in theory the
  10K limit could be lifted.
    * Would need sort / paging / indexes. As usual, paging needs to be based on some aspect of
      the link that is unique, which is tricky here
* HOWEVER - if any of the query parameters or expectations change the limit may have to be
  reinstated, e.g.
  * Changes to how the search regards ACLs.
  * Searching on additional properties, e.g.
    * Workspace object properties
    * Sample properties

### Implementation notes

* Since multiple clients may be creating, updating, or expiring links on the same sample
  or data object simultaneously, the code needs to account for possible race conditions on
  those operations.
* Links are immutable once created, *except* that they can be expired.
* The unique ID of a link in the database is a fn of the data unit ID (e.g.
  workspace UPA + data id) for an unexpired link, and the DUID + created time for expired links.
  This ensures there's only one non-expired link per DUID in the DB.

### Implementation

* Parameters: `new_link`, `update` boolean indicating `current_link` should be replaced if it
  exists
* Start a transaction with a collection exclusive lock.
  * This is required since we're counting multiple documents. Allowing other writes while the
    transaction is in progress will make those counts inaccurate.
* Fetch the `current_link` for the data unit ID, if any
* If `current_link`:
  * If not `update`: fail
  * If `current_link` == `new_link`: abort transaction and return (no-op)
  * If `new_link` is to a different sample and count_links(`new_link.Sample`) > 10K: fail
    * Link look up is based on the data, so we know it's to the same UPA, and since we're
      expiring and replacing a link the link count for the UPA doesn't change.
  * Expire and save `current_link`
    * Creates a new ArangoDB document with a new `_key`
* Else:
  * If count_links(`new_link.UPA`) > 10K: fail
  * If count_links(`new_link.Sample`) > 10K: fail
* Save `new_link`
* Complete the transaction.

### Extant failure modes

* ArangoDB transactions can fail on one node and succeed on another. This will commit the
  changes that succeeded but cause the transaction as a whole to fail client-side. This means
  in theory the client could determine the current state of the DB and try to repair any
  inconsistencies, but in practice this is very complicated.
  * A link could be expired without the current link being updated, effectively leaving an
    expired and current version of the same link. If this link were to be expired again an
    error would occur and the DB would have to be manually corrected.
  * A link could be updated without the prior link being expired, effectively causing the record
    of the prior link to disappear.

## Expiring links

### Implementation notes

* See the implementation notes for creating / updating links above.
* Arango does not support atomically changing a document's `_key`. Since expiring a link
  means changing the `_key`, we use a transaction to reduce the possibility of inconsistent
  database state.
  * But does a transaction really help?

### Implementation

* Parameters: `duid` - the data unit ID
* Fetch `current_link` from the DB via the `duid`.
* If not `current_link`: fail
* Start a transaction.
* Expire `current_link` and save.
  * Creates a new ArangoDB document with a new `_key`
  * Fail if a duplicate key error occurs, meaning the link was expired after fetching the document.
* Delete the old `current_link` document.
* Complete the transaction.

### Extant failure modes

* ArangoDB transactions can fail on one node and succeed on another. This will commit the
  changes that succeeded but cause the transaction as a whole to fail client-side. This means
  in theory the client could determine the current state of the DB and try to repair any
  inconsistencies, but in practice this is very complicated.
  * A link could be expired without the current link being deleted, effectively leaving an
    expired and current version of the same link. If this link were to be expired again an
    error would occur and the DB would have to be manually corrected.
  * A link could be deleted without the expired document being written, destroying the link's
    history.
* Since expiration does not use an exclusive lock, it is possible for other writes to collide
  with the expired link document and cause the write to fail.
  * It is not clear if this will
    [cause the transaction as a whole to fail](https://github.com/arangodb/arangodb/issues/11424).
* If the delete fails, an error will be raised and the transaction will be aborted.
  * Funnily enough, there is an `ignore_missing` parameter, but from the `python-arango`
    documentation:
    ```
    :param ignore_missing: Do not raise an exception on missing document.
    This parameter has no effect in transactions where an exception is  
    always raised on failures.
    ```
  * This could be caused by:
    * Another thread expiring and deleting the link, in which case no further action is necessary.
    * Another thread expiring and updating the link, in which case the current operation should
      not expire the new link.
  * This error takes split second timing and is highly unlikely to occur, and should not
    leave the database in an inconsistent state.
