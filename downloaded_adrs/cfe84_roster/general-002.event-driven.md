# Decision

Application is using events as the primary citizen for data modification

# Detail

The primary updates to any data is done through events. e.g. adding a user is done by publishing an `userAdded` event. Events are the source of truth. Transmutation into a readable state is done through listeners that record the state to databases (either local, or on the server).

# Reason

There are multiple:
- Adequacy to "mobile first" where synchronization might be complex, and having dated events at the source of truth makes things much, much simpler.
- Traceability