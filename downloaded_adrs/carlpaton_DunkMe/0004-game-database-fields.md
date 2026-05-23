## Game Database fields

#### Context and Problem Statement

All game records need to be persisted to the relational database with reporting in mind.

#### Considered Options

- dbo.game for each game record, dbo.game_line for each shot attempt.

#### Decision Outcome

Chosen option: dbo.game with dbo.game_line

- Each shot attempt is recorded with a score of 0 for miss and 1 for a dunk
- Verbose logging like this will make reporting easier and leave nothing to interpretation

## Pros and Cons of the Alternatives

### *[dbo.game with dbo.game_line]*

* `+` *[Exact amount of shots makes for simple reporting]*
* `-` *[Additional relatively un-necessary lines for 0 scores]*



([back](README.md))