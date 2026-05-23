# Architecture for background jobs

Part of Technical Story: [https://github.com/UST-MICO/mico/issues/95]

## Context and Problem Statement

Several operations (crawl repo, deploy services, ...) are required to run in the background. Therefore, a background job architecture is required being able to launch arbitrary jobs in the background.

## Decision Drivers

* MUST be implemented in Java
* MUST offer a callback functionality

## Considered Options

* Java ExecutorService
* Java CompletableFuture
* Spring Scheduling

## Decision Outcome

Chosen option: Java CompletableFuture, because of the possibility to chain multiple actions and the option to attach callbacks on completion of a background task. 

### Positive Consequences

* Possibility to chain together multiple actions after a succesful execution of a background task. 
* Use of FixedThreadPool, i.e., a pool of threads with a predefined number of threads which are reused. If all threads are active at a time and additional tasks are submitted, they will wait in a queue.  

### Negative Consequences

* With the use of a FixedThreadPool, a background task may be delayed if all threads are active at the time of submission.This may produces time of waiting in the frontend of MICO.

## Pros and Cons of the Options

### Java ExecutorService

* Good, because it offers a simple interface.
* Good, because it enables basic functionality for async background task execution and scheduling.

### Java CompletableFuture

* Good, because of possibility to chain multiple actions.   
* Good, because built-in Java feature. 
* Good, because callbacks can be attached to be executed on completion.

### Spring Scheduling

* Good, because of easy implementation as a result of existing spring injections implemented in the application.
* Good, because well suited for monitoring and management (providing several useful attributes).
* Bad, because of no known possibility to receive a feedback of an async executed action.

## Links

* [Java ExecutorService](https://docs.oracle.com/javase/7/docs/api/java/util/concurrent/ExecutorService.html)
* [Java CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)
* [Spring Scheduling](https://docs.spring.io/spring/docs/current/spring-framework-reference/integration.html#scheduling)