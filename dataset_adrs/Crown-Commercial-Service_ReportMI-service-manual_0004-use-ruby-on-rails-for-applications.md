# 4. Use Ruby on Rails for applications

Date: 2018-06-06

## Status

Accepted

## Context

In [ADR-0002][adr-0002] we outlined the overall technical approach for the Data
Submission Service, and highlighted the components which we expect will be
developed.

This ADR focusses on the technology choice for building a portion of the
applications. In particular:

1. Submission app - the public facing front-end for suppliers to submit returns
1. Administration app - the front-end for CCS staff to support the operation of
the service
1. Onboarding app - the front-end for CCS staff to manage the onboarding of new
suppliers and commercial agreements
1. Data storage API - the API which these three applications use to store and
retrieve data

### Language and framework choice
There are many possible language and framework choices for the development
of the applications for this service.

The existing MISO service is built using C# and ASP.Net. Other services in CCS
use a mixture of PHP and Java/Spring. Digital Marketplace uses Python and GOV.UK
uses a mixture of Ruby with Rails and Sinatra, Python and GO.

Any decision we make about languages and frameworks should consider:
- The skill of the current team we have available to build the service - what
are the current team comfortable using?
- The skill of a future team - is there a large enough pool of suppliers and
contractors who could support and main the service in the future?
- External toolkits and modules - are there useful toolkits and modules which
could reduce development effort (eg the
[GOV.UK Frontend Toolkit][govuk-frontend-toolkit])
- Cost - what is the cost of developing in this way? Are there licence costs?
- Hosting - would picking this language restrict hosting options?

We should consider the Service Manual guide on
[choosing technology][service-manual-choosing-technology].

## Decision

We will use Ruby on Rails for the applications in the Data Submission Service

The development team is used to working with these choices, and there is a large
community of developers both inside and outside government using Ruby and Rails
for government digital services.


## Consequences

This choice will affect future support of the applications as it will require
knowledge of Ruby on Rails.

[adr-0002]: 0002-overall-technical-approach.md
[govuk-frontend-toolkit]: https://github.com/alphagov/govuk_frontend_toolkit
[service-manual-choosing-technology]: https://www.gov.uk/service-manual/technology/choosing-technology-an-introduction
