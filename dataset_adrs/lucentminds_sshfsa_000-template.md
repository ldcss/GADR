# Title
ADR-001: Adopting Go language.  
`These should be short enough to fit in a commit message.`

# Summary
We decided to upgrade from nodejs to Go to support portability better.  
`This should be super short and concise—maybe even 140 characters or less.`

# Context
We are currently using nodejs everywhere. It's hard to keep nodejs apps updated with all of their modules.  
`This should eventually become out of date, but still be contextually relevant! Without this context, the decision record might not make sense when reviewed in hindsight. And usually the implementation of this particular architectural decision will make the context out of date—but this is fine!`

# Decision
We will migrate to Go for services X, Y and Z.  
`The decision is made up of full sentences, in the active voice.`

# Consequences
We will be able to compile a Go source to a single executable, but we will have to learn the best methods for debugging a Go app.  
`list all consequences (not just the benefits) to the decision, including what could go wrong.`

# Status
Superseded by [ADR-002](/adrs/002-going-back-to-nodejs.md)  
`Status should only be one of the following`

* `Proposed`
* `Accepted`
* `Deprecated`
* `Superseded`

`The last two are the only time when a decision record should be modified after creation (unless something is found to be factually wrong in the record). Furthermore, in the case of “superseded,” it may be useful to provide a link to the decision record which supersedes it like the example.`