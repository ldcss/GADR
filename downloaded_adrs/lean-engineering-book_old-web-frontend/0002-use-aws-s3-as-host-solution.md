# [Use AWS S3 as Host Solution]

* Status: [accepted]
* Date: [2020-02-28]

## Context and Problem Statement

We need to host our web application so clients can access it. The solution must be easy to manage and update.

## Decision Drivers

* Easy to update
* High availability
* Easy to configure HTTPS
* Observability

## Considered Options

* [AWS S3](https://aws.amazon.com/s3/)
* [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/)
* [Google Cloud Storage](https://cloud.google.com/storage/)

## Decision Outcome

Chosen option: "AWS", because it's the one we have the most experience. The 3 solutions analyzed are pretty similar in regard to the drivers considered. Given that, we made our decision based on our previous experience.

## Pros and Cons of the Options

### Amazon S3

- [Host a Static Website](https://aws.amazon.com/getting-started/projects/host-static-website/?trk=s3-gs)

* Good, because we can [enable server access logging](https://docs.aws.amazon.com/AmazonS3/latest/dev/ServerLogs.html)
* Good, because it is easy to update the deployment - [aws s3 sync](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html)
* Good, because of extensive documentation and guides
* Good, because it's possible to configure HTTPS with [Amazon CloudFront](https://aws.amazon.com/cloudfront/?nc2=h_ql_prod_nt_cf)
* Good, because we can enable server side encryption
* Bad, because it's not the cheapest (but also it's not the most expensive)

### Azure Blob Storage

- [Tutorial: Host a Static Website on Blob Storage](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website-host)

* Good, because we can [enable storage analytics logging](https://docs.microsoft.com/en-us/azure/storage/common/storage-analytics-logging?toc=%2fazure%2fstorage%2fblobs%2ftoc.json)
* Good, because it is easy to update the deployment - [az storage blob sync](https://docs.microsoft.com/en-us/cli/azure/storage/blob?view=azure-cli-latest#az-storage-blob-sync)
* Good, because it's possible to configure HTTPS with [Azure CDN](https://docs.microsoft.com/en-us/azure/cdn/cdn-overview)
* Good, because data is automatically encripted at rest
* Good, because it's the cheapest
* Bad, because documentation is a little cumbersome

### Google Cloud Storage

- [Hosting a static website](https://cloud.google.com/storage/docs/hosting-static-website)

* Good, because we can enable access logs
* Good, because it is easy to update the deployment - [gsutil rsync](https://cloud.google.com/storage/docs/gsutil/commands/rsync)
* Good, because we can enable server side encryption
* Good, because of extensive documentation and guides
* Bad, because it's the most expensive
