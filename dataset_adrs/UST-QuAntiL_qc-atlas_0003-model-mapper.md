# Use a Model Mapper to convert entities to DTOs and vice versa

* Status: accepted
* Deciders: [Q-tal Enpro Team]
* Date: [2020-06-04] <!-- optional -->

## Context and Problem Statement

Due to the use of two different object types for transfering and storing data, the conversion between the types becomes a necessity. Therefore we need means to perform the respective conversion.

## Considered Options

* Manually written conversion methods
* [Model Mapper](http://www.modelmapper.org)
* [MapStruct](https://mapstruct.org/)

## Decision Outcome

Chosen option: "[Model Mapper](http://www.modelmapper.org)", because it fulfils our requirements, is highly configurable and less error prone then manually written converters.

### Positive Consequences <!-- optional -->

* Less boilerplate code

## Pros and Cons of the Alternatives 

### Manually written conversion methods

- `+` Requires no extensions
- `+` No performace overhead
- `-` Hard to maintain
- `-` Prone to errors and bugs

### Model Mapper

- `+` Easy to use
- `+` Very powerful
- `+` Does not require any extensions
- `+` Works without errors, if configured properly
- `-` Since it's based on reflection, it may be slower than the other two options considered

### MapStruct

- `+` Very Fast
- `+` Easy to use
- `+` Works without errors, if configured properly
- `-` The approach is based on code generaion, like Lombok.
- `-` Needs a seperate plugin for the IDE and Maven to work properly
