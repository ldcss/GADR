# 13. Communicate with the scratch app via a local web-server

Date: 2019-10-20

## Status

Accepted

## Context

The scratch app has to invoke the arduino-cli program to compile the converted programs.  
The scratch app has to invoke the scratch-to-c program to convert the scratch blocks to a runnable arduino program.  
In both cases the scratch app would have to invoke a native program.  
This is not possible in current web browsers.  
This would be possible using e.g. Electron, but the authors don't know Electron and Electron would add around 100 MB size overhead and also mean that without Electron the app can't be used.  
Using a local web-server all that is needed is any browser, the scratch ftduino app and the local web-server.  

## Decision

We will use a local web-server that will be used by the scratch app to invoke certain native programs.  
The local web-server may also be used to host the scratch app itself for example when there is no Internet connectivity available.

## Consequences

Some schools may not like running a web-server. The web-server would also have to run at a non-standard port, so it does not need elevated rights.
