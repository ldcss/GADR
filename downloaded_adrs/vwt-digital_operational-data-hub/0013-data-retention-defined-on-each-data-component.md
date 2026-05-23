# 13. Data retention defined on each data component

Date: 2020-09-21

## Status

Accepted

Implements [4. Create software defined everything](0004-create-software-defined-everything.md)

Implemented by [53. Project company data](0053-project-company-data.md)

## Context

Data LifeCycle Management is a process that helps organisations to manage the flow of data throughout its lifecycle – from initial creation through to destruction. While there are many interpretations as to the various phases of a typical data lifecycle, they can be summarised as follows:
1. Creation: data acquisition or retrieval
2. Storage: storing the data
3. Usage: using the data to support activities in the organisation
4. Archival: keeping the data in case it is needed again
5. Destruction: removal of the data from the organisation

When storing data, we must make sure it is available for the time it is needed, but it should also be deleted when it is not needed again. This not only saves cost, but also ensures timely removal of Personal Identifiable Information compliant to GDPR.
Management of retention policies and life cycle (destruction) measures can be automated by specifying the period the data should be kept. Protecting the data from deletion during this period and purging it after ensures adherence to the temporal requirements on the data.

## Decision

We will specify a temporal for each dataset in a [Project Company Data](0053-project-company-data.md) data catalog, which will automatically result in retention policies and life cycle rules.

## Consequences

### Advantages

* Data life cycle management is embedded in the way of working.
* PII will be held as long as required, but not any longer, compliant to GDPR.
* Protection against accidental deletion of data.
* Cost will be limited as there's no endless growing storage.

### Disadvantages

* Data life time specified in temporal has to be specified up-front. When requirements change, the temporal should be changed as well.

## References

* https://www.dataworks.ie/5-stages-in-the-data-management-lifecycle-process/, retrieved 2 October 2020
