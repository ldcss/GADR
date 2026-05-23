# Remove requirement for login for all pages

* Status: accepted
* Date: 2021-04-19

Technical Story: PLATUI-855

## Context and Problem Statement

Within contact-frontend, for the standalone pages, two routes into the page exist. The first requires a tax service 
user to be logged in, and redirects to login if the service user is not logged in. The second, on a different URL 
suffixed with "-unauthenticated", does not require login, but serves the same page. After discussion, the PlatUI team
decided that the requirement for a user to be logged in was making a worse experience for the service end user, adding
the requirement of login,when all the same functionality is also available without logging in via a different URL.

## Decision Drivers

* Current functionality with login leads to a possibly bad tax service user journey, in particular in the use case where
  a user is signed out in the background whilst trying to report an issue, given that all this functionality is
  available without login
* If a tax service user is logged in, but has clicked on a link to the unauthenticated version of the form, 
  contact-frontend currently doesn't even attempt to look up their enrolments, meaning potentially less information is
  persisted to Deskpro agents
* Requiring login for any of these technical problem report forms makes them less accessible and therefore makes the 
  site less likely to receive valuable user feedback in particular from users with additional accessibility needs
* From a development perspective, maintaining logged-in and non-logged in versions of the pages adds to complexity in
  the codebase, making our development process slower and our testing time longer

## Considered Options

* Keep login redirect and make no change
* Remove login redirect from all pages and keep existing endpoints for now
* Remove login redirect from all pages and remove the "-unauthenticated routes"

## Decision Outcome

Chosen option: "Remove login redirect from all pages and keep existing endpoints for now", because:
* The benefits to end users in terms of accessibility feel significant enough to warrant the change
* Information about logged in users will still be persisted to Deskpro but there will not be a redirect for users
  who have been logged out in the background
* Codebase is significantly simplified for developers working on contact-frontend
* However, deleting the "-unauthenticated" routes will be a major breaking change across the Platform, and should be 
  decoupled from this

### Positive Consequences

* Capturing information about all logged in users, not just the ones who have clicked on a contact-frontend route not
  ending in "-unauthenticated"
* More accessible experience for tax platform end users who are not forced to log in to report technical problems
* Significant simplification of codebase for developers

### Negative Consequences

* There is a risk that without forcing users to log in to particular implementations of the contact-frontend forms,
  there will be less information sent to DCST in certain cases. On the other hand, for certain users, the login
  requirement might lock them out of the contact-frontend forms completely, e.g. if they are trying to report a problem
  with login
