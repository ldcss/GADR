# ADR: Separate DAO for each action related to the datastore
### Status
Proposed.

### Context
The two main entities that are stored in the datastore are purchases, and the users. Purchases can be created, read, updated, and deleted. The users can be created, read, and deleted. 

### Decision
It was decided to create a DAO for each action related to the datastore. This will provide an interface between logic layer and the datastore. In doing so, the logic layer has access to the datastore without needing to worry about the implementation details. This allows modification or expansion to the logic layer to be performed without needing to change how the datastore is being accessed. This helps address the [Maintainability QAS](https://github.com/seng350/seng350f19-project-2-1/issues/10) by allowing modification or expansion to purchase summaries to be written efficiently. 

The alternative to this decision would have been to not create a DAO for each action on the datastore. This was rejected as it would require the datastore to be tightly coupled with accessing the database. This would have made modification or extension of the purchase summaries more difficult.

### Consequences
* Improved maintainability.
* This enables many of the core User Stories to be efficently implemented by utilizing clear interfaces to the datastore.
