# ADRXXX: Title

## Status

Pending

## Context
We currently have a "public sector domains" table (along with an "organisations" table containing the owners of the domains).
However, many organisations have websites that are not on their own domain but in a subfolder of another domain. Moreover, many _services_ reside in subfolders or other logical locations.
Each of these needs to be treated as a separate "website" in the context of accessibility monitoring.
Thus, we either change the "public sector domains" table to include all websites, not just unique domains, OR we create a new table specifically for public sector websites and initially copy over those domains that we can confirm are definitely websites.

The domains table is useful in and of itself as a repository of registered domains. We should keep and maintain this as-is.

## Decision

We will create and populate a new table in the PubSecDomains schema that contains:
* url
* name of the service
* the site's title from its HTML <head><title> element, where given
* the site's description from its <head><meta name="description"> element, where given
* last_updated timestamp
* the website's sector (foreign key to sectors table)
* many-to-many join to the existing Organisations table (one site can, surprisingly, come under the auspices of more than one organisation; obviously one organisation can have multiple websites for their various services)


## Consequences
It's one more table to maintain (see ADR004).
