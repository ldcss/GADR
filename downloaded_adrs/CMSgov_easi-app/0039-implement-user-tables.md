# User Table implementation and Rollout Plan

**User Story:** [EASI-3341](https://jiraent.cms.gov/browse/EASI-3341)

As we look forward to future feature improvements for the EASi application, there is a need to implement User Tables. These tables will allow for per user configuration, as well as more simply storing information about each user.

As this is an existing application we need to have a mechanism in place to migrate existing data that is only a username (EUAID) to reference an entity in the user table. There are also spots in the data where a user is referenced only by name, and not by username.

To implement this, we need to be able to 
1. Get information about users
2. Store that information in the User Table
3. Migrate existing data to use the new account reference

Database migrations only happen in the DB context, so we can't query an external API when they are being run. As such, we need to come up with an approach that can update the user information at another time.

## Initial Account Implementation

### Considered Alternatives

* Write a helper script or program that inserts user account records for all places in the DB that reference an EUAID
* Insert place holder records
* A combination of approaches. Using an auxiliary script, and rely on temp records for any unforeseen edge cases


### Decision Outcome

* A combination of approaches. Using an auxiliary script, and rely on temp records for any unforeseen edge cases

An auxiliary script serves our current need the best. It will ensure that most users are have a record already in place before we attempt a migration. As a result, the migration should be smooth. 

For cases where we cannot create a user account for an existing record, we can add placeholder account information. That will allow us to create a reference to the user table for an EUAID, and handle this edge case where user information is missing. As a first pass, we will handle migrating to the user account table for EUAIDs first, and later approach the places that a full name is referenced. 

### Pros and Cons of the Alternatives <!-- optional -->

#### Insert place holder records

* `+` This can be done during the migration
* `+` This doesn't rely on external data source
* `-` Extra complexity incurred when querying user accounts (how can we be sure the data is up to date?)

#### Write a helper script or program that inserts user account records for all places in the DB that reference an EUAID

* `+` Data is accurate
* `+` Edge cases can be handled easily
* `-` Relies on data to stay in an up to date state
* `-` Extra complexity incurred by creating a separate app / script

#### A combination of approaches. Using an auxiliary script, and rely on temp records for any unforeseen edge cases

* `+` We have a higher level of confidence in the data than either other approach
* `+` Data should be up to date
* `+` Any data that is not able to be updated by the script can use the temporary data
* `-` We incur the complexity of both approaches

## Implementation Plan

### Context

EUAIDs and full names of users are present throughout the application. As such, we need to consider a phased approach to implement this.
Special attention should be given to places in the app that reference a user different than the currently logged in user. The currently logged in user is the simplest user to reference, as they automatically can have an account reference added in the database. When another user is referenced, they don't automatically have a user account created. 

### Plan

With the above decision, we should first implement user accounts, and create accounts for all historical references.

We should implement user account references for all the places that a user besides the currently logged in user account is referenced. By doing so, we will ensure that we have a user account referenced in the database for all referenced users. This should give us confidence that every user referenced in the application has a user account.

It would be ideal to create a reference of the user that is being added and replace the reference with a foreign key to the user table. A first pass alternative would be to create an account for every referenced user. We could then take more time to switch out the logic to reference a user.

As noted previously, we will handle the simpler cases of EUAIDs first, and later approach places that a users full name is referenced.

#### Areas that add Users
1. System Intake
    a. Requester
    b. Business Owner
    c. product manager
    d. ISSO
    e. TRB Collaborator
    f. OIT Security Collaborator
    g. EA Collaborator
    h. Contractor
    i. Admin Lead

2. Business Cases
    a. Requester (Should be the same as system intake)
    b. Business Owner (Should be the same as system intake)

## Proofs of Concepts

To validate these hypothesis, a few branches were created to test some of this initial implementation.

### [Account Creator Test Branch `(EASI-3341/user_account_spike_poc_user_table_filler)`](https://github.com/cms-enterprise/easi-app/tree/EASI-3341/user_account_spike_poc_user_table_filler)

This branch makes a small utility program. It queries the database for both usernames and user ids, and then it attempts to find information on that user in OKTA. If successful, it creates an account reference for the user in the database. The script can be invoked by running `go run ./cmd/populate_user_table/*.go` . Select the options you want to run by pressing space, and press enter to execute the commands.



### [Account Table and TRB Migration `(EASI-3341/user_account_spike_poc)`](https://github.com/cms-enterprise/easi-app/tree/EASI-3341/user_account_spike_poc)

This branch ports the user table functionality from MINT. These features include
1. New Data loaders
2. A User Account Table
3. A New implementation of Base Struct
4. Generic functionality to get an account by an ID ( see TRB Request `createdByUserAccount` field)

There is also a migration to migrate the TRB request table to use the user account table. More work will need to be done to finish migrating the data properly, but this shows feasibility


### Access Check
From previous work in MINT, access control should be fairly simple to implement. Previously, this was handled by the [access control](https://github.com/CMSgov/mint-app/blob/bfc54d4de177a4d836028e5356bdb24d30eab490/pkg/accesscontrol/access_control.go#L17C1-L77C2) package, simply checking if the user was a collaborator.  This should be straightforward to implement in EASI if it is needed.
