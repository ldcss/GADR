# Executor Engine Separation

* Status: accepted
* Deciders: roleyfoley, ml019
* Date: 2020-02-13

## Context and Problem Statement

Hamlet is currently built on two application stacks, a set of bash scripts which run deployments and invoke the generation of outputs, and a freemarker wrapper with supporting templates which handles the creation of outputs. There is a tight coupling between these components and it is difficult to determine the authoritative source of context which we share between the these to stacks.

## Decision Drivers

* To improve user experience we have introduced a cli tool which is based on the [click library](https://click.palletsprojects.com) which is built in python. Integrating this cli into the environment has highlighted the need for this cli tool but also exposed the tight coupling between these two application stacks

## Considered Options

* Replicate the cli feel provided by click into our existing bash environment and maintain the existing coupling
* Migrate the bash processes into a Java based application which can call freemarker ( a java based process )
* Create a clearly defined abstraction layer between the existing bash scripts and the freemarker wrapper

## Decision Outcome

Chosen option: "Create a clearly defined abstraction layer between the existing bash scripts and the freemarker wrapper"
Makes our architecture cleaner and provides a clear way for hamlet to scale in the future

### Positive Consequences

* We have more explicit definitions of what hamlet is made of and how it works
* We can make choices on appropriate tools for specific services within hamlet

### Negative Consequences

* Defining and building the layer separation will add complexity to hamlet

## Pros and Cons of the Options

### Replicate the cli feel provided by click into our existing bash environment and maintain the existing coupling

Rather than looking at introducing a new tool into hamlet we instead update our existing bash based scripts to offer a centralised CLI experience. In this model a central bash script ( called hamlet ) would invoke the other bash scripts that we currently need to know exist and to call.

* Good, because this removes extra dependencies on other tool sets and the education required to introducing these tools
* Good, because it requires less effort to introduce and migrate to
* Bad, because the bash testing and tooling services aren't as mature as other languages as bash is mostly intended for scripts rather than applications

### Migrate the bash processes into a Java based application which can call freemarker ( a java based process )

This would move the bash scripts we currently have into our freemarker wrapper java application. This would require rewriting all of our bash scripts into java equivilents and providing a JAVA based cli

* Good, because this would reduce the number of application stacks involved in the hamlet system
* Good, because this would be cross platform as java is intended to be cross platform
* Bad, because this would require significant training and retooling of what we currently have

### Create a clearly defined abstraction layer between the existing bash scripts and the freemarker wrapper

This would maintain our existing tooling but introduce an abstraction layer between the two services, in this model we would define the freemarker components as the engine, this is responsible for creating outputs from the the contents of the CMDB which outline a list of instructions as contracts and any supporting documents that they require. The bash components would become an executor, they are responsible for actioning the outputs provided from the engine and providing the outputs from these executions back to the CMDB.

In this model the engine would be invoked with a default set of parameters requesting a generation contract, the engine would create an output which outlines the additional output documents required for a given action. The executor then invokes the engine using the parameters provided in the contract to create the outputs required. This could include other contracts which the executor then runs to perform additional tasks in order to complete a given action. T

This requires the executor to essentially implement, the contracts would be made up of defined steps and include parameters required to complete the step. The executor is responsible for providing an implementation of all steps defined in the engine

* Good, because this creates a clear line between what the bash tooling performs and what the freemarker tooling performs
* Good, because this defines functionality within hamlet rather than basing it on tooling
* Good, because this allows for the functionality implementation change if required with reduced impact and redevelopment
* Bad, because it introduces a new layer to the way that hamlet works which requires design and implementation in our existing stack. So rather than rewriting existing processes we need to redevelop our existing implementation to incorporate this design
