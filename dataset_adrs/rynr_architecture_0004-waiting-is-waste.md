# 4. Waiting is waste

Date: 2018-05-18

## Status

Accepted

## Context

Having a developer waiting for any process to finish is a stupid thing. It's not only that it's to long for the developer to wait, it also hinders you from fixing issues fast.

## Decision

Any processes and workflows need to be very fast and fully automated.

## Consequences

Any process happening with the code needs to be automated. The power of the machine should be used as much as possible. Testing should be able to utilize multiple cores on a computer.  
This also means that building complex applications is an enemy of lean fast builds. Having seperated parts that can be build, tested and deployed fast is a good way.  
All the process should also be documented (see also [#3](./0003-have-the-master-documentation-in-the-readme.md)) and as easy that anybody can run them. It should be possible for everybody to build and deploy a release.
