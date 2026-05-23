# 2. Manage data in the Armadillo suite

Date: 2020-06-03

## Status

Accepted

## Context

In this project we manage the data in the Armadillo suite. 

## Decision

We will use the MolgenisArmadillo client to manage data in the Armadillo suite. This means managing folders and files in the data backend based on R-data.

## Consequences
Managing data using the client entitles the following consequenses
- You can perform CRUD operations on files, folders and subfolders in the Armadillo data backend
- You can login and logout in the Armadillo service
- You are allowed to copy data from one folder to the other
- You are allowed only to upload RData in folders in Armadillo data backend
- You are allowed to upload files up to 500mb
- The client does not check the RData files that uploaded to the Armadillo data backend
