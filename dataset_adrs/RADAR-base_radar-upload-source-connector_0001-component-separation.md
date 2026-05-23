# Component separation into frontend, backend and connector with converters

## Context and Problem Statement

Given the need to upload files, process them and commit them to Kafka, how do we set up component separation

## Decision Drivers

* Usability – users should not have to wait too long, get a good overview of progress made, and understand and indicate how the data that they upload will be processed.
* Reliability – uploaded data should always be committed to Kafka or be marked erroneous
* Performance – data processing should be scalable.

## Considered Options

* Frontend and connector  – separate into frontend and connector with integrated backend.
* Frontend, backend with converters and connector  – frontend as before, but with a separate backend that does data conversion before it is processed by the connector.
* Frontend, backend and connector with converters – frontend as before, with a backend that only keeps track of uploaded files, and a connector that has a number of supported converters.
* Frontend, backend, converter job system, connector – frontend as before, with a backend that keeps track of uploaded files and starts up conversion jobs and a connector that commits the processed data to Kafka.

## Decision Outcome

Chosen option: "Frontend, backend and connector with converters", because it keeps the backend free from any issues with the connector. The connector can scale at wish. The setup is similar to "Frontend, backend, converter job system, connector" except the job system is integrated into the connector. This makes the connector a bit heavier on code and internal management but it keeps the amount of setup and configuration low.

### Positive Consequences

* Users have a responsive backend that gives them status updates because data is not processed in the backend
* Connector is in charge of conversion and Avro schema handling
* Connector can restart without any interruptions to the user interface.
* Severe conversion errors will not cause the backend to fail.

### Negative Consequences

* Converters do not reside in the backend, but the backend does need to know what converters are available. This makes the configuration a bit heavier.
* The connector configuration will become more involved with configuration for each converter.
