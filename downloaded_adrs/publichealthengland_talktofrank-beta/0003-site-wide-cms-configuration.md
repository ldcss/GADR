# 3. Site wide CMS configuration 

Date: 2019-03-08

## Status

Proposed

## Context

Certain elements on the Talk To Frank site need to be loaded regardless of the user entry point, 
e.g. the current user story involves adding a warning message bar that appears on all pages.

The CMS needs to be updated to support the addition of site wide 'settings'.   


## Decision

A new 'site settings' content model will be created.  A 'Sitewide' item will then be created to contain all sitewide settings.

This would then allow for the following (future) setup, 

Content items of type 'site settings'
- Sitewide
- Homepage - any settings that should override the sitewide values on the homepage.  
- Drugs A-Z - any settings that should override the sitewide values on the Drugs A-Z page.  

References:
- https://www.contentful.com/r/knowledgebase/dynamic-microcopy/
- https://www.contentfulcommunity.com/t/is-it-common-to-have-a-settings-content-model/924/2


## Consequences

- Additional API calls would need to be made by the frontend framework to 
    1. fetch the sitewide settings
    2. check if there are any overrides for the current page
- Future page specific settings could be handled by adding a new 'Page url' field to the 
content model 

