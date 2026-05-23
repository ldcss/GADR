# ADR-001<br/> Should the seed template be opinionated on state management framework choice?


## Context
Given the speed at which state-management libraries, preferences and trends change, should this starter seed should assert an opinion via dependencies in this regard? 

Developers bring different skills and ideas to the table, should they be free to make a decision on the best tool for the job, based upon requirements, complexity etc?


### Who Was Involved in This Decision
- Alex Ward
- Chris Weight


### Relates To
- N/A


## Decision
The Hybrid seed template will _not_ express an opinion via pre-determined dependencies on what state management frameworks (if any) should be used. This can be decided on a per-project basis. Though there are positives and negatives either way, it is felt that the ability to rapidly implement changes to approach over the course of time and projects is a powerful plus.


## Status 
:bulb: Proposed on 2018-01-24
:white_check_mark: Accepted on 2017-06-23


## Consequences

### - Positives

+ Developers are free to work to their strengths and pre-existing knowledge when starting a project
+ There is flexibility should a 'better solution' become prevalent in *the future*
+ Reduces maintenance overhead in the starter seed
+ Developers not familiar with a particular state-management approach, framework, library etc have the opportunity to study how it is used 'in the wild' and gain expertise

### - Negatives

- A Developer on-boarding onto an existing project may not be familiar with the design pattern expressed by a chosen state-management framework or library. This will increase on-boarding time
- Consistency across projects is not guarenteed
- An unknown chosen state-management approach may ultimately prove to be a bad choice (hard to reason, difficult to maintain, overly complex etc)

