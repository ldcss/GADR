# Test Suites

Lumens's out of the box PHPUnit test module does not provide enough functionality to test all aspects of the project, such as database read/write operations. It does provide API unit testing. 

## Considered Alternatives
* Use [Codeception] (https://codeception.com/) testing  framework
* Optional consideration: Full PHPUnit testing framework

## Decision Outcome

* Chosen Alternative: **Use Codeception**
* It is simple to use and a compact one.
* It supports more than one testing suites i.e. Acceptance, Unit and Functional.
* It makes code easy to read, write and debug.


## Pros and Cons of the Alternatives <!-- optional -->

### *[Codeception]*

* `+` Lots of features are available for testing low levels like Unit testing or high levels like API or BDD testing.
* `+` It can be used with other frameworks also for testing.
* `+` It is totally based on PHP, so test cases are also written in that and programmer doesn’t need to learn different languages for that.
* `-` Configuration is not simple and easier.
* `-` It doesn’t have much useful examples, documentation sometimes vague.
* `-` It is totally based on PHP so if the developers don’t know PHP then they can’t write the test cases for the software.


### *[PHPUnit]*

* `+` Confine to every part of the program for unit testing.
* `+` Most widely used across the organization for unit testing.
* `+` Test various types of Controllers without extending.
* `-` It cannot run directly with a web browser.
* `-` It is less Functional, more Unit.
 
