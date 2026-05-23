# 2. Use containers and multiple boxes

Date: 2018-06-25

## Status

Accepted

## Context

The aim of this project is to allow teams to quickly create their own Jenkins
platform, running on AWS.

Jenkins has a master/agent architecture, where a single master node can trigger
jobs running on multiple agents. This decision concerns how we deploy, configure
and manage both the master and the agents.

## Decision


We will make both the master and the agents Docker containers, running on
separate managed EC2 instances. We will provision and manage these directly for
now, without using an orchestration service like ECS or Kubernetes.

### Use of separate instances

Having separate instances for the master and the workers increases security by
making it impossible for code running in worker jobs to affect the master.

In addition, this allows for teams to increase capacity by adding extra worker
boxes as required.

### Use of Docker for master

Running the master in Docker makes it easy to deploy and upgrade. This improves
teams' abilities to quickly respond when new Jenkins versions are released in
response to security vulnerabilities, for example.

In addition, using Docker means that the configuration can be kept in the git
repository along with the rest of the code, rather than managed via the Jenkins
UI.

### Use of Docker for agents

Running the workers as Docker containers allows isolation of each job, ensuring
that each job starts from a known state, making it possible to target a specific
configuration via the Jenkinsfile, and increasing security by making it
impossible for the job to affect the underlying VM.

### Not using orchestration frameworks

Although some teams at GDS are experimenting with ECS, the Jenkins service is
simple enough that it is not worth introducing the added complexity for this
project.

## Consequences

The current architecture does not allow jobs to create new Docker images as part
of their steps. Some teams are using this functionality, so their Jenkinsfiles
will require changes.

Supporting this would be possible by creating an additional worker which mounts
the Docker socket on the box within the agent container, although this may have
security implications.

