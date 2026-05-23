# ARD-0001 Technology Stack and Deployment

## Context
*This section describes the forces at play, including technological, political, social, and project local. 
These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. 
It is simply describing facts.*

The Office of Development Transformation (ODT) is focused on helping CAD learn and adopt lean, agile, and devOps techniques and 
processes. ODT will be initialy focus on Green Field Developent. The Online Bank is a sample app used in the ODT University classes.  The Purpose of theapplication is to provide a 
sample app as a context for the training courses.  We believe most people are familiar with online
banking, and won't need to spend a lot of time learning the problem domain.

The purpose of this document is to determine the technology stack for the sample application.

**NOTE:** While we are initially focused on a Java Web stack, we may elect to develop out an example in the Microsoft Stack.
If you would like to help, please contact us.


## Decision
*This section describes our response to these forces. It is stated in full sentences, with active voice. 
"We will ..."*

We will be focusing on the modern web java stack.

### UI Technology Stack:
- Angular 2
- Bootstrap
- protractor
- jasmine 

### Server Side Technology Stack:
- Java 1.8+
- SpringBoot 1.4+
- Restful 
- MySQL
- Spring Data JPA (Hibernate)
- JUnit 5 / Spock

### Development Technology Stack:
- Local Development
- SCM: GIT
- Intellij
- Favorite Editor
- Gradle
- Angular Quickstart
- Concourse CI (CI/CD)
- Jira
- Sonar

#### Deployment: 
- Pivotal Cloud Foundry (Java and Static Build Packs)

## Status
*A decision may be "proposed" if the project stakeholders haven't agreed with it yet, or "accepted" once it is agreed. 
If a later ADR changes or reverses a decision, it may be marked as "deprecated" or "superseded" with a reference to its 
replacement.*
- Proposed - 11/2016
- Accepted - 12/2016

## Consequences
*This section describes the resulting context, after applying the decision. All consequences should be listed here, 
not just the "positive" ones. A particular decision may have positive, negative, and neutral consequences, but all of them 
affect the team and project in the future.*
