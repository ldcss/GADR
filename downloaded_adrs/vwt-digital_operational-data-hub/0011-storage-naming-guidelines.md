# 11. Storage naming guidelines

Date: 2021-04-26

## Status

Accepted

## Context

We feel the need to use naming guidelines for Google Cloud Platform (GCP) storage.

## Decision

We identify rules for the storage name, the path on the storage and for the filename.

### Storage name

The storage name should always start with the product ID of the GCP project the storage is in followed by a clear name of what kind of data the storage contains and the name should end with "stg". If we take as example a storage that contains data about employees, its storage-name could be ```project-id-employees-stg```.

### Path

The path of a storage should always start with a folder that has a clear name that describes the data it contains best.
The part of the path before the file should always be year/month/day. Where the year and month are zero padded.
An example of a normal GCP path would be: ```{storage-name/}clear-data-name/2021/04/26/file-name```.

#### Source

If the storage files come from outside GCP, the path should then start with “source” followed by the clear data name, year, month and day. An example of such a path would be ```{storage-name/}source/clear-data-name/year/month/day/file-name```.

### Filename

A filename on a GCP storage should always be “timestamp-UUID.extension”, where the timestamp’s format is ISO8601 so that it is readable by humans. The timestamp is the time when the file was uploaded. An example would be ```20210426T000011Z-c6995d8d-670c-470d-8fae-498e31ad8ad7.json```

#### Source

If the storage files come from outside of GCP, the storage file should have meta data containing the original path of the file. For example, if the file comes from an Azure fileshare with path ```azure-fileshare-name/export/file-name```, then this path should be added to the meta data.

## Consequences
