# Simple Composition Components

Technical Story: 
- Depends on: 
  - [Generic Component Requirements](https://mico-docs.readthedocs.io/en/latest/adr/0025-generic-component.html)
- Related issues: 
  - [717](https://github.com/UST-MICO/mico/issues/717)
  - [718](https://github.com/UST-MICO/mico/issues/718)

## Context and Problem Statement
A Simple Composition Component is a [Generic Component](https://github.com/UST-MICO/mico/issues/724), that follows the concept of a certain [Enterprise Integration Pattern](https://www.enterpriseintegrationpatterns.com) by invoking a user-defined (or predefined) openFaaS function and acting upon its results. In contrast to the [Complex Integration Components](https://github.com/UST-MICO/docs/blob/master/adr/0025-implementation-of-complex-eai-patterns-with-faas.md) there are no further efforts (such as maintaining a state) needed for implementing the corresponding Simple Composition Component. 


## Decision Drivers
We want to have a list of all Enterprise Integration Patterns, that can be implemented as Simple Composition Components with a reasonable amount of effort.

## Considered Options
Theoretically, all Enterprise Integration Pattern could be implemented as Simple Composition Components

## Decision Outcome

Which of those do we want to implement??

### Routing Patterns

The following tables describes for all Routing, Transformation and Management patterns, if they can be implemented as Simple Composition Components (As defined above). 

The following assumptions are made:
- We have two Generic Components:
  - A Generic Transformation Component: Provide each message to a user-defined function and forward the result to a predefined target topic
  - A Generic Routing Component: Provides each message to a user-defined function and forward the result to the topic, that is returned by the user-defined function.
- Both components read from a single topic only
- There are no external resources available (e.g. for storing a state)

| Name                       | Implementation Strategy                                                                                                              | Return Value                                                                |         Possible as <br/>Simple Composition Component         |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|:--------------------------------------------------------:|
| Content-Based router       | All rules are implemented in the user-defined function                                                                               | The topic, to which it is routed                                            | Yes                                                      |
| Message Filter             | All rules are implemented in the user-defined function                                                                               | Either nothing, or the topic to which it is routed                          | Yes                                                      |
| Dynamic Router             | All rules are implemented in the user-defined function                                                                               | The topic, to which it is routed                                            | No                                                       |
| Recipient List             | The recipients are hard coded in the user-defined function | All topics, to which the message shall be forwarded                         | Yes                                                       |
| Splitter                   | The splitting rules are implemented in the user-defined function                                                                     | The sub messages, that contain the splitted <br/>content of the original message | Yes                                                      |
| Aggregator                 | Would require that the user provides a message storage, <br/>in which the messages can be stored until they are aggregated                                   | The aggregated message                                                      | No                                                       |
| Resequencer                | Would require that the user provides a message storage, <br/>in which the messages can be stored until they are forwarded in the right order                 | The (correct) sequence of messages                                          | No                                                       |
| Composed Message <br/>Processor | Could be implemented by combining a Splitter, Router and Aggregator                                                                    | The composed message                                                        | No (since the aggregator <br/>is not considered to be simple) |
| Scatter-Gather             | Could be implemented by combining an aggregator, multiple <br/>transformers and a topic, to which all transformers subscribe                | the transformed and aggregated message                                      | No (since the aggregator <br/>is not considered to be simple) |
| Routing Slip               | Probably too complex <br/>for Simple Composition Component                                                                                      | -                                                                           | No                                                       |
| Process Manager            | Probably too complex <br/>for Simple Composition Component                                                                                      | -                                                                           | No                                                       |
| Message Broker             | Probably too complex <br/>for Simple Composition Component                                                                                      | -                                                                           | No                                                       |


### Transformation Patterns

| Name                 | Implementation Strategy                                                                                                                                                                        | Return Value                     | Possible as Simple <br/>Composition Component |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------|------------------------------------------|
| Content Enricher     | The user-defined function contains all the information, that may eventually be added to a message  | The transformed message          | Yes                                       |
| Content Filter       | The user-defined function implements the whole process of filtering <br/>out content of a message                                                                                                   | The filtered message             | Yes                                      |
| Envelope Wrapper     | A Content Enricher for wrapping a message in an envelope. A <br/>Content Filter for unwrapping                                                                                                      | -                                | Yes                                      |
| Claim Check          | Combination of a special Content Filter for replacing message data <br/>with a 'claim', and a Content Enricher <br/>for recovering the data. Also a data storage for storing the data until it is recovered  | -                                | No                                       |
| Normalizer           | A combination of a Router, and a set of Translators                                                                                                                                            | The transformed message          | Yes                                      |
| Canonical Data Model | The user-defined function is implemented in such a way, that <br/>receives/returns messages with a canoncial data format                                                                            | Message in canonical data format | Yes                                      |

### System Management

| Name            | Implementation Strategy                                                                      | Return Value                                | Possible as Simple Composition Component |
|-----------------|----------------------------------------------------------------------------------------------|---------------------------------------------|:----------------------------------------:|
| Control Bus     | It would be necessary to receive from more than one topic                                    | -                                           | No                                       |
| Detour          | Would require a control bus                                                                  | -                                           | No                                       |
| Wire Tap        | Special case of Recipient List                                                               | The topic to which the message is forwarded | Yes                                      |
| Message History | Every user-defined function adds a reference of itself to the message history of a function  | The modified message                        | Yes                                      |
| Message Store   | Would require, that a data storage is available                                              | -                                           | NO                                      |
| Smart Proxy     | Would require a data storage for storing the return address                                  | -                                           | No                                       |
| Test Message    | Would require, that the Test Data Verifier receives from two topics                          | -                                           | No                                       |
| Channel Purger  | This would be a feature, that is implemented in the Generic Component. It is not planned yet | -                                           | No                                       |
