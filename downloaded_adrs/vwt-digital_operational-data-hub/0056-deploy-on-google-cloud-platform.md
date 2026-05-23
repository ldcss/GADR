# 56. Deploy on Google Cloud Platform

Date: 2020-09-22

## Status

Accepted

Implements [3. Create cloud native solutions](0003-create-cloud-native-solutions.md)

## Context

Running a cloud-native solution requires a cloud platform. Building or running our own would not be possible due to budget and time constraints, public cloud is a more efficient solution. During Q1 2019 both Microsoft Azure and Google Cloud Platform (GCP) were considered. Differences were especially found on these aspects:
* [Serverless](0002-use-serverless-infra-components.md): Azure services we need were found to be billed more time-based. The service is either on (and can be used) or off (not available) and is billed per second it is turned on. GCP billing was based on the actual execution count. Also [Python](0042-python-version-3.md) cloud function support was at higher availability on GCP.
* [Software defined](0004-create-software-defined-everything.md): Azure pipelines (yaml) were found to be at lower level compared to GCP, both on functional and non-functional requirements.
* [Security by design](0006-implement-security-by-design.md): service accounts are used for permissioning in all components on GCP. On Azure this is still work in progress. Azure relied on authentication based on secrets (keys), which means more configuration and higher security risk.
Data at rest is always encrypted on GCP (not even possible to turn this off), Azure still allowed unencrypted storage.
* [Data integrated](0007-solutions-are-data-integrated.md): GCP components all have an API based on REST principles, also allowing cloud platform information. Azure APIs are less consistent and not available for all cloud components.
* [Location-aware (xyzt)](0008-data-is-location-and-time-aware.md): Google Maps is integrated in GCP, Azure does not integrate with map functionality.
* Components on GCP are more integrated compared to Azure. Azure is build from independently build components combined together in a web-portal. GCP integration is at a deeper level resulting in a more natural cooperation between components. For example, the service accounts (mentioned above) on GCP used by all components compare to the storage-specific account on Azure and the integrated Cloud Build service on GCP compared to the Azure DevOps approach.
* Documentation is more complete on GCP compared to the more ambiguous Azure documentation that can be found on the Internet. 
* Implementation of new cloud platform functionality is done [API-first](0043-api-first.md) on GCP, followed by console/portal and command line tools. Azure first provides portal access and might deliver an API later on. In automation an API is way more important compared to portal availability.

## Decision

We will deploy our cloud-native solutions on the Google Cloud Platform.

## Consequences

### Advantages

A Cloud Platform facilitating the services needed to deploy our cloud-native solutions, fulfilling both our functional and non-functional requirements.

### Disadvantages

Companies experience with GCP is less compared to Microsoft technology.
