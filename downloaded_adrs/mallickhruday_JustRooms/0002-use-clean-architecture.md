# 2. Use Clean Architecture

Date: 2019-07-31

## Status

Accepted

## Context

We need to decide how to structure our application so as to lower coupling and improve cohesion.

## Decision

We intend to use a clean architecture, particularly a hexagonal style

## Consequences

This project uses a clean architecture approach and 'depends inwards'. So the Adapters depends on the Ports, which in turn depends on the Application.

The 'Application' is the ports & adapters term for the domain model.

This means that the Application layer cannot depend on types defined in the Ports or Adapters layers. And it means that the Ports layer cannot depend on types defined in the Adapters layer.

As a result in places we use Inversion of Control, defining an interface at a lower layer that is implemented at a higher layer. So we define IRepository style interfaces in the Ports layer that are defined in the Adapter layer.

As a rule, we keep co-ordination and control of the 'use case' in the ports layer and don't allow it to bleed into the domain. So the domain should rarely need to use Inversion of Control.
 
