# Provide a Testing Environment for Non-Engineers

**User Story:** *317* <!-- optional -->

Because of the way job codes are configured, testing new features is
becoming difficult. We've also run into situations where we had to
track down users with specific job codes selected in order to test
certain functionality. We need a better way!

For the scope of this ADR, we are going to focus on the ability to test
features, regardless of whether that testing happens before or after a
merge to our main branch. Gating code merges is out of scope for now.

## Considered Alternatives

* *Use Launch Darkly to Selectively Downgrade Permissions*
* *Do Testing Locally*
* *Obtain Role-Based Accounts*
* *Repurpose Deployed Dev Environment for Testing*

## Decision Outcome

* Chosen Alternative: *Use Launch Darkly to Selectively Downgrade Permissions*
* No infra work, and little application engineering work required
* Will work the same across all environments
* Allows us to retain our deployed test environment (called Dev)

## Pros and Cons of the Alternatives

### *Use Launch Darkly to Selectively Downgrade Permissions*

We can use per-user targeting to selectively "turn off" specific job codes,
without having to make any changes in EUA. This permission targeting would
always be a downgrade system, not an upgrade system, so folks should never
be able to gain access to features they shouldn't be able to see.

* `+` Works across all of our deployed environments, including prod, which
     could be helpful for debugging
* `+` Minimal work on the dev side to change user role checks to include a
     Launch Darkly check as well
* `+` No infra work needed
* `-` Non-engineers will need to get comfortable using the Launch Darkly console
* `-` We might need to increase  our license to include more Launch Darkly logins

### *Do Testing Locally*

Similar to  our our engineers do their work, we could have non-engineers set up
a working local environment for their testing

* `+` Allows for use of dev auth
* `+` Can easily switch between branches
* `+` Doesn't require EUA accounts since code is all open source
* `-` Requires all non-engineers to have a working dev environment
* `-` Requires all non-engineers to become somewhat fluent in git, which is usually
     easy until it's not

### *Obtain Role-Based Accounts*

This solution involves getting new accounts to use with Okta that have the
specific job codes we need. Think something like governance-admin@truss.works
and testing-admin@truss.works. We would store passwords and multi-factor auth
in 1Password.

* `+` Anybody with access to our 1Password vault can log into EASi and view the app
* `+` No code changes required
* `-` Likelihood of getting these accounts set up with EUA is slim
* `-` Not sure our test accounts with Okta can have job codes associated with them

### *Repurpose Deployed Dev Environment for Testing*

Our current infrastructure includes a "Dev" environment, which is a deployed
environment we can use to deploy code before it is merged into our main code
branch. We could repurpose this environment to match our main code branch and
turn on our "dev auth" (instead of Okta), which can spoof job codes.

* `+` Environment already exists, so no need to provision a new one
* `+` Can configure Dev to use dev auth, but keep impl a production-like environment
* `+` Easy for non-engineers to access without local code management
* `-` Removes our testing environment used before we merge
* `-` Requires infra work to change our CI pipeline
