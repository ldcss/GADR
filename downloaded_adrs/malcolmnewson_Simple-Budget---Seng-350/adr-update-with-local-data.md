# ADR: Update summary and analytics with local data when new purchases are made
### Status
Proposed

### Context
To improve user experience, the purchase summary and analytics should be able to reflect all purchases that a user has made, including purchases logged during a users session. The main factors related to user experience are performance (loading the summary and analytics quickly), data accuracy (accurate summaries and analytics), and data integrity (new purchases are successfully stored in the data store).

Therefore, a decision needs to be made on how to handle showing new purchases that have been logged during a user session in the purchase summary and analytics.

### Decision
It was decided to locally update purchase summaries and analytics on the client-side with the input from new purchases. The alternatives would of been to 
* update the datastore with the new data and then update the summaries from the datastore, or,
* implement caching using a tool such as Redis.

This decision enables the purchase summaries and analytics pages to show new purchases very quickly, and reducing the traffic load on the server; addressing the [Performance QAS](https://github.com/seng350/seng350f19-project-2-1/issues/10). 

Additionally, this decision requires user feedback to inform the the user if a new purchase has been successfully stored, or if there has been a failure and they need to resubmit their purchase in order for it to not be lost.

It was decided to not implement caching in order to reduce complexity in the development of this application. It was decided to not wait for the purchase to get stored in the datastore before updating the summaries and analytics page as it would of decreased the performance of the application.

### Consequences
* Loss of data integrity if the datastore fails to update successfully.
* Improved performance with regards to server loading and purchase summary and analytics refresh speed.
