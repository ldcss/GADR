# 11. Resources And Endpoints

Date: 2020-02-05

## Integrations

|Name|Status|Integrates/With|Repo|
|:-|:-|:-|:-|
|<a name="integrations-deputy-reporting"></a> Deputy Reporting|In development|Digideps / Sirius|[https://github.com/ministryofjustice/opg-data-deputy-reporting](https://github.com/ministryofjustice/opg-data-deputy-reporting)|

## Resources and Endpoints

## Root

|Action|Method|Endpoint|
|:-|:-|:-|
|Health|GET| /healthcheck|

## Reports

|Action|Method|Endpoint|Integrations|
|:-|:-|:-|:-|
|Health|GET| /reports?healthcheck|[deputy-reporting](#integrations-deputy-reporting)|
|Create|POST| /clients/{caseref}/reports|[deputy-reporting](#integrations-deputy-reporting)|

## Supporting Documents

|Action|Method|Endpoint|Integrations|
|:-|:-|:-|:-|
|Create|POST| /clients/{caseref}/reports/{id}/supportingdocuments|[deputy-reporting](#integrations-deputy-reporting)|