# Sample Service / Relation Engine data linking design document

## Background

See [link_ws_data_to_sample.md](link_ws_data_to_sample.md).

## Document purpose

Flesh out Option 1 of the Sample Service data linking options, e.g. link data to samples
in the RE database, not via workspace annotations.

## General design considerations

* A user having access to a sample **does not** mean they necessarily have access to data linked
  to that sample. They must have explicit workspace permissions for the data.
* A user having access to data linked to a sample **does** have read access to the sample.
* When creating a new version of a sample, data links are not automatically updated.
  * This could be a feature in the future, either automatically or on request.
* A particular data unit can be linked to only one sample.
    * A workspace object may contain multiple data units - a matrix containing data from many
        samples, for example.
    * The data unit can be linked to multiple versions of the sample

## Definitions

* SS - Sample Service
* WSS - Workspace Service
* RE - Relation Engine
* SIDV - Sample ID and version. The ID of the sample and version of the sample. Omitting the
  version indicates the most recent version should be used, but this is obviously subject to
  race conditions.
* UPA - Unique Permanent Address. A unique identifier for an object in the workspace.
* Data unit - A cohesive unit of data taken from a single sample. A workspace object may contain
  many data units.
* DUID - Data Unit ID. A unique identifier for a data unit - an UPA and optionally an identifer for
  data within the data object.

## Operations

### Link data to a sample

1. Make request to SS with the SIDV and DUID.
    * May want a bulk method, especially for linking columns of a matrix to multiple samples.
    * May need to associate metadata with the link, e.g. denoting to which column of a matrix
      the link refers.
2. SS checks that the user has admin access to the sample.
    * Links from data -> sample grant read permission to the sample, and thus creating links
      is equivalent to having admin privileges for the sample.
    * **OPEN QUESTION**: Do we want an explicit link data permission or is admin ok?
        * For now just use admin.
        * **OPEN QUESTION**: Should link data perms implictly grant write perms? If not,
            permissions become non-monotonic, which is unfortunate.
    * SampleSets do not affect whether a user can link data to the samples contained therein.
3. SS checks that the user has X permission to the data.
    * **OPEN QUESTION**: What permission is required for data in order to link it to a sample?
        * Links grant no special privileges for linked data.
        * What if another stakeholder of the data doesn't want the data linked?
            * Perhaps write or admin access should be required.
        * Since this effectively modifies the data, require write permissions for now.
4. SS adds a link from the WSS shadow object in the RE to the appropriate node in the sample.
    * SS checks that the object has no more than 10K links to samples and the sample has no more
        than 10K links to objects
        * See [Slack conversation](https://kbase.slack.com/archives/CNRT78G66/p1583968517059500)
    * This probably requires a transaction to ensure the data unit is not linked to any other
      samples or other nodes in the same sample as well as the above.
        * It can be linked to other versions of the same sample.
            * In this case, the old link should be expired (time traveling).
    * **OPEN QUESTION**: Should the SS verify the data unit ID somehow? That seems really
      expensive and really complicated - would need a verifier for each type or the
      types would have to put the IDs in a standard location in the JSON.
        * Don't verify for now, complicated and expensive.

### Update or delete a link
1. Essentially the same steps as linking data except:
    * The older version of the link should be expired.
    * The 10K limit doesn't apply.
    * This can be implemented last.

### View data linked to a sample

1. Make a request to the SS with the SIDV and optionally a timestamp for time travelling queries.
2. The SS checks that the user has read access to the sample.
3. The SS gets the list of workspaces to which the user has read access from the WSS.
4. The SS performs a traversal from the version node in the sample to WSS shadow objects where the
   workspace ID is in the list of accessible workspaces.
5. The SS returns the list of UPAs.
    * This list is limited to 10K objects (see above) and so may be returned in bulk or sorted
      without major cpu or memory concerns.
   * **OPEN QUESTION** May also want to query on workspace object properties. Node indexes on
      these properties could speed up the query.
      * Don't support for now.

### View samples linked from data

1. Make a request to the SS with the DUID of the data and optionally a timestamp for time
    travelling queries.
2. The SS checks that the user has read access to the UPA.
3. The SS performs a traversal from the WSS shadow object in the RE through connected sample nodes
   to the sample tree root.
   * **OPEN QUESTION** May want to query on sample metadata.
      * May need to restructure the sample metadata to make this possible.
        * IIUC, only equality queries can be done on arrays of documents when using an index.
            * Maybe not using an index is ok.
        * On the other hand, if we separate metadata into separate documents that's going to make
         the document count explode and traversals may not be possible.
      * How does the metadata of parent nodes of the linked node in the sample affect the query?
          * Is metadata inherited? Should we duplicate parent metadata to children in the DB?
      * Don't support for now.
   * This list is limited to 10K objects (see above) and so may be returned in bulk or sorted
      without major cpu or memory concerns.
   * **OPEN QUESTiON** Exclude all but the latest sample version?
     * Not sure if this is possible in query or needs to be done in the server
     * Support a toggle in the API

### Other operations

* Missing any?

### More complex query examples

* Given a taxon and a sample, find all WSS objects that are linked to both
* Find all genomes with a specific gene linked to sample sets in a subset of workspaces.

## Design implications

* If a WSS object linked to a sample is copied, the copy will not be linked to the sample.


