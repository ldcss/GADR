# 7. Use arduino-cli in offline mode

Date: 2019-10-20

## Status

Accepted

## Context

Arduino-cli normally downloads all required libraries on-the-fly.  
This might not be desirable at some institutions because they restrict Internet access or because many people using arduino-cli at the same time might saturate the available bandwith.  
Using arduino-cli in offline mode also means that we know which version of libraries are used, which simplifies troubleshooting.  
Arduino-cli supports multiple platforms.  
Each of these platforms has platform-specific tools that need to be downloaded.  
It is not possible to download the tools needed for a Windows host on a Linux host.  
We have to manually download the tools for the different platforms.   


## Decision

We will use arduino-cli in offline mode and manually download the tools for the different platforms.

## Consequences

It is hard to upload the versions of the different tools, because for each different platform each url has to be updated separately.  
