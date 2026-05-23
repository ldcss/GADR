# ADR 02: Credential Storage

* Status: accepted
* Interested parties: @zwolf, @camallen, @adammcmaster
* Date: October 21, 2019

## Context

Rails apps need access to environment-based credentials (API keys, db URLs and passwords, etc). We do this a few different ways across all of our Rails apps. This ADR is a chance to take everyone's temperature on using a neat but new bit of Rails 6 and inform similar decisions later.

## Considered Options

* Kubernetes secret storing encoded environment variables
* Rails internal credential storage solution
* Kubernetes mounted dotenv volume

### Option 1: Kubernetes encoded env variables

A list of environment variables are base64-encoded and piped into a k8s secret. Loaded by being added individually to the templates.

Pros:
* Our current standard (Caesar, PRNAPI)--or as close to one as we have.
* Each var exists in template, so the contents are clearly defined.

Cons:
* Whole base64 encoding thing makes reading/editing credentials a chore
* Credentials are stored entirely seperate from the app, tying their values to deployment/k8s instead of to the app.

### Option 2: Rails internal credentials

As of Rails 5.1, Rails supports storing its own credentials. Rails 6 includes support for this feature across multiple environments. A `config/[environment].yml.enc` file is encrpyted with a `config/[environment].key`. The latter is stored as a k8s secret and mounted in `/config`. The encrypted yml file can then theoretically be included in version control, but could also be stored in the same volume mount if that makes people nervous. Development key+creds can be kept in git and are used by default (via `RAILS_ENV`).

Syntax for the Rails helpers is as follows:
`rails edit:credentials --environment staging`

The `--environment` arg looks for `config/[environment].key` to decode `config/[environment].yml.enc`.

Pros:
* Simpler templates, since every var doesn't have to be included to still be accessible
* Follows new conventions, built into Rails.
* Keeps the app's requirements within the context of the app. A record is kept (potentially versioned, even) and redeployment (say, to Azure) has less steps.

Cons:
* Rails 6 only (for multiple envs). Our other apps will need upgrade all the way to use the same functionality.
* Different. This already an issue with our various other Rails apps, so it would be yet another strategy, but a fairly self-documenting one.
* Rails 6 is released and stable, but this feature is kind of new. 5.1 was a while ago, though.


### Option 3: k8s Mounted secrets volumes
Used by old Rails apps deployed to k8s (eduapi, for instance). Roughly the same as Option 1, since it's a list of envvars that is loaded by k8s into the environment, only with a mounted volume that completely obfuscates the contents everywhere. So it's like the first one, only worse. Including for reference, but not the direction we want to go.

## Decision Outcome

Decided to go with Option 2, Rails credentials. It's the most forward-looking option and isn't terribly different from existing setups. There's even a precedent in the graphql stats API. Also, as it's already being done in the aforementioned API, we're going to store encoded credentials in the repo.

### Links
* rails docs: https://edgeguides.rubyonrails.org/security.html#custom-credentials
* PR that added environment specificity: https://github.com/rails/rails/issues/31349
* quick blog post on use: https://blog.saeloun.com/2019/10/10/rails-6-adds-support-for-multi-environment-credentials.html
