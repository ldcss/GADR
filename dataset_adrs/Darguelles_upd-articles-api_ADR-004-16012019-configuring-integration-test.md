### **ADR-004 - Integration Test**

**Context**

In order to make sure we are retrieving the expected status and object responses from our API, we need to add an integration test layer in order to ensure the API is working as a single unit.

**Decision**

We gonna use the built-in Spring test module and [RestAsured](http://rest-assured.io/) in order to make request to the API in a more human readable way.

**Status**

Accepted

**Consequences**

To execute the integration tests we just need to execute the `intTest` task configured in our `build.gradle` file.
The main context is loaded from the Core application, in the future this can be configured in a own context loader for integration test.