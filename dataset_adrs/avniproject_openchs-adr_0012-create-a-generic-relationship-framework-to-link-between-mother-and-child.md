# 12. Create a generic relationship framework to link between mother and child

Date: 2018-05-28

## Status

Accepted

## Context

During a delivery for a mother in the mother program, we will need to create one or more new children. Filling in details during delivery and during PNC visits will need switching between them easy. 

At the same time, we are also thinking of creating the concept of a family. Here, the individuals of a family will be linked to the head of the household through a relationship. 

We need the modeling of a relationship to be a generic structure that can support both these use cases. 

## Decision

Create an option to map relationships between individuals, with relationship being a concept orthogonal to families. Relationships between individuals can be anything (family relationships, or even relationships to ASHA worker etc if required). 

Relationships will be two-way with different values between the two. We will not build (atleast for now) the ability to automatically deduce transitive relationships. 

## Consequences

Support for family can be turned off if it is not required for an organisation. 
Development for the family feature and mother-child linking can happen in parallel without dependencies. 
There will be individuals that are related, but are not part of the same family. It is possible that some of them are not part of any family. The user is expected to do this manually. 
