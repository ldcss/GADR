# 6. Use arduino-cli to upload/compile code for the ftduino

Date: 2019-10-20

## Status

Accepted

## Context

We need some way to compile the generated code, which the scratch converter produced.  
We need some way to upload the code to the ftduino.
We found two programs that could be used:
- [arduino-cli](https://github.com/arduino/arduino-cli)
- [Arduino](https://github.com/arduino/Arduino/blob/master/build/shared/manpage.adoc)  

The Arduino program provides a command line interface.  
It needs to have a java runtime bundled and it also has all the files needed for running the full Arduino IDE.  
It is bigger than arduino-cli.  
Arduino-cli is a single program written in Go. It is newer, but also more sensitive to configuration problems (Read: It crashes).

## Decision

We will use arduino-cli to compile and upload code for the ftduino, because it is a single program.

## Consequences

-