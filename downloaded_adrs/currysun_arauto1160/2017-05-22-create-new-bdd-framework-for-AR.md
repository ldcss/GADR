# Create new BDD framework for AgileREPORTER

## Status
Accepted

## Context
- `arauto`, the current GUI testing framework for AR is slow, hard to work and unmaintainable. 
- it was developed in Shanghai 
    - taylor for Shanghai's environment/setup
    - the owner has left the company
    - it uses TestNG instead of JUnit

## Decision
- write a new framework using a simpler, cleaner design 
    - use `Selenide` library to write easier Selenium-based tests  
    - use `Cucumber` library to write BDD tests  
- testers and developers are responsible for maintaining the framework
- changes should go through the same PR process

## Consequences
- easier for developers to start writing tests
- easier to write tests and run them against local env
- easier to maintain
- testers and developers buy-in
- some functionality may be duplicated in the new framework
- some existing tests may need to be ported over time