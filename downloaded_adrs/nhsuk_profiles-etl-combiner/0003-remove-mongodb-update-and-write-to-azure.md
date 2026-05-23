# 3. Remove MongoDB update and write to Azure

Date: 2017-06-21

## Status

Accepted

## Context

The merge of the data sources is a common operation from which the generated asset can be used by several different processes.
Currently the generated asset is only available for the immediately following process within this application i.e. updating MongoDB.
There is an immediate need to use the same generated asset for updating Elasticsearch.

The [mongodb-updater](https://github.com/nhsuk/mongodb-updater) service is able to update a MongoDB database from a JSON file available at a URL.

## Decision

The `gp-data-merged.json` file will be written to the team's preferred cloud hosting platform, enabling the merged data to be used as a
source for both the `mongodb-updater` and the forthcoming `elasticsearch-updater`.

## Consequences

A `gp-data-merged.json` file will be available in cloud storage for use by consuming applications.

The MongoDB updating code will be removed and an instance of the generic [mongodb-updater](https://github.com/nhsuk/mongodb-updater)
will be configured to update the profiles database from the merged data instead.

The repository will be renamed from `profiles-db-updater` to `profiles-etl-combiner` to reflect the new behaviour.
