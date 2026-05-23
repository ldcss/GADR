# ADR2: Use Github over Trello for managing project boards

Managing projects using boards makes it easy to track the progress of the project. It assists the development team with identifying what tasks need to be completely, that have been completed and are in progress. Both Trello and Github provide the functionality to manage projects, as we already utilise Github for software development version control it is easier to utilise it's project managing features in our repository. 

Trello has the same functionality provided by Github to manage projects and it also contains a great user interface which provides ease of use for the user. Trello not being linked to the project repo in GitHub means that all the issues and statuses need to be manually updated consistantly to track the progress of the project.

However, with Github the status of issues are automatically updated.  When an assignee has completed their tasks and has requested a pull request, upon approval by the respective reviewers, it automatically closes the issue and updates the status to Done. Github also provides the added benefit of assigning team members to certain tasks and linking their issues to project milestones. 

## Decision

We have decided to use Github to manage our project boards.

## Status

Accepted

## Consequences
    * We do not have to worry about making mistakes when updating the status of issues because it will automatically be done for us.