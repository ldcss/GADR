# 9. Use jackson to read json files

Date: 2019-10-20

## Status

Accepted

## Context

Scratch save files are zip files that contain the actual code in a `project.json` file.  
To read this file we need a deserialization library.  
Jackson, GSON and org.json are common libraries.  
Jackson seems to offer the most features and the authors already have used it.
GSON offers many features Jackson also features.  
org.json seems to be only a json parser and the use has to create the resulting object themselves, while the other libraries also feature object mapping.   

## Decision

We will use [Jackson](https://github.com/FasterXML/jackson-databind/).  

## Consequences

Object mapping needs additional configuration.  
