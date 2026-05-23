# 9. Source information node storing source locations

Date: 2021-11-01

## Status

Accepted

## Context

The custom AMF validator needs to show the location of the file from which each error was generated. 
Given the current state of the amf model and emission of jsonld, there was no way to obtain the location of a specific node. 

## Decision

A new node was defined as a field in BaseUnit call BaseUnitSourceInformation, which has the necessary information to obtain the source location of any node.
Internally, this node has two fields, one that stores the root location, and another that stores LocationInformation nodes which contain alternative locations with the ids of all the elements parsed from that location.
A new render option was included making the emission of this node to jsonld optional and not activated by default.

An alternative solution was to serialize SourceLocation annotation in each node, but this leads to a 25% or more increase in size of the resulting jsonld, as the paths are stored in a redundant fashion.

## Consequences

In large apis with multiple references to external files, the resulting jsonld is increased by around 4% when the option of source information is used.

It is also important to take into account that this node is generated during parsing, so after resolution there will potentially be elements with new ids that won't match correctly in the source information structure.
As the custom validator is currently using a non resolved model the generation of the source information node is done just before parsing, but ths will have to be adjusted if we decide to use a resolved model.
