# 3. repo directory structure

Date: 2021-02-08

## Status

Accepted

## Context

We feel the need to standardize the directory structure for github repos. 

## Decision

### 1. General rules
* Directory names must always:
    * Always use underscores (“\_”) in names for folders and files to split between words.
    * use lowercase.

### 2. Cloud functions
* The root directory for cloud functions is 'functions/'.
* A '.gcloudignore' file is provided to limit the uploaded files.

### 3. API
* the root directory for the API is 'app/'.
* For OpenApi APIs see the separate ADR for working with OpenApi generated code.

### 4. Frontend
* the root directory for the APP is 'app/'.
* The directory structure below the app directory is based on the recommendations of the framework.
    * For the angular applications the recommendations can be found at [Angular Workspace and project file structure](https://angular.io/guide/file-structure).

### 5. Tests
* Files needed for testing are stored in the 'test' directory.

### 6. SAST
* Files needed for the SAST scan are stored in the 'sast-config' directory. 

## Consequences
