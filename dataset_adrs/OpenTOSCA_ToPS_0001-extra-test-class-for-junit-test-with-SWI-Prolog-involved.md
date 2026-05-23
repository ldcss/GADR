# Extra Test Class For Junit Test With SWI Prolog Involved to Enable CircleCI grandle test with the Rest of The Test Classes

* Status: accepted
* Deciders: Karoline Saatkamp, Oliver Kopp
* Date: 2018-03-29

Technical Story: Test methods which test classes that use the jpl lib of SWI Prolog throwing errors when running CircleCI because
SWI Prolog must be installed on the system to run the Prolog queries.

## Context and Problem Statement

Tests including Prolog queries with SWI Prolog can not be executed with CircleCI because SWI Prolog is not 
running at the executing system.

## Considered Options

* Add an extra test class which encompasses all tests that involves SWI Prolog calls.
* Create a docker image and run SWI Prolog at CircleCI

## Decision Outcome

Chosen option: extra test class to reduce the effort and to still enable testing SWI Prolog locally. For this the extra class is
annotated with @Ignore. All other tests run with CircleCI. These tests includes the core functionalities of the developed tool.
