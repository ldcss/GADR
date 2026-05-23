# Implementation of complex EAI-Patterns with FaaS


## Context and Problem Statement

Some [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com) have a complex structure where parts of the behaviour can be implemented generically while some parts need to be modifiable by the end user (in our case the system admin using MICO).
We have already [decided to use a FaaS platform](0023-faas.md) to provide this modifiability in form of code as configuration.
While this works well for most patterns, for some of the more complex patterns it is not easy to allow modifiability via FaaS.
This is especially the case if the user want to write as little code as possible meaning the [generic part](0025-generic-component.md) of the component has to be implemented by the MICO team.


## Decision Drivers

* Modifiability of the patterns must be provided via a FaaS function
* The function should only have to contain as little code as possible
* Generic code for the pattern should be provided by the MICO platform either as a library to import into the FaaS function or in the component that calls said function


## Challenges

### Where / how to implement generic logic

* Implement all logic in the FaaS function
* Implement custom logic + some of the generic logic in the FaaS function
* Implement only custom logic in the FaaS function

### State of configuration channel

How can the FaaS function get the current state of the configuration (e.g. dynamic router).

* Let the FaaS function subscribe to Kafka
* Have a separate DB
* Send the current configuration together with the message

### Sending to multiple destinations / unknown destinations

A router does not have a specific endpoint to send all messages to and may even send messages to many endpoints.

* Implement generic routing with `recipientList` / `routingSlip` only and let FaaS function write the route into the message header
* Let the function send the messages directly to Kafka

### Stateful components

Some patterns are inherently stateful.

* Store state in a DB
* Store state in generic component and send to FaaS function with message

### Performing intermediate request steps

A content enricher needs to perform requests to get the content to inject into the message.

* Offload implementation completely to the user
* Split into two parts, one determining which requests are needed and one injecting the requested content into the message.


## Affected patterns

```eval_rst
======================= ================ ============== ==========
 Pattern                 dynamic config   destinations   stateful
======================= ================ ============== ==========
Router                  no               yes            maybe
Dynamic Router          yes              yes            maybe
Content based Router    maybe            yes            maybe
Aggregator              no               no             yes
Resequencer             no               no             yes
Process Manager         maybe            yes            maybe
Message Normalizer      maybe            no             no
======================= ================ ============== ==========
```

## Decision Outcome

**Where to implement logic**: To be decided

**State of configuration channels**: To be decided

**Stateful functions**: To be decided

**Routing**: We will support custom routing decisions in the FaaS function by always interpreting a routing slip if it is present.
The routing slip has to support multiple destinations for one routing step.
This will also allow us to make more patterns possible (everything that is not stateful) with a single generic kafka to FaaS connector.

**Intermediate requests**: To be decided


## Evaluation of Options

### Where to implement generic logic

#### Implement generic logic in FaaS-Function

* Good because we can use Kafka as trigger for the function
* Good because it allows easy extension and modification of the generic logic where needed
* Bad because we need to implement the generic logic in all supported languages as a library/framework
* Bad because the alternative would mean complex FaaS networks/dependencies if generic logic is capsuled in FaaS functions

#### Implementing generic logic in Kafka to FaaS Adapter

* Good because we only need one implementation in one language
* Bad because generic logic needs to support all patterns => possibly more complex implementation

### Stateful patterns

#### Store state in compacted Kafka topic

* Good because it uses no extra component
* Bad because only useful for storing configuration channel state/state that does not change too often
* Bad because it needs many assumptions
* Bad because whole channel needs to be read to load state

#### Store state in DB

* Good because DBs are really good for storing and querying state
* Bad because management of DBs (isolation of DBs for different FaaS functions) is difficult

#### Send state with the message to the FaaS function

* Good because FaaS function can be trivially stateless
* Bad because state could be large
* Bad because generic component needs to know what state to send (up priori assumption)

### Sending to multiple or unknown destinations

#### Allow FaaS function to send messages directly to kafka

* Good because it allows complex routing patterns
* Bad because FaaS function needs to understand and react to various header fields in the cloud event (routingSlip, route history)

#### Implement generic routing via header fields (routingSlip/recipientList)

* Good because we can ensure semantics of some header fields in our implementation
* Bad because header fields need to be sufficiently complex to support complex routing decisions

### Intermediate requests

#### Offload complete implementation to user

* Good because all requests can be controlled by user code
* Bad because user may need to (re-)implement generic code
* Bad because FaaS function needs to know about kafka topics

#### Split into request part and merge part

* Good because split implementation is easyer to understand
* Good because split implementation allows for generic request handling implemented by MICO
* Bad because split pattern implementation is  more complex
