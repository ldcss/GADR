# 3. Use one domain 

Date: 2018-07-05

## Status

Approved

Approved TDDA 2018-12-18
Review by March 2019

## Abstract

Use one domain for buyer journeys for all five agreements in beta.

Once we understand the solution we can factor out multiple web components and domains later.

## Context

We are currently building a digital service to enable buyers on five CCS frameworks to specify requirements and 
shortlist suppliers online. This MVP will form the basis of a broader service to be delivered iteratively which 
will ultimately enable buyers to run competitions and make awards online as a single service. 

The MVP will also establish a model and foundation for extending the digital service to other frameworks managed by CCS. 

The five frameworks for MVP are spread across different pillars and business areas, and therefore have different user bases, and users with different needs. 

It is likely that users in organisations like schools will make use of more than one of the five initial frameworks - they may use Supply Teachers for their short term staffing needs, and Facilities Management less regularly for their maintenance and facilities needs. 

However, it is also likely that a large proportion of users of one of the frameworks will rarely if ever use one of the other 4. We expect that in the future when more and more frameworks make use of the digital platform, the likelihood of a single user regularly using more than one framework will increase. 

Users from different organisations and with different needs for goods or services are likely to arrive at the service through different routes - perhaps through GOV.UK, the CCS website, or other government services. 

The CMp infrastructure supports any number of web facing components deployed as individual subdomains under a single automatically managed domain record.


## Decision

### We will use a single domain for all commercial agreement journeys for buyers

We will use a single domain for all framework journeys for buyers rather than a different domain for each commercial agreement.

This will minimise the maintenance overhead of managing one domain per framework which will become particularly cumbersome as the platform grows over time. 

This will also ensure that the experience for users remains simple over time, maintaining the flexibility to distinguish or combine routes in to the service to ensure that they continue to match buyer behaviour, searching patterns, and purchasing needs even as the number of frameworks grows. 

A single domain ensures that this kind of simplicity can be maintained at lower cost (changes inside the service being cheaper to make and lower impact on users than changes to the underlying infrastructure) whilst the service scales in size and complexity.

The domain will be:

 ```
 marketplace.service.crowncommercial.gov.uk
 ```


## Consequences

This decision may change as we learn more about the best way to build the service as a scalable foundation making use of common components, infrastructure and data sources. 

For example we may choose to use a different domain for a buyer finding an agreement, and another domain for 
competing an agreement with one or more suppliers.

Having a single component for all user journeys raises a small risk when different journeys have different security recquirements. It may well be indicated to move parts of journeys that have a higer or different security profile to different web components. 
