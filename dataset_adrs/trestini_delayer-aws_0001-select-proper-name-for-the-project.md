# Select a proper name for the project

*   Status: accepted
*   Proposers: trestini
*   Deciders: trestini
*   Date: 2018-04-27

## Context and Problem Statement

Even this is not essentially a technical decision, I believe that this "simple"
name probably will drive some other important decisions, like the creation of
terminologies, naming packages and other stuff, helping defining
functionalities, etc. According to [Martin Fowler](https://martinfowler.com/bliki/TwoHardThings.html) 
naming things figures out as one of the hardest things in computer science. 
Apart of a joke, I believe that choose a good name is a good success factor, 
but this is not a technical decision, which can make things harder.

## Decision Drivers

*   Consider the serverless nature of the project
*   Consider the simplicity
*   Consider the vendor specific nature
*   Consider the fact that this could not be a scheduler

## Considered Options

*   scheduler-service
*   aws-scheduler
*   serverless-scheduler
*   aws-timemachine
*   delayer-aws
*   call-me-later
*   imnac (i'm not a cron)

## Decision Outcome

Chosen option: "delayer-aws".

All the conception and idea behind of this project was made over
the "scheduler" word, which sounds natural, since the main purpose of the project is to *schedule* a
task to run in the future. However, the term "scheduler" reemsemble a lot of things that already are
in place, like *recurrence* e *orchestration*. The main objective of this project is to provide a way
to easily and cost-effectively execute tasks in future. Easily because it will be based in a Restful 
API to deal with tasks (in face of config files or configuration screen), and cost-effective by using
serveless architectural approach. This is very different of current set of tooling, which could be
called "schedulers" too (and actually are!), but do a LOT of thing other then this, like but not
limited to, recurrence and orchestration.
In summary, I would like to think that people would find here more a "system-to-system-todo-list" 
than in a complete "scheduler". That's why I think that "delayer" reflects much more what it will do
then "scheduler".
The suffix "-aws" aims to:
-   confirm that it is not multicloud
-   confirm that there are plans to build this for other cloud providers

### Positive Consequences
*   clearly defines what this project do, and what it will do for the next iteractions

### Negative consequences
*   not using "scheduler" in the name can reduce the comprehensiveness about the project

## Pros and Cons of the Options

### scheduler-service

This is the name originally chosen (the repository was created with this name). Below arguments fits
for all "scheduler"-like names in the list.

*   Good, is simple and shows the main purpose of software
*   Bad, because is totally generic and doesn't reflects things that's should
makes it different from the other schedulers

### aws-timemachine

*   Bad, a "timemachine" recriates an ideia of going to and back in time. This sofware has only the
"future" concept
*   Bad, because can be confused with Apple Timemachine (in name and features)

### call-me-later

*   Good, reflects **exactly** what this software should do
*   Bad, to much informal
*   Bad, doesn't appear to be a software name

### imnac (i'm not a cron)

*   Good, it's common the use of acronyms in open source world
*   Bad, hard to remember
*   Bad, resembles nothing 

## Links

*   Two Hard Things in computer science: https://martinfowler.com/bliki/TwoHardThings.html
