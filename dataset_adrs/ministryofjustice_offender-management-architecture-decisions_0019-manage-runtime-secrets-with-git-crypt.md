# 19. Manage runtime secrets with git-crypt

Date: 2019-01-30

## Status

Accepted

## Context

The recommended way of managing application config needed at runtime on the
cloud platform is to use Kubernetes secrets. These can be created manually
using kubectl on the command line to apply config files, or as part of a
deployment process.

We want to manage as much of our application config as possible in
version-controlled code, so that we can see when config was changed and so
that we can easily reproduce changes and rebuild environments.

The team are used to using [git-crypt](https://www.agwa.name/projects/git-crypt/)
to encrypt files containing secrets from their work on Visit someone in prison,
but that service is hosted on a different platform which means that the secrets
are in a private repo, separate from the application. It's easy to forget to
update config at the right time when it's managed separately from the
application, and that has resulted in production outages in the past on that
service.

If we use git-crypt to encrypt secrets files in public repos rather than
private ones, the risk associated with accidentally pushing secrets in
unencrypted files is increased. If we take this approach, we would want to make
it easier to avoid doing that rather than relying only on people being careful.

We are using kubectl for deploying. Some other teams are using helm, which has
support for templating so that values for config files can be kept separately
from the structure of the configuration. Unless we start using templating of
some kind in our config files, we will need to keep the whole files containing
Kubernetes secrets definitions private instead of just the secret values.

### Other options

Alternatives to using git-crypt in public repos include:

- separating out secrets into a private repo, using git-crypt there instead.
  This would increase the likelihood of us not updating the config when it's
  needed, leading to production outages.

- creating Kubernetes secrets manually from the command line, using config
  files committed in the application repo without secret values or encryption -
  so the secret values would be generated as needed and only stored in the
  relevant namespace. This would mean that our Kubernetes secrets could not be
  deployed as part of our automated pipeline but would need to be manually
  updated, and the manual workflow for updating a single value in a secret
  with multiple data values would be more complex. We would need to be careful
  to not accidentally commit the values in the secrets files after deploying
  them.

- storing secret values in CircleCI envvars, to be used when creating
  Kubernetes secrets during deployment, using templating in our secrets files.
  CircleCI has no concept of environments (all envvars for a project are
  available to all jobs) so all of our test and build steps would have access
  to production secrets, and we would need to define an approach to namespacing
  CircleCI envvars for different environments. Even so, envvars needed for
  running tests, building and pushing images, running deployments and running
  applications in different environments would all live together in one list,
  which would make that list more confusing than it already is.

- using another secrets store to manage our secrets, probably instead of using
  Kubernetes secrets. This would add another external dependency for our
  applications and would have the same challenges around either managing
  secrets values manually (thereby losing the ability to automate processes) or
  finding somewhere to manage version-controlled secrets from, and having
  another place to coordinate changes to required config with application
  deploys. It could also introduce another system for the team to authenticate
  with in order to manage secrets.

## Decision

We will keep the Kubernetes secrets definitions which are related to our
applications in the public application repos, encrypted with git-crypt.

We will only add team members who need access to production secrets to the
git-crypt setup. The only exception to this is our CircleCI deployment jobs
which need to decrypt the secrets to deploy them.

We will define a standard for creating and managing GPG keys and only use keys
with the git-crypt setup which meet that standard.

We will set up pre-commit hooks on our repos which contain encrypted secrets
to help us use git-crypt well.

We will agree processes for revoking credentials with other relevant teams in
case they are accidentally exposed.

If another standard way of managing secrets for applications running on the
cloud platform is developed, we will consider using that instead.

## Consequences

We will have fewer places to manage config needed by our applications in
production, making it less likely that we forget to make or apply a required
config change and so reducing the likelihood of breaking production.

Our production config will be entirely managed in code, making it easier to
rebuild environments if we need to. Our only manually-created config will be
CircleCI envvars.

We will still need to be careful to not commit secrets in unencrypted files in
our application repos, or to rename files containing secrets without also
updating the corresponding git-crypt config (although pre-commit hooks can
help us with this).

We need to remain aware that git-crypt does not fully support removing users
who no longer need access, and that in any case secrets should be rotated if
possible after someone has left the team.
