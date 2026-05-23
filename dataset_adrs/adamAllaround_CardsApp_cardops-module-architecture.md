#Choice of application level architecture for cardops module

##Context
Need to choose an applicable architectural approach to cardops module so that it can be consistently followed and the module can be developed and extended easily.

##Drivers 
* The module contains business rules
* It should be easy to prototype the solution
* Time estimated for completion is 2 months
* The application should be a prototype - not an enterprise class solution
* The database should be quick to set up, best if it's known already
* This domain is treated as a core domain
* We're pootentially looking into changing the business rules around withdrawing, maybe introducing 
new card types

##Decision
This module is best realized with Hexagonal Architecture, aka ports and adapters. Since its the core of 
our domain. This architecture should enable easy prototyping and easy testing.
  
##Consequences
* may be slightly more difficult to understand for newcomers

##Other options
* Standard three layer - harder to test the solution