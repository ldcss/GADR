# Saved Data

### Status

accepted


### Context

These hunts are designed to be 1-3 hour long or longer. Some players may not 
have that time to block out. There should be a way to save the progress of a
hunt inside the game.


### Decision

We do not want to administer a database and everything that comes along with
that (users, access, groups, etc). Store progress on a hunt in a local file
or "database" thing. Allow for resets of the hunt when loading. 


### Consequences

- Removes need to admin a database
- Removes network complexity
- Keeps costs low
