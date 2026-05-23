# ADR: Using Postman for API testing
### Status
Proposed

### Context
API testing can be used to ensure that the interface between the client and server is properly designed and implemented. This includes verifying response codes, API endpoints, and allows verification of returned data.

### Decision
Postman will be used to implement automated API testing, allowing consistent verification of correct communication between client and server. This will contribute to a quality controlled product with as few bugs as possible, as well as the [Testability QAS](https://github.com/seng350/seng350f19-project-2-1/issues/6). Postman has been chosen instead of other API testing tools such as SoapUI and Katalon studio in part due to its use in the lab component of Seng350. Some other benefits include its ability to function as a browser extension, free access for small teams, and easy to use characteristics. Because of the simplicity of this project Postman is a sufficient API tester.

### Consequences
* Postman implimented in the build pipeline.
* Verified API protocol between client and server.
