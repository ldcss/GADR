#Work flow of development

## Issue
We would like to decide on a work flow for developing and creating new features. 

## Decision 

- We will follow trunk based development
- Implement non backwards compatible features under feature toggles
- If the build is broken, there should not be more commits pushed to master branch until fixed