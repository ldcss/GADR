# Function to component mapping

Technical Story: [Issue #713](https://github.com/UST-MICO/mico/issues/713) <!-- optional -->

## Context and Problem Statement

To implement the EAI patterns we use a combination of a generic component
which handles the communication with Kafka and a FaaS solution. The business logic of the EAI patterns (message splitting/aggregation or transformation) is provided via functions which are hosted on the FaaS solution. The generic component communicates with Kafka and de/serializes the messages. We need a means to wire the instances of the generic component with the functions. E.g. A user wants to insert a message splitter between two message-based components. To realize this an instance of the generic component in combination with a splitting FaaS function will be used. The generic component needs the address of the FaaS gateway and the function name (e.g. http://address:8080/function/msg-payload-splitter) to call the function. To provide the necessary information to instances of the generic component we considered the following techniques. 

## Decision Drivers <!-- optional -->

* MUST be supported by the language/technology which is used to implement the generic component
* MUST be easy to integrate into MICO
* SHOULD be a well known and proven solution

## Considered Options

* Environment variables
* Function registry
* Control Topic
* Function composition
* Function proxy
* Configuration file

## Decision Outcome

Chosen option: "Environment variables", because MICO already supports this and it is easy to implement in the generic component.

## Pros and Cons of the Options 

### Environment variables

This option uses environment variables to store the necessary information. These variables are controlled by MICO.

* Good, because MICO already supports setting environment variables
* Good, because most languages support reading environment variables
* Good, because we need environment variables anyway because we need to provide the Kafka configuration
* Good, because it is a well known and proven solution
* Good, because it follows the (twelve-factor app methodology)[https://12factor.net/de/config]
* Bad, because the configuration can not be changed on the fly (do we want this?)

### Function registry

We implement a separate component which stores the mapping of the functions to the instances of the generic component. We could evaluate if (Apache ZooKeeper)[https://zookeeper.apache.org] or (etcd)[https://github.com/etcd-io/etcd] fits this purpose.

* Good, because the mapping can change in the fly
* Good, because there is support for this approach in most languages
* Bad, because more development/evaluation overhead

### Control Topic

We already use Kafka so we could follow the [dynamic router pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DynamicRouter.html) and use a control channel(topic) to configure the instances. This topic could use the [compaction feature](https://kafka.apache.org/documentation/#compaction) to always retain the last known configuration for each message key.

* Good, because we already decided to use Kafka
* Good, because this option provides a log of configuration changes
* Bad, because the configuration for Kafka could not be provided via this method
* Bad, because more development/evaluation overhead


### Function composition

We don't implement the generic component as a separate component but as a function which is hosted on the FaaS solution. There is a [Kafka connector](https://github.com/openfaas-incubator/kafka-connector) for OpenFaaS. Then compose the functions with a composer like [this](https://github.com/s8sg/faas-flow) or follow the workflow techniques described in the OpenFaaS [documentation](https://github.com/openfaas/workshop/blob/master/lab4.md#create-workflows).

* Good, because the basic components for this approach already exist
* Good, because no separate generic component is necessary
* Bad, because the composer does not seem to be very mature and proven

### Function proxy (API Gateway)

Each instance of the generic component calls the API gateway which handles the routing/mapping to the functions.

* Good, because each instance of the generic component calls the same gateway and therefore needs the same configuration
* Bad, because we don't have this proxy and therefore this adds development overhead

### Configuration file

Generate a configuration file per instance of the generic component and deploy it with the instance. Same pros and cons like environment variables but more complexity for file generation/parsing and deployment.