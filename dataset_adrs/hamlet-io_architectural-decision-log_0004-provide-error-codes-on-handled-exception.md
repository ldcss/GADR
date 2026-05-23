# [Provide Users an Error Code on Fatal Error]

* Status: accepted
* Deciders: rossmurr4y, roleyfoley, ml019
* Date: 2021-03-02
* Implementation Log: https://github.com/hamlet-io/architectural-decision-log/issues/7

## Context and Problem Statement

Hamlet Deploy is not a compiled binary file nor is it written in a single programming or scripting language. It is a combination of all of the above; 
 * Java for the Freemarker wrapper, 
 * Freemarker has its own DSL, 
 * the original Hamlet Deploy Executor is presently primarily Bash scripts and 
 * the "Click" CLI Executor is written in Python. 
 
When a handled exception occurs, there is no consistency in the error information provided. A handled error in Freemarker is likely to provide a large JSON object for review, whilst an error in the Bash Executor will provide a brief summary of the problem. Because these summaries are not always unique-per-error, many provide only a generic error message. 


## Considered Options

* create a manually-maintained library of error codes & assign one to each handled error
* introduce logging classes, that group together messages of a simmilar kind

## Decision Outcome

Chosen option: introduce logging classes, that group together messages of a simmilar kind. Later we will re-evaluate to determine if a more specific approach to error handling (such as individual error codes outlined above) would remain useful / necessary and if so can build upon this framework.


### Manually-maintained library of error codes

* Good - will provide a method for providing tailored error messages and possible fixes to the user
* Good - could be extended to provide an avenue for review of the most-encountered error messages
* Good - improved reporting / communication around errors experienced
* Good - consistency across the spectrum of potential error sources
* Bad - increase in maintenance overhead
* Bad - may be a challenge to enforce consistently
* Bad - difficult to make extensible by community content


### Logging classes

* Good - provide a method for tailoring messages, whilst allowing for re-usability
* Good - accessible to community content
* Good - consistency across the spectrum of potential error sources
* Good - framework could be extended / upgraded at a later time
* Good - minor maintenance overhead once established
* Bad - less specificity is possible when compared to unique error messages

