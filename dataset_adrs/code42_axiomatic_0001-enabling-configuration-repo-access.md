# Enabling Configuration Repo Access

* Status: accepted
* Deciders: Dana, Darby, Josh, Milo, Jim
* Authored: 20201023 Decided: 20201109

## Context and Problem Statement

How should Axiomatic ensure that dir2consul, when run as a Nomad batch job, has access to configuration repos hosted on GitHub?

## Considered Options

1. Service User: A service user is created within the GitHub organization along with an SSH key pair. The service user is granted access to the configuration repos. The Nomad job definition for dir2consul is given the service users SSH key.
1. Axiomatic Retrieves Deployment Keys from Vault: Repo specific deploy keys are stored in Vault. Axiomatic retrieves the appropriate deploy key and adds it to the Nomad job definition for dir2consul.
1. Nomad Retrieves Deployment Keys from Vault: Repo specific deploy keys are stored in Vault. Nomad retrieves the appropriate deploy key and makes it available to the dir2consul batch job.
1. A Team Member becomes the Service User: Similiar to the 'Service User' option except that access to configuration repos is granted implicitly as the team member already has access.

## Decision Drivers

* GitHub prevents deployment key reuse. The SSH key can only be attached to one repo.
* There is no appetite for spending money on Service User accounts.
* Option 2 needs a process for creating the ssh key pair, adding the public key to the repo, and storing the private key in Vault (potentially automated via Terraform)
* Option 2 setup is an infrequent activity as would be key rotation
* Option 3 fundamentally cannot be done due to bugs/non-support in Nomad
* Option 4 was eliminated due to possible violation of our acceptable use policies

## Decision Outcome

Chosen option: Option 2, Axiomatic Retrieves Deployment Keys

### Positive Consequences

* Allows us to provide a repeatable solution for configurationn repos in the short term
* We will default to using read-only ssh access

### Negative Consequences

* Requires codifying a key management process and a potential automation effort

## Pros and Cons of the Options

### Service User

* Good, because the user can be used for other automation too
* Good, because configuration repo setup is merely granting read-only access to the service user
* Bad, because we are billed for every user account
* Bad, because the service user becomes a single point of failure
* Bad, because the service user may be used in other contexts where config repo access is not acceptable
* Bad, because the lack of fine grained permissions capability leading to the creation of multiple service user accounts
* Good/Bad, because a service user may have write access to a repo
* Good/Bad, because a service user may provide GitHub API access

### Axiomatic Retrieves Deployment Keys from Vault

* Good, because deploy keys are unique to each repo
* Good, because the keys are securely stored in the centralized Vault making rotation easy
* Bad, because it increases the work to set up a configuration repo (create the SSH key, add it to the GitHub repo, add it to Vault)
* Bad, because it requires Axiomatic to have knowledge of deploy keys and access to Vault
* Good/Bad, because a deploy key can only provide limited write access to a repo
* Good/Bad, because a deploy key does not provide any GitHub API access

### Nomad Retrieves Deployment Keys from Vault

* Good, because Axiomatic and dir2consul are freed of deploy key knowledge
* Good, because Axiomatic and dir2consul do not need access to Vault
* Good, because it leverages the Vault access that Nomad already has available
* Bad, because Nomad currently can't do it. Nomad has to retrieve the deploy key before it attempts the git clone via the jobs 'artifact' stanza. Hashicorp is aware and already working on the issue. Reference [Nomad Github Issues](#nomad-github-issues)
* Good/Bad, because a deploy key can only provide limited write access to a repo
* Good/Bad, because a deploy key does not provide any GitHub API access

### A Team Member becomes the Service User

* Good/Bad: Same as the Service User
* Bad, because the audit trail always points back to the team member
* Bad, because it puts the team member in a bad spot if a security event occurrs
* Bad, because it likely violates our security standards

## Links

### Deploy Keys

* [Managing Deploy Keys](https://docs.github.com/en/free-pro-team@latest/developers/overview/managing-deploy-keys#deploy-keys)

### Nomad GitHub Issues

* [Cannot download private git repo with artifact stanza](https://github.com/hashicorp/nomad/issues/2818)
* [vault secrets in artifact stanza](https://github.com/hashicorp/nomad/issues/3854)
* [allow passing GIT_SSH variables to go-getter](https://github.com/hashicorp/nomad/issues/6619)
