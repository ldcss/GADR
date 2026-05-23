# :bulb: Should the Web APIs be Synchronous or Asynchronous

:calendar: Date: 2/10/2020

## :heavy_check_mark: Status : Accepted

## :dart: Context

The Web APIs can be implemented as Synchronous or Asynchronous.

## :traffic_light: Decision

Considering the fact that the APIs does a datastore look up which can take some time, making the services asynchronous is the recommendation. 

The decision is based on the guidance provided by Microsoft here: https://azure.microsoft.com/mediahandler/files/resourcefiles/api-design/Azure_API-Design_Guide_eBook.pdf
## :trophy: Consequences

Making the service asynchronous will let consuming applications unblock the calling thread enhancing the user experience.