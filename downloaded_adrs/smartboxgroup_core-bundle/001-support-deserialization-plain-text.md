# 1. Support "deserialization" of plain text 

Date: 2020-05-07

## Status

Accepted

## Context

The built-in deserializers included in JMS are sufficient for most cases, but sometimes the provided payloads are not compatible with them. Situations like this include strings in plain text, where no deserialization is expected. Feeding this type of data to JMS raises an exception that stops the execution of the application.

In these cases, the serialization needs to be bypassed in a clean and transparent way that will allow the calling class to continue its execution.

## Decision

We decided to implement a custom deserializer **that accepts plain text**. 

This deserializer is plugged **as a custom deserializer** in JMS' configuration and called whenever the format type "plain_text" is passed to the Serializer class.  

## Metadata
Authors: @andres.rey
People involved: @david.camprubi 
