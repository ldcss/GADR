# Manage GitHub repositories with Terraform

- Status: Proposed
- Date: 2019-09-DD
- Deciders:
    - achotard
    - jpthiery
    - jmartinsanchez

## Context and Problem Statement

Working with microservices and a issues / Pull Requests based workflow, labels
for these issues and PRs are a must have and should be explicit about what the
issue/PR is about.

However, there are numerous labels that represent different kind of
information (scope, lifecycle step, concerned component, etc). Colors help to
identify these different kind of labels. In the end, managing all of this
manually is painful, and implies duplicate work across multiple services
repositories for common labels (closing reasons, PR lifecycle, etc.)

We want to find a way to handle this cleanly.

## Decision Drivers <!-- optional -->

- How easy it will be to integrate new repositories
- How much work we have to do to for minor changes

## Considered Options

- Handling everything manually, and writing some documentation/processes about
  our rules / common way of doing things
- Automate it with some infrastructure-as-code tooling

## Decision Outcome

Chosen option: **"Automate GitHub repositories management with
infrastructure-as-code, namely Terraform"**, because:

- We don't want to do things manually
- Having everything as-code is cool
- It will be easy to apply to many repositories
- We already use Terraform for a bunch of stuff so it's known by people

However, it will not be run automatically by our CI/CD pipelines at the
beginning, since Terraform needs an API access to GitHub and this would imply
creating a "machine user" GitHub account, which will be more thing to manage
than we want for now.

## Pros and Cons of the Options

### Handling everything manually

Pros:

- This is already what's being done
- Nothing more complicated than what people are used to do with GitHub

Cons:

- Is painful when applying a modification to a bunch of labels
- Will be a waste of time for new repositories (more and more labels)
- The GitHub UI has improved but is still a pain to use

### Automate it with infra-as-code tooling

In our case, there is no debate in the context of this project: if we use
infra-as-code tooling to manage GitHub repositories, it will be through
Terraform.

Pros:

- There is already a [GitHub provider for
  Terraform](https://www.terraform.io/docs/providers/github/index.html)
- Will allow to create Terraform modules for common stuff across repositories

Cons:

- More complex to apprehend than modyfing everything by hand in the WebUI
- People need to generate their own GitHub API token
- Will need a "machine user" GitHub account for the CI
