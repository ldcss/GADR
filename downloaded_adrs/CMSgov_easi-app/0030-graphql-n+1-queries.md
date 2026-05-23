# Do not use Dataloader for dealing with n+1 query issues with GraphQL Resolvers

**User Story:** *(none)*

There's a potential problem with how our GraphQL resolvers are written that could impact scalability as our database gets larger and as we fetch more data and more complex structures from CEDAR. With some nested objects, our GraphQL resolvers can make n+1 queries to the database (or other underlying data source, i.e. CEDAR) to respond to a request. As an example, this GraphQL query:

```graphQL
query {
  accessibilityRequests(first:0) {
    edges {
      node {
        id
        name
        statusRecord {
          status
          euaUserId
        }
      }
    }
  }
}
```

ends up making a SQL request for all accessibility requests, then it makes a *separate* SQL request for *each* accessibility request status record:

```
2021-12-20 23:36:02.281 UTC [118] LOG:  statement: SELECT * FROM accessibility_requests WHERE deleted_at IS NULL

2021-12-20 23:36:02.283 UTC [118] LOG:  execute <unnamed>: SELECT * FROM accessibility_request_status_records WHERE request_id=$1 ORDER BY created_at DESC LIMIT 1;
2021-12-20 23:36:02.283 UTC [118] DETAIL:  parameters: $1 = '6e224030-09d5-46f7-ad04-4bb851b36eab'

2021-12-20 23:36:02.285 UTC [120] LOG:  execute <unnamed>: SELECT * FROM accessibility_request_status_records WHERE request_id=$1 ORDER BY created_at DESC LIMIT 1;
2021-12-20 23:36:02.285 UTC [120] DETAIL:  parameters: $1 = '3dd13915-93fd-47ba-8715-886f33d749bb'

2021-12-20 23:36:02.286 UTC [122] LOG:  execute <unnamed>: SELECT * FROM accessibility_request_status_records WHERE request_id=$1 ORDER BY created_at DESC LIMIT 1;
2021-12-20 23:36:02.286 UTC [122] DETAIL:  parameters: $1 = 'bea5c7a4-cf84-4aea-9300-5c8828aa1866'
```

This could cause some scalability issues as the number of records in our database goes up. It's also a potential issue when querying CEDAR; see [this PR comment](https://github.com/cms-enterprise/easi-app/pull/1406#discussion_r778218474) as an example where the n+1 problem prevents us from optimizing our GraphQL schema.

## Considered Alternatives

* Do nothing.
* Use a dataloader-based approach for batching multiple queries. See https://github.com/graphql/dataloader  and https://gqlgen.com/reference/dataloaders/ for information on this general approach.
  * Implement this with the [`dataloaden`](https://github.com/vektah/dataloaden) library. The [`dataloaden-proof-of-concept` branch](https://github.com/cms-enterprise/easi-app/tree/dataloaden-proof-of-concept) has a proof of concept for using this, which batches the SQL queries.
  * Implement this with the [`graph-gophers/dataloader`](https://github.com/graph-gophers/dataloader) library.


## Decision Outcome

* Chosen Alternative: Do nothing for now (though keep an eye on the issue going forward)
  * This isn't currently causing us problems. If it starts to impact us in the future, we'll revisit this.


## Pros and Cons of the Alternatives

### Batch queries (general approach)

* `+` Definitely solves the issue when our database is the data source.
* `-` May not necessarily work when querying CEDAR. The CEDAR endpoints would need to support searching by multiple IDs, i.e. searching for deployments for multiple separate system IDs.

### Implement batching with `dataloaden`

* `+` Proof-of-concept works.
* `+` Is the recommended dataloader library by `gqlgen`, which is what we use as our general GraphQL framework.
* `-` The `dataloaden` library hasn't been updated since 2019, which means any bugs aren't likely to be fixed.

### Implement batching with `graph-gophers/dataloader`

* `+` Library seems to be more actively maintained.
* `-` Needs a proof-of-concept to make sure this works with our `gqlgen`-based code (though it should, see [discussion on GitHub](https://github.com/graph-gophers/dataloader/issues/79)).

### Do nothing

* `+` Minimum effort required.
* `+` The problem doesn't appear severe right now, especially when EASi's database is the data source, due to the small amount of data we're dealing with.
* `-` Doesn't address the problem; with a larger data set in our database, or with more data being requested from CEDAR, we could run into issues with our backend taking a long time to resolve a GraphQL query.
