# 5. Use AWS RDS Aurora MySQL for database persistence

Date: 2017-10-20

## Status

Accepted

## Context

Bookit needs a persistence mechanism.  There are many to choose from that fit an application's needs.  Currently, we believe a SQL/RDBMS approach fits better than NoSQL.  There's not a lot of context to add to that, just a quick poll of the engineers when we kicked off the project.  With that in mind, we wanted something hosted/PaaS.  

Given we're in AWS, RDS is an obvious choice.  We don't currently have a preference for DB vendor/implementation, but are drawn to open source and free.  MySql and PostgreSql fit that criteria.

Further, AWS RDS has their own MySql implementation which provides much better performance and up to the minute backups with no degredation for fractions of a penny/hr more than the standard MySql over RDS.  And while Bookit's usage might not warrant the need for higher performance, there is always a need for high availability and Aurora provides that in a very hands off way.  There is also an Aurora implentation for PostgreSql but at the time of this decision, that is in Preview so we decided to skip it.

## Decision

Use AWS RDS Aurora MySql implemntation for our database persistence mechansim.  Create via Riglet CloudFormation stacks.  Production will run with 1 primary and 1 replica for HA.  Staging & Integration will run with only 1 Primary to keep costs down.

## Consequences

* SQL/RDBMS systems will allow us to utilize ORM technologies to quickly hook up a persistence layer.
* We might find later that a NoSql document storage mechanism fits our use cases better and can adjust then.
* Aurora is slightly more expensive than RDS MySql/PostgreSql, but only by $0.004/hr.
* We don't plan on utilizing any vendor specific improvements to SQL standard.  This enables us to change our mind on DB vendor at a later date.
