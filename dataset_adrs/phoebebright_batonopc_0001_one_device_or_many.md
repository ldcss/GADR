0001 Library handles many devices or just one
======

Status
-------

Made

Context
-------
The purpose of this library is to collect together data from one or more sensor devices, save that data to a database and periodically create and send batches of data for processing.

Should the library be setup to handle multiple devices, checking and logging data from each device in turn or should that be left to the application using the library?

Pros for Multi device
-------
1. easier for application developer - just provide the access details of each device and away you go.


Pros for Single device
-------
1. Each device may well have different timings and manage data in different ways. At two extremes:
    - data is stored on the device and collected daily
    - device requires sampling at 10 second intervals
    This level of complexity is better handled by the application.
2. If there are delays in collecting data from one device, this could have a knock on effect in the collection interval of another.
3. If one goes down they all go down.
    
Decision
----------
Keep it Simple - Library written for one device.  In future may add settings to accomodate threading if this proves useful.

Consequences
--------------

