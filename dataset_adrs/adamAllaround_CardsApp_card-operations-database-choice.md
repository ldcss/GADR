#Card Operations Module Database

##Context
We need to choose the database for our CardOperations. The database needs to store data in persistent form but it's not required that data is stored across sessions. 
Application is a prototype, so it should be good for a quick setup. 

##Drivers 
* Operations data needs to be available to customers when application is running
* Operations data does not need to be available for long time or across application restarts.
* Eventual consistency in statement creation is ok
* Time estimated for completion is 2 months
* No paid solutions should be used
* The application should be a prototype - not an enterprise class solution
* The database should be quick to set up, best if it's known already
* We should be able to see the data stored in the DB - some UI is preferred

##When
* The decision is made at the start of the project. 7 june 2020. 
##Status
Done. No other options considred now.

##Decision
We decided to go with H2 database for its ease of use, easy setup and familiarity.  
##Consequences
* Prefered ease of use and quick setup over longer installation.
* Prefered that the solution works on all the environments with software package that is in git , rather than having install third party software. 
* Prefered not worrying about migrations for now as the database will be re-created at startup.
* We accepted that this won't be used when we gou out of prototype phase. 

##Other options
* MySql - less flexible, requires installation