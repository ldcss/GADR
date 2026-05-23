# [Convention-based Logging Classes]

* Status: accepted
* Deciders: @roleyfoley @ml019 @kshychko @ken9ross @rossmurr4y
* Date: 2021-04-13

Technical Story:
In accepted [ADR-0004](./0004-provide-error-codes-on-handled-exception.md), the need for error codes was outlined. The agreed on solution was to implement logging classes to group together log messages (of which Errors are one). 

In its [implementation log](https://github.com/hamlet-io/architectural-decision-log/issues/7) the first step was to identify what classes should be implemented and how they should be structured. Subsequent discussion mapped out the classes and structure required, which will are now accepted and documented separately in this ADR.

## Context and Problem Statement

Hamlet Deploy as a product is made up from several "components". They are not written in the same coding/scripting language and so their outputs - particularly when it comes to log behaviour and error messages - are quite different from each other. When an error or debug message is received, how can the end-user and the Hamlet Deploy developer both gain greater insight from the message that is received?

## Decision Drivers <!-- optional -->

* A solution to this issue must be possible in Bash, Python and Freemarker (Java)
* It must be simple to maintain

## Considered Options

* Use logging codes that follow a numerical convention
* Use an inheritance-based class approach

Separate to the logging code structure, the discussions identified two options as to _where_ log code definitions should be stored:

* Create a centralised definition
* Assign a range to each Hamlet Framework Component and have each one manage the definitions independantly

### Use Logging Codes Followig a Numerical Convention

A numerical system could be defined where each digit in a given code indicates the message severity (i.e debug, trace, fatal, info etc.) and the Hamlet Deploy Framework Component message origin. Additional digits would then be used to indicate the precise nature of that error.

A 4-digit system should provide sufficient coverage.

> *XXX = Severity
> X*XX = Hamlet Framework Component
> XX** = Unique log code

For the first digit, existing log message severities would be used. Some digits are currently listed as "spare" severity levels which should simmilarly be spares under this system.

For the second digit, the Hamlet Framework Components would be assigned as follows:

> Generic/Unaccounted For Error - 0
> Freemarker Wrapper (Java) - 1
> Engine - 2
> Engine Plugins - 3
> Executor - bash - 4
> Executor - python - 5

### Use an Inheritance-based Class Approach

Design a layered log message system where a log message inherits its severity and origin from parent classes, which themselves contribute greater detail to the message.

> Severity
>   Origin
>     Message

### Centralised Code Definitions

Assuming the selection of the numerical convention-based approach, a central definition of the codes is developed. Each Hamlet Framework Component would then be updated with a mechanism to interpret and use them.

### Per-Component Code Range

Assuming the selection of the numerical convention-based approach, digits 3 & 4 would then provide each Framework Component a range of 99 possible unique log messages.

Each Component would create a "dictionary" of this range and their associated log messages. When a new message is written, either an existing digit is used again (assuming matching cause of the log message) or the next unallocated number in the 00-99 range is added to the dictionary.

Each Component would then simply append the 2-digit-code to the message's severity & it's own assigned Framework Component digit to form the logging code.

## Decision Outcome

Chosen option:  _"Use Logging Codes Following a Numerical Convention"_ with _"Per-Component Code Range"_

It was deemed easier to implement and there seemed little benefit and greater complexity to implementing an inheritance-based approach. 

A code range allows each component to implement the definitions in the way that most makes sense to it.

## Pros and Cons of the Options

### Use Logging Codes Following a Numerical Convention

* Good, because its easy to maintain
* Good, because each Hamlet Framework Component has easily understood log message boundaries
* Good, because a good deal of information can be determined from an log message code on its own
* Good, because it standardises the approach to log messages across Hamlet Deploy
* Bad, because there are no rules around how and when an existing code should be reused and when a new one assigned

### Use an Inheritance-based Class Approach

* Good, because inheritance will enable the greatest re-use of log codes
* Good, because a log message can contain varying scopes of detail - ie. a known limitation of the Engine for instance could be inherited by a child, and a subsequent error will not only indicate the cause but provide background on that limitation
* Bad, because it's greater work for each of the Hamlet Framework Components to implement up-front (a greater deal of the work is front-loaded)

### Centralised Code Definitions

* Good, because there is a single place to maintain
* Good, because this is easily understood by users or new developers
* Bad, because the individual mechanisms for interpreting the definitions provide an unnecessary point of failure in Hamlet Deploy
* Bad, because these mechanisms will require more overhead than alternative
* Bad, because it has a higher upfront development cost to alternative

### Per-Component Code Range

* Good, because each Component is entirely responsible for how it defines and maintains the definitions
* Good, because this allows each Component to implement an minimal-effort approach
* Good, because the maintenance overhead should be considerably lower than alternative
* Good, because the range is a clear boundary for the Component, preventing overlap with other Components
* Good, because choosing to implement an additional digit at a later time should require little effort, and may only be necessary in some of the Framework Components
* Bad, because it's likely that some Framework Components will require a greater range than others
