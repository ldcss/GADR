# 4. Use local data for Redbridge and North Cumbria CCGs

Date: 2018-08-21

## Status

Accepted

## Context

North Cumbria CCG and Redbridge CCG do not have an ODS code. As a consequence it is not possible to relate them to the IAPT services. When a GP is serving under either of these CCGs we can display the information for the CCG.

## Decision

Rather than display no result we know the contact information for each of these CCGs. We have decided to store this information locally and display it for the user.
This is only a temporary measure and the change will be reverted once the data has been loaded into the central system.

## Consequences

The data stored locally is not administered centrally, as all other data is. This change is only temporary and will be reverted once the data has been added into the central systems.
