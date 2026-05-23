# 1. Structure of Classes Beyond Standard RailsMVC

Date: 2019-02-07

## Status

Accepted

## Context

There are many ways to structure classes beyond the standard rails Model View Controller (MVC) structure, therefore to help make the project maintainable in the future we have come up with the following standards.

## Decision

* Avoid Helpers
  * The rational behind this decision is standard rails helpers are hard to test efficiently and are global so they can have unintended consequences.
  
* Use a Decorators directory `app/decorators`
  * Decorators should be used for read only operations that modify the data for viewing purposes.

* Use a ChangeSet directory `app/change_sets`
  * ChangeSet should be used for reformatting the data for purposes of showing it to user/system for modification.
  * We have kept the change set concept since these classes can also be useful for data import not just user facing formats.

* Use a Services directory `app/services`
  * Services should be used for encapsulating complex actions or actions that work across multiple models, like seeding or importing bulk data. These may change the underlying data structures.

* Use a Mailer directory `app/mailer`
  * Notifications will be put in the mailer directory so that we can stick with the standard defined by ActionMailer

### Possible Future needs

We currently believe that the business logic operations that are required for the system will be small enough to live directly on their primary model.  If in the future the models become too bloated we recommend creating a BusinessRules directory `app/business_rules`. BusinessRules would be a corollary to Services, for complex or model-spanning read-only logic.

## Consequences

* This organization makes sense to us, but it's a little different from Rails standard, and a little more like Figgy
* Developers who are familiar with these patterns will understand the division and patterns being used
* Developers who aren't familiar with change_sets or services might take more time to find the code we are separating out.
