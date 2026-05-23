
# Milestone 2: Detailed Design
## Overview
Simple Budget provides a simple interface for users to view and log their personal spending. To access their account, users will select their username from the list shown on the login page. They will then be directed to their summary page. The summary page shows an overview of the user’s past spending per category and selecting a category allows the users to view a detailed list of all their recent purchases in that category. From the summary page, users also have the option to log a new purchase into any category. Input fields will include the amount spent, a short description, the date and time of purchase (with default values to the current date and time), a choice of categories to log the purchase into. Input validation will be performed on the inputs and a confirmation will be displayed once the purchase has been successfully added to the database. 

This document describes the architecture of the Simple Budget web application. The following diagrams depict a high-level view of the system. The Architecture Design Records (ADR’s) explain the rationale behind some of the major design decisions. 

## Class Diagram
![Class Diagram](https://github.com/seng350/seng350f19-project-2-1/blob/master/docs/M2/class-diagram.png)
## Sequence Diagram
![Sequence Diagram](https://github.com/seng350/seng350f19-project-2-1/blob/master/docs/M2/sequence-diagram.png)
## ADRs
* [Impliment Postman API testing](https://github.com/seng350/seng350f19-project-2-1/blob/master/docs/M2/adr-impliment-postman-testing.md)
* [Update purchase summary and analytics with local data](https://github.com/seng350/seng350f19-project-2-1/blob/master/docs/M2/adr-update-with-local-data.md)
* [Storage layer DAOs](https://github.com/seng350/seng350f19-project-2-1/blob/master/docs/M2/adr-storage-layer-dao.md)
