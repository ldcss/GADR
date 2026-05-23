### **ADR-002 - Docker support**

**Context**

The application can run on any machine with JVM installed, but what if we don't have a correct Java version in our machine or server environment? Containers comes to the rescue.


**Decision**

Docker (https://www.docker.com/) is an easy to configure container platform to manage our applications in isolated containers. That will help us to deploy our application in any environment with the Docker daemon installed.

**Status**

Accepted

**Consequences**

By the moment the container can be used just for deploys, development support can be added sharing a Volume in the Dockerfile. Instructions to modify the Dockerfile can be found [here](https://docs.docker.com/engine/reference/builder/). 