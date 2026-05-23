# ADR003: Choice of Tools and Platforms

## Status

Accepted

## Context

The choice of tools that will be built and used by the accessibility monitoring team are influenced by:

* Suitability to the task
* Cost and ongoing-cost (open-source preference)
* The [GDS Way](https://gds-way.cloudapps.digital/).

As defined in ADR002, we need to meet a number of requirements:
1. Maintaining an organised list of public sector websites
1. Picking websites to test from that list
1. Triaging each site
1. Prioritising sites for testing
1. Tracking the progress of testing on each website
1. Creating a report for the completed test
1. Sending the report to the site's owner
1. Managing and recording interaction with the site's owner


## Decision

We will...

### Use Zendesk
Rationale:
* GDS have a license for Zendesk.  
* It has an extensive, well-documented API.  
* There is a lot of experience in GDS of general usage, and a fair amount in using the API.  
* We have a sandbox Zendesk environment.

This will be the driver of testing work. Tickets will be created in Zendesk (manually or automatically) representing websites to test.  
They be prioritised in Zendesk and then be assigned to / picked up by Accessibility Officers.

Zendesk will also handle communication and follow-up with the site owner.

This satisfies items 5, 7 and 8 above.

### Use Postgres

* A relational database is best suited to the requirements for both a public sector domains database and the testing records
* It is open-source
* It is well supported and documented
* It is available as a "plug-and-play" service on [GOV.UK PaaS](https://www.cloud.service.gov.uk/) (see below)

This satisfies item 1 and facilitates items 2, 5 and 6.

### Use GOV.UK Platform-as-a-Service
* Meets GDS' [cloud-first policy](https://www.gov.uk/guidance/government-cloud-first-policy)
* VERY well supported with an extremely well-experienced and skilled team within GDS.
* Supports all of the chosen technologies

### Use Deque Axe
[Deque Axe](https://github.com/dequelabs/axe-core) is a 3rd-party, open-source tool that tests the web page that you give it against a set of predefined rules.

* It is open-source
* It can be run from the command-line and so can probably be automated.
* It produces results in a machine-readable format (JSON)

This satisfies item 3.

### Use the GOV.UK Design System for the front-end
The [GOV.UK Design System](https://design-system.service.gov.uk/) is a set of components, styles and patterns created by the GOV.UK team after extensive user-research.  
Not only does this serve as a ready-made template engine, but we know that it scores extremely highly on accessibility.

### Programming languages

* Use node.js for Axe-integration as it is well suited to asynchronous http calls.
* Use node.js (and nunjucks)for front-end code as that's what GOV.UK Design System is written in.
* Use Python 3 for Zendesk integration as there is a well-maintained open-source Python library.


### (Under review) Use PowerMapper SortSite
[SortSite](https://www.powermapper.com/products/sortsite/) by PowerMapper is a 3rd-party commercial product that is widely used in the testing of websites, and has a thorough accessibility checking feature. It also crawls a website and catalogues its pages, a function that Axe does not perform and would be useful to us.

However, it is not open-source and only runs in a Windows or MacOS environment, so would not be easy to integrate into an automated process.
There is a web service whereby a domain is submitted to it and it returns an HTML report, but this is not a machine-friendly format and would require screen-scraping and parsing - quite a major task, and one that's prone to breaking if/when SortSite changes its output format.

The site-mapping functionality of SortSite could be achieved with an existing open-source python or node library.


## Consequences

With various 3rd-party products and libraries, this system will need to be maintained in order to identify and mitigate breaking changes.
