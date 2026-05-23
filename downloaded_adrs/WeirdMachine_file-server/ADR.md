# Architecture decision record

# Overall Architecture

Right now the Project consist of two classes and one enum.

The main class FileServer contains the entrypoint where the Server is configured and started. 
It opens the server socket and opens a thread for each request. This request gets than handled by the same class.

Response class is a wrapper for the response which contains HTTP header and some binary data.
It ensures that the headers are correctly set in combination to the binary data. 

The HttpStatus Enum contains the used HTTP Status codes and String. 

## Status

in review 

## Context

We want to server files via HTTP, without a framework or too much external packages. 

## Decision

The functionality of this server is very limited, so this project uses a more functional approach over object orientation.

## Consequences

It will be difficult to add more sophisticated features, or even to implement HTTP completely.
