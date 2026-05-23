# 18. Conversion of unknown scratch functions to C will fail

Date: 2019-10-20

## Status

Accepted

## Context

Only a subset of all scratch functions has been implemented.  
It might make sense to ignore unsupported functions.  
This would make sense when encountering sound/image related functions.  
So the user could still use these functions when using the web version and not using the offline version.  
On the other hand the user will be surprised that some functions won't actually work.  
Functions silently being ignored would make troubleshooting harder.  

## Decision

Unknown scratch functions will cause the conversion to C to fail.

## Consequences

Unknown scratch functions can not be used.