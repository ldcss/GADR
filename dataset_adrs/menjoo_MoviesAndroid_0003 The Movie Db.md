# What service should the app consume?

* Deciders: Menno Morsink
* Date: 2018-04-10

## Context and Problem Statement

This app shows how i would build an Android app. Therefore the app architecture is the goal itself,
the features this app has, are just a way to show an app architecture. 

## Decision Drivers

* Availability
* Realism
* Content creation

## Considered Options

* Fake data layer
* The Movie Db

## Decision Outcome

Chosen option: "The Movie Db", because it is more realistic when the app consumes a real service.

Positive Consequences: 
* It is realistic

Negative consequences:
* When it's down the app cannot consume it 

## Pros and Cons of the Options

### Fake data layer

* Good, because always available
* Bad, because No network code needed
* Bad, because Content has to be created
* Bad, because Not realistic

### The Movie Db

* Good, because realistic
* Good, because not having to create content
* Bad, because might not always be available. Caching data offline could help here, but would not 
help in an initial run 

## Links

* [TheMovieDb](https://www.themoviedb.org/documentation/api)
