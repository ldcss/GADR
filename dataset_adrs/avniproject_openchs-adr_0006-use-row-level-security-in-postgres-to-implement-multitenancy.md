# 6. Use row-level-security in Postgres to implement multitenancy

Date: 2018-05-16

## Status

Accepted

## Context

Multitenancy is required because we are now deploying openchs-server on the cloud. This can be achieved by
1. Multiple databases
2. Multiple schemas
3. Same database with a discriminator column

### Constraints
1. An organisation should not be able to view or update another organisation's data
2. There is common metadata for forms, concepts that organisations can override

### Other concerns/requirements
1. The architecture should prevent mistakes in code to leak data from one organisation to another
2. Maintaining multiple copies of metadata (if using multiple dbs/schemas) is hard
3. Data per organisation is low


## Decision

 - Use discriminators to achieve multitenancy. 
 - Enforce multitenancy using Postgres RLS policies
 - Create a hierarchical organisation structure where organisations can read metadata from current or parent organisations, and read/write data for their own organisation
 - Use OpenCHS as the grandparent organisation. It will hold the default program metadata

## Consequences

 - Additions a form element to an organisation can be done through a new row. But deletion cannot be. So, for each table that needs deletion of rows per organisation, there will be a non_applicable_table that handles organisation specific deletes
  - Any change to OpenCHS organisation will automatically propagate to all organisations. This might not be desirable in the future
