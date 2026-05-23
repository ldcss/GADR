# Decouple game from web server

## Context and Problem Statement

I want to create a multiplayer web game.
What structure this project should have?

## Decision Drivers

* Software architecture is important
* Clear separation of concerns
* Testable code

## Considered Options

* Stand-alone OTP application for game business logic
* Single OTP application for web server and game

## Decision Outcome

Chosen option: "Stand-alone OTP application for game business logic", because

* Good for business domain isolation
* Ignoring web concerns at the beginning helps thinking about game API
* Possible different clients (command line, web) makes complex interaction tests easier
* Different releases: bundled together with the server or one game application for many servers
