# 3. Addition of Paper Verification Codes to the Codes service

Date: 2025-06-30

## Status

Pending

## Context

Paper Verification codes are required to provide access to modern LPAs for organisations when one or more of the actors on the LPA have opted for a paper based access to the process. 

They are different to the Activation/Actor codes that are currently managed by the service but are close enough in scope and implementation to consider using the service to provide them.

It is important to note that Paper verification codes do not alter the usage of the code service for the creation and lifecycle management of Activation/Actor codes for both Modernise and Sirius LPAs.

## Decision

In order to effectively mark the codes as being for paper based access it has been decided that they will take the form of a 'P' followed by 14 hyphen separated digits. The length of the code is neccessary as codes will be long lived items that only start to age once they have been used. 

> **Example Code**  
> P-PRTB-F62Y-SQ4N-G3

Codes will exist indefinitely until they are first used by an organisation. Once used, a 2 year expiry is applied to the code. Codes are not removed or otherwise deleted from the system as it will be a requirement that they are never reused. Additionally we can inform users that a particular code has been cancelled or expired. 

In brief it is proposed that 3 new endpoints are created at the path `/paper-verification-code`. Namely `/create`, `/mark_used` and `/validate`. 

### /paper-verification-code/create
This is sufficiently different in logic that the creation of a new endpoint makes sense. Although much the same information will be required from Sirius to create the code we will not need to set a TTL or date of birth on the record. When a replacement code is created for an LPA/Actor combination then the existing code should continue to exist and function but it's usable lifetime should be shortend via the `expiry_date` field to allow a reasonable period for creation, delivery and disemination of the new code. 

As with the existing `/create` endpoint it should accept multiple LPA UID/Actor UID pairings in a single call, create all relevant codes and pass back the collection of created codes.


### /paper-verification-code/mark_used
Paper Verification Codes do not age until first used. This endpoint will allow the Use an LPA service to inform that the code has been successfully accessed and that the expiry process should begin. Currently a 2 year expiry is proposed.

### /paper-verification-code/validate
The proposed workflow will mean that the validation call will *only* recieve the code to check. The code service should ensure that the code is marked as active before returning:

  1. The LPA UID (amongst other data) to which the code is attached **or**
  2. A response indicating the code has been cancelled (inactive *and* `status_details` is 'Revoked') **or**
  3. A response indicating the code has been replaced (inactive *and* `status_details` is 'Superseded')

The the case of *3* it is likely we will want to return the generation date of the newest available code. This will allow downstream services to display an approximate date of delivery/usage for organisations to help in their conversations with LPA users.


## Consequences

Although the types of code are distinct in their end usage the two clients of the service (Use an LPA and Sirius) will be using the endpoints in much the same way and with the same access patterns so it makes sense to have the same service handle both types.

By isolating new and distinct functionality to additional endpoints we will be minimising any changes to existing Activation/Actor code code paths.
