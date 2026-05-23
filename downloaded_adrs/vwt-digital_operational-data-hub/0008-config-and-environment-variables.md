# 8. Config and environment variables

Date: 2021-03-15

## Status

Accepted

## Context

We feel the need to create guidelines for the use of config variables and environment variables when using cloudbuild.

## Decision

**In Short**

The code that is going to be executed by the Cloud Function (aka the project that is deployed) should receive its configuration variables from a config file. 

The cloudbuild steps use environment variables which can be stored in the cloudbuild.yaml or an external file.

**Elaboration**

When developing a Cloud Function, you should store the variables in a config file. The variables are easy to read and use, and other developers (and you) don’t need to build anything for the project to run (unless something other than variables need a build).

This moves over to when a project is deployed: The variables used in the code of the Cloud Function are all stored within the project: A config file. The project should not receive variables from a cloudbuild, but from a file that is merged into the project by the build (or the other way around).

When building something, you might need variables that you are only going to use for building/deployment. Or you might use an external project that needs to get some variables. These variables should be given as environment variables or CLI flags. These variables could be stored in a file that is placed inside a repository for easy access, but can be put into the build as environment files.

**Examples**

Configuration stored in a repository and merged into the project environment (or the other way around), like this example:

`config.py`
```python
INDEX = 0
TOKEN = 'AAAAaaaaBBBBbbbb'
```
`__main__.py`
```python
from config import INDEX, TOKEN
```

<br>

Configuration as an environment variable used to build in a specific step, like this example:
```yaml
substitutions:
  _VENV: '/venv'
  - name: 'cloud'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        source ${_VENV}/bin/activate
```