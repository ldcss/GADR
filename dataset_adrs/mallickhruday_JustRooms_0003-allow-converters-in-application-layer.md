# 3. Allow Converters In Application Layer

Date: 2019-07-31

## Status

Accepted

## Context

A clean architecture depends inwards, putting I/O concerns at its boundary/adapter layer. DynamoDB has an object model that allows us to mark up an entity with persistence information. 

By adding this persistence information to the entity, in the form of attributes, we couple the application to a persistence concern--how do we persist these entities to DynamoDB, which would be redundant if we changed how we stored the entity.

In addition, we have to add converter classes to the Application layer, as the attribute markup needs to know how to persist a 'custom' field type, which contains information on DynamoDB stores values.

The alternative is to use a DTO, marked up with DynamoDB attributes in the boundary/adapter layer, and then use automapper in the ports/interactors layer to map to and from DTOs.

## Decision

Allow markup on the entity and put converters in the application layer. As we 'own' our own tables in Dynamo the risk of coupling to them is low, and the use of attributes is orthogonal to the code, allowing them to be easily removed if we were to change DB. This is tradeed-off against the cost of having to implement the DTO and autommapper.

## Consequences

The application layer is couple to the AWS SDK
