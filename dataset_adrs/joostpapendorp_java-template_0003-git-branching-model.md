# Use GIT-Flow branching model.
* Updated: 20200521 - Switched model after implementing full CI. 

We'll follow the [GitHub flow](https://guides.github.com/introduction/flow/) as our GIT branching model. Prior to 
implementing our Continuous Integration processes, we used the older
[GIT-Flow branching model](https://nvie.com/posts/a-successful-git-branching-model/). 

## How should we structure our repositories?
* Should we impose a git flow on our development process?
* If so, which flow should we use?

## Considered Options
* No model
* [GIT-Flow branching model](https://nvie.com/posts/a-successful-git-branching-model/) (current)
* [GitHub flow](https://guides.github.com/introduction/flow/)

## Decision Outcome
Currently, we use the GIT-Flow branching model. This older model allows us to quickly revert to previous versions, test 
releases separate from production and manually catch regressions usually caught by the test suite. 
It thus helps us to guarantee the quality by hand. 

It prevents loss of information in the repository, making it easier to read into past decisions and developments than 
when no model is in place.

However, this model is more formal and more cumbersome than the Github flow. 
Since we implemented our CI-process, we can now switch to this simpler model. 

We will therefor adopt the GitHub flow.

### Positive Consequences 
* We gain more insight into the history of the development…
* Quality of the deployed releases can be monitored more securely.
* Light-weight

### Negative Consequences
* Requires that a stable Continuous Integration process is in place.
