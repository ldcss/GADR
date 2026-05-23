# Remove dependency on external DeskPro from contact-hmrcdeskpro-performance-tests

* Status: accepted
* Date: 2020-11-16

Technical Story: PLATUI-818

## Context and Problem Statement

The performance tests for `contact-frontend` and `hmrc-deskpro` live in the repository 
[contact-hmrcdeskpro-performance-tests](https://github.com/hmrc/contact-hmrcdeskpro-performance-tests). As part of the performance test journey, they were previously making calls that didn't reflect a real user journey:
1. Making a call to the endpoint `/ticket/$id` in `hmrc-deskpro` to get the IDs for the ticket in MongoDB and external Deskpro
2. Failing the test if there was no ID yet available from external Deskpro for the ticket

The problems with this are:
1. The calls to POST ticket data to external Deskpro happens asynchronously as a scheduled job, with queueing in place to handle high load. In the real world, it is not coupled the an end user's journey, so this test is not representative of a real user journey.
2. The Staging instance of external DeskPro ends up tightly coupled to our performance tests, and our performance tests fail if external DeskPro is not.
as performant as `contact-frontend` and `hrmc-deskpro`. We should not be performance testing external services, especially as we have queueing in place to manage load.

In short, by coupling in this way to external DeskPro:
* we test a service that we don't own
* we don't reflect the user journey
* we put unnecessary load on the system by calling `/ticket/$id`.

## Decision Drivers <!-- optional -->

* Upcoming SA peak 2021 requires load testing to 700,000 tickets created from1 to 31 Jnuary inclusive

## Considered Options

* Talk with DDCOps about increasing performance of Staging DeskPro
* Remove calls to external DeskPro from the tests

## Decision Outcome

Chosen option: "Remove calls to external DeskPro from the tests", because our tests should be testing the
services that we own, not external DeskPro which is owned by DDCOps. Additionally, we have queueing backed by MongoDB in place within `hmrc-deskpro` precisely so that if there is high load on `contact-frontend` and `hmrc-deskpro`, this can handle the throttling of tickets POSTed to external DeskPro. 

### Positive Consequences <!-- optional -->

* The performance tests are an accurate representation of the user journey
* We as PlatUI are only testing the services that we own

### Negative Consequences <!-- optional -->

* Team DDC Ops no longer get performance testing of their DeskPro instances as part of the 
PlatUI performance tests. However, a separate repo can be created to performance test 
external DeskPro.
