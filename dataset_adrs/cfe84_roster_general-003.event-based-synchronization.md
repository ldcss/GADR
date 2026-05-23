# Decision

The synchronization between front-end and back-end is done through POSTing and GETing events

# Details

This is rather than a REST API. The REST API might come later.

A replication manager replicates all events to the server. There will be events that don't need replication (e.g. `replicationFailed`), these will be marked as `requiresReplication: false`.

# Reason

This is very simple to implement, and given the scale of the application and its mono-user character, should be good enough for now.