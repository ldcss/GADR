# 15. Manage short-lived access tokens in tests

Date: 2019-01-16

## Status

Accepted

## Context

We have implemented the VCR gem as part of our testing suite; this gem allows you to "record your test suite's HTTP interactions and replay them during future test runs for fast, deterministic, accurate tests.". The interactions are saved into yaml files (cassettes) as part of the spec/fixtures folder and committed to the repository.

VCR allows you to filter out sensitive information, but this does not cover any data returned in the body.  We get a short-lived access token returned in the body as part of the OAuth flow and need to find a way of ensuring that these are not exposed and used to get access to sensitive data.  Whilst the tests are run against T3, which is an anonymised dataset, we don't want to risk the possibility of someone being able to engineer a way of undoing that and seeing real data.

The main options:

- making the github repository private
- git-crypting the VCR cassettes folder
- adding the VCR cassettes folder to .gitignore
- not using VCR and instead using other ways of mocking external calls in tests

Making the github repository private contradicts our commitment to coding in the open, and eventually opening a previously closed repository is often risky and hard to prioritise.

Encrypting the VCR cassettes folder would effectively mean making a portion of the repository private.  There are three criteria for keeping code closed and they are: not publishing keys and credentials; algorithms related to detecting fraud; and anything around unreleased policy.  This situation does not meet any of these criteria.  Full documentation related to open source code guidance can be found [here](https://www.gov.uk/government/publications/open-source-guidance/when-code-should-be-open-or-closed).

Adding the VCR cassettes folder to gitignore would mean that we could continue to make use of the gem in local development and during the CircleCi workflow.  The APIs that we are using are being actively developed against and it's important that we catch any changes as early as possible. Therefore a developer can re-record all cassettes at the start of a feature to check for changes, and then just reuse them to speed up the tests.  The cassettes then don't get committed to Github and access tokens are not exposed. CircleCi can continue to run the tests as normal and whilst anyone can access the project, cannot see the contents of the cassettes.

Lastly, there is an option to not use the VCR gem at all and use something like WebMock to mock every API call in the test suite. However, if there were any issues with API documentation being out of date we wouldn't necessarily know what to expect in the response.  Also, if we mock the calls there might have been changes we weren't aware of and find out late in to the development process, whereas actually making the calls will cause the tests to fail and let us investigate.

## Decision

We will add the VCR cassettes folder to gitignore.

We will change the VCR config to allow a recording mode to be added i.e. "all" -> re-record all cassettes, "new_episodes" -> append the cassette(s) with any new calls made, "once" -> just record them once and reuse.

## Consequences

We remove the risk of short-lived access tokens being exposed publicly, we can continue to use VCR in local development to keep our test speeds as low as possible, and we will also continue to use VCR during our CI/CD workflow in CircleCi.

In regards to CircleCi it does mean that our CircleCI project environment variables need to include credentials for authenticating against T3.

It's important to note that our tests will be making external network calls, which may increase build times and flakiness. We are likely to need to address these concerns later, but this decision is a pragmatic approach to help us move forward now.
