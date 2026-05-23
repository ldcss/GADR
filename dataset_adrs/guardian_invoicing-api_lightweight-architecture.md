# Lightweight Architecture 

## Status

Proposed

## Summary

Keywords: lightweight, iterative improvements, inlined implementations, testing in production  

* Small Scala AWS Lambda package size of less than 10 MB
* Prefer direct inlined business logic over abstracted indirections 
* Use of off-the-shelf AWS infrastructural facilities instead of bespoke implementations
* Testing in production via preconditions-program-postconditions instead of mocked tests
* Prevent silent failures
* Minimal custom abstractions of Zuora 
* Usage of lightweight HTTP and JSON libraries and vanilla Scala

## Context

This design is based on the observations and lessons learned over the years from various approaches taken
to solve problems in AWS/Zuora domain. The core idea is minimalism in tools, abstractions and indirections.

### Small Scala AWS Lambda package size of less than 10 MB

* There is no need for custom lambda libraries. The following vanilla Scala snippet is all that is necessary to 
define Scala lambda

    ```scala
    object Lambda {
      def handleRequest(input: InputStream, output: OutputStream): Unit = {
        // deserialise stream
        // run program
        // serialise to stream
      }
    }
    ```

* There is no need for importing web frameworks/libraries within lambdas as AWS provides necessary facilities 
out-of-the-box such as logging, concurrency, error handling, etc.
* Many custom libraries are not necessary as Scala is a very expressive language which can express the same 
concept using vanilla facilities
* If something can be done with couple of lines of code, there is no need to import whole library just to do that

### Prefer direct inlined business logic over abstracted indirections 

* Generally speaking there is not much algorithmically complicated logic in our business domain. 
* Essentially we need an HTTP client, JSON deserialiser, and some request orchestration code.
* We should be able to inline directly the whole orchestration in a single file, instead of spreading it 
over many files, libraries, and abstractions.
* Advanced features should be used in few places where needed, instead of across the whole system

### Use off-the-shelf infrastructural facilities instead of re-inventing the wheel

* AWS has good documentation, many examples across open source GitHub, and is GDPR compliant. 
* Setting up infrastructure is difficult, but it is largely a one-time affair. After that it rarely changes,
and when we have to then we should be able to look up documentation 
* For example, if our stack is API Gateway + Lambda, there is no need to import web frameworks, implement custom 
routers, etc.

### Testing in production via preconditions-program-postconditions instead of mocked test

* Favour runtime preconditions and postcondition testing in production instead of unit test with mocked HTTP/JSON.
    ```
    input
      .tap  { preconditions }
      .pipe { program } 
      .tap  { postconditions }
    ```  
* Reserve unit tests for complicated business logic algorithms, not plumbing
* Issues such as malformed JSON or wrong HTTP request orchestration are likely to surface quickly after deployment 
(as long as alarming is setup) thus ROI for unit testing these aspects is likely not worth it 
* Runtime preconditions/postconditions is just code alongside main business logic and as such harder to ignore and 
has lower maintenance cost relative to unit tests


### Prevent silent failures

* There have been multiple cases of silent failures introduced by handling errors with techniques that swallow 
errors without error logging or wiring them to non-200 responses. Failing fast on unrecoverable errors hooks into AWS 
out-of-the-box error logging and alarming at minimal cost.
* If there is no automatic error recovery possible and system cannot proceed, why fail slow?
* Automatic error recovery, self-healing, etc., are difficult to achieve ideals, usually not possible in Zuora. 
Due to nature of Zuora outages which are hours long, error handling cannot be meaningfully addressed 
by techniques on a unit level. Instead, they should be addressed on a much higher infrastructural level such as using 
SQS, Step Functions, etc. 
* If error recovery is possible, then it should **not** actually be modelled as an error but simply an alternative path 
the system tries.

### Minimal custom abstractions of Zuora

* Work on whitelisting as opposed to blacklisting principle
  * If system detects a scenario it cannot handle then immediately notify developers to make adjustment
    instead of trying to predict the Zuora model up-front to handle all imaginable scenarios
* Modelling of Zuora has not been very successful over the last five+ years due to the way Guardian uses it with
countless exceptions in the model
* Instead use Zuora directly the way they document it which means essentially on the REST API level.
* Favor preconditions and postconditions to check if we have done the right thing
  * "Does the invoice look correct after production mutation?", as opposed to 
  * "Here is the predicted model capturing all the ways invoice can be generated, and the corresponding (mocked) unit test."
* Zuora is hard enough to understand without developers putting another layer on top of it

### Usage of lightweight HTTP and JSON libraries and vanilla Scala

* Scala is an expressive language, and many concepts can be directly implemented without depending on external libraries
* JSON and HTTP is boring, there is no need for sophisticated libraries, or even worse, 
re-inventing yet another custom implementation
* There is no need for special logging or config libraries. AWS provides this out-of-the-box.
* Most scenarios do not require advanced techniques/libraries. Such techniques should be used only where necessary 
in isolated segments of the codebase.

## Consequences

**Arguments for**

* No silent failures
* Sub-second AWS lambda warm-up
* Lower maintenance cost
* Easier to lookup documentation
* Easier to on-board developers
* Testing on real data instead of mocked data
* Quicker builds
* Forces developers to stop ignoring alarms

**Arguments against**

* Crucially depends on developers responsibly reacting upon receiving alarms

## Decision

Pending

