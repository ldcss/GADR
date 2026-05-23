# ADR004: Create a Database of Public Sector Domains

## Status

Pending

## Context

The accessibility monitoring team have to test "a diverse, representative and geographically balanced distribution" of public sector websites.

In order that no public sector website is excluded from potential scrutiny, it follows that the team will need to have a full list of websites that are in the public sector, together with the type of service (e.g. education, health, central/local government etc) and, where applicable, geographical location.

There are two approaches to creating such a list:
1. **Domain-led:** Find every domain that has been registered to an organisation that is deemed to be "public sector" and determine the organisation that owns it
2. **Organisation-led:** Find every organisation that is deemed to be "public sector" and every service that each such organisation runs online, and find the corresponding website.

### 1. Domain-led strategy
The limitation of (1) is that (with certain exceptions, e.g. .ac.uk and .gov.uk) there is no regulation over what top-level domain should be used by the many flavours of public sector organisations. They could be anywhere.  

At the time of writing (July 2020) there are approximately 1.7 billion websites in the world, hosted on 409 million domain names. The websites we're looking for could be hosted on \*.uk domains or generic .com/.net/.org (or even .me, .info, .tv or any potentially any other "generic TLD").  
Of the 149m country-specific domains registered, 7% (~10.5M domains) are \*.uk, so we can at least exclude the other 93% (139m) non-UK country-specific domains (that is, we are very unlikely to find a UK public sector website hosted on a .tk or .ru domain, for instance\*).  
That leaves a mere 270m domains that Public Sector websites could potentially be hosted on. Scouring those domains for websites that fall into the definition of "uk public sector" would be a lengthy and resource-intensive task.

Nevertheless, a list of the domains that we can be sure are public sector, and that we can retrieve data about, would give the accessibility monitoring team a good range to select from.  
The domains that fall into this category are:
* gov.uk
* nhs.uk
* nhs.net
* ac.uk
* sch.uk
* police.uk
* parliament.uk
* mod.uk
* gov.wales
* llyw.cymru
* gov.scot

### 2. Organisation-led strategy
It should be feasible to compile a list of organisation _types_ that are in the public sector (e.g. "schools", "central government", "local authorities", Universities", "NHS").   
We can then move onto making lists of the actual _organisations_ in each of those categories by referring to the bodies that regulate them.

A lot of this information is online in one form or other, but certainly not all of it.

Some initial work has been done by the accessibility monitoring team already, with the result being a "list of lists" that is currently in a Google Sheets spreadsheet. Each of these lists - in various formats - would need to be somehow imported into the database. Where a website for the organisation in the list is specified, this can be added to the domains list.

## Decision

Our intention is to use both strategies.

* We will create a **database of public sector domains**.
* We will populate it with lists of domains and organisations from official sources, together with, as far as possible, contact details and other useful data such as page ranking, http(s) status.
* We will also use the data gleaned from domain registers etc to seed a list of **public sector organisations**.
* We will compile a list of public sector categories which will form a list-of-lists; these lists will then be used to further populate the database of organisations.
* Organisations will be categorised by location (including "national") and by sector (probably using [the definitions of "organisations" categorised for the Local Governments Association by ESD](https://standards.esd.org.uk/?uri=list%2ForganisationTypes))
* Wherever possible, links will be created between the domains and organisations. At some point in the future, organisations that don't have associated domains will need to have their associated websites found and entered into the database so that automated testing can be carried out.

## Consequences

There's a lot of work to be done in gathering, cleansing and categorising the data.

This pair of tables and associated sub-tables will need to be maintained somehow. Currently there is no resource allocated to do so, nor any plans to place the resource under the auspices of a team to specifically curate it.

A definitive list of public sector organisations (and their websites) would be useful in many areas of government (and possibly beyond). This could form the foundation of something much bigger if we can get interest from the architect/data communities.


_\* There are, of course, exceptions. For instance, the "Germany Enabling Office" is an organisation "supporting the British Forces community and UK Defence in Germany". It is hosted at [bfgnet.de](https://bfgnet.de)._
