#Testing Framework

##Context
We need to choose a testing framework for our system. It's best if it's used across all solution so that it's a standard approach.

##Drivers 
* Tests should be readable and quick to write
* Testing framework that is well known is prefered

##When
* The decision is made at the start of the project. 7 june 2020. 
##Status
Done. No other options considred now.

##Decision
We decided to go with Spock, due to its readability and the fact that it's a well known framework. Some groovy langauge tricks enable quick test preparation.  
##Consequences
* We prefered test conciseness over long test methods
* We prefered test-reusability with spock parameters rather than several test methods
* We prefered test readability with text data and given when then blocks
* We prefered built in spock Mocking and interaction based testing over mockito.
* We accepted a little harder setup with Maven

##Other options
* MySql - less flexible, requires installation