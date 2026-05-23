# 2. Usage and import of shared library

Date: 2020-11-02

## Status

Recommended

## Context

We need to decide how the shared library should be loaded for usage.

- A library version can be a tag, a branch or a commit SHA.
- A library can be loaded explicitly or implicitly
- A library default version can be configured globally or not

### Loading implicitly
````groovy
pipeline {
  agent any
   
  stages {
    stage {
      steps {
        someMagicallyAvailableLibraryFunction()
      }
    }
  }
}
````
- a default version of the library needs to be defined globally
- there is no need to import the library, as it will be loaded automatically
- you can override the version by importing it manually: `@Library('my-shared-library@my-custom-version') _`

### Loading explicitly
````groovy
@Library('my-shared-library@1.0.0') _
 
pipeline {
  agent any
   
  stages {
    stage {
      steps {
        someMagicallyAvailableLibraryFunction()
      }
    }
  }
}
````
- an import statement is always needed
- a default version could be defined globally, then the version can be left out when importing

### Using a global predefined version
- can be overriden in the pipeline
- does not force users to select a version

### No globel predefined version
- import will not work without version
- consumers are aware of the version that they use
- can be dynamic (auto updating) when using release channels with branches

## Decision

We will use explicit loading without a predefined version and release channels for releasing based on branches.

- reduces the magic of the used version
- can still be auto updating
- consumers know that a library is used and what the version is


## Consequences

The library import and the version needs to be set by every consumer. 