# Use jcabi github-api

## Context and Problem Statement

We need a Java-Client to interact with the GitHub API.

## Considered Options

* [jcabi's Object Oriented Github API](https://github.jcabi.com/)
* [org.kohsuke.github-api](http://github-api.kohsuke.org/)
* [org.eclipse.egit.github.core](https://github.com/eclipse/egit-github/tree/master/org.eclipse.egit.github.core)

## Decision Outcome

Chosen option: "jcabi's Object Oriented Github API", because it offers the most accessible way to the data returned by the [GitHub REST API v3](https://developer.github.com/v3/).
With `org.kohsuke.github-api` it seemed to be impossible to retrieve meta data about the pull request.
`org.eclipse.egit.github.core` is not updated on maven central. See [bug 454237](https://bugs.eclipse.org/bugs/show_bug.cgi?id=454237).
We accept that we need a [GitHub personal access token](https://github.com/settings/tokens) for interacting with the API.
