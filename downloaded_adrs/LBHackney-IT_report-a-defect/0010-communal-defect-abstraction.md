# 10. communal-defect-abstraction

Date: 2019-07-12

This ADR is being added retrospectively to the work done on the back of this decision on the 27th June: https://github.com/LBHackney-IT/report-a-defect/pull/59

## Status

Accepted

## Context

The New Builds Team manages defects for individual properties as well as those for communal areas like shared lifts or parking areas. Before this decision the service only supports creating defects against individual properties.

The data we have is that 70% of defects are at the property level and 30% are for communal areas.

The primary user need is to allow the New Build Team to create communal defects which provide the contractor with a location/address and access information so that they can arrive at the right location first time and fix the defect.

The secondary business need is that Hackney can repurpose all defect data with other digital services so they can make provide a better experience to residents in terms of repair management and future purchasing decisions.

The new build team have to manually create a minimal viable data hierarchy within the service of schemes and properties. This replicates what they were doing previously in Google Spreadsheets and is a step forward towards setting up an integration with can automate this effort.

We have found that the existing data hierarchy for the concepts of estates, schemes, cores, blocks and sub-blocks is inconsistent between Universal Housing, the Property API and the previous workflow that the New Build Team used. We were unable to find consistent and clear definitions for which to use in each scenario.   

We learnt that data hierarchy is being reviewed with the potential for the Addresses API to become responsible for this as a strategic decision in becoming less dependent on Universal Housing.

We have learnt that an older Hackney service called the Repairs Hub has had difficulty in trying to solve the same problem in figuring out the right hierarchy and instead of using the Property API has used the Repairs API as a proxy to get meaningful data on properties: https://github.com/LBHackney-IT/repairs-management/blob/develop/app/models/hackney/property.rb#L12. We don't believe that coupling the defect service to property information in the same way is beneficial as it would increase technical debt. We presume there is an ambition that property data should be made available only through either the Property API or the Addresses API, and that there will be less cost in Hackney only having to have to migrate 1 service instead of 2.

## Decision

We have decided to abstract the concept of communal hierarchy into a single flexible concept called 'Communal areas'.

A Scheme will have many properties and many communal areas, each can have many defects.

To solve the primary user need communal areas require:

- a `name` for the NBT to manage defects with a consistent grouping
- a `location` that will allow the contractor to receive a single address or set of addresses via email

## Consequences

- this choice requires minimal effort in the short term, allowing us to spend the little time we have remaining to focus on delivering a service that solves the primary user need. Without a service that's fit for purpose for the New Build Team, we risk Google Sheets having to remain meaning there would be no potential to share any defect data to other Hackney services. We feel that being able to share 70% of defect data for properties is better than trying to build something that _could_ share 100% but isn't used by the users
- this provides the New Build Team a lot of flexibility in being able to report defects for physical areas that make sense. Future decisions can on hierarchy can be made with data by looking what communal areas are being created
- there is no primary identify for communal areas like there is for a property in the UPRN which makes this 30% of defect data hard to share with other services until another step forward is taken
