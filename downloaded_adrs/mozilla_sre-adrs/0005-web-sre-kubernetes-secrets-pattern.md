# 5. web-sre-kubernetes-secrets-pattern

Date: 2021-06-09

## Status

Accepted

## Context

Secrets are inconsistently managed across our various clusters.  This makes it hard to trace where secrets come from and update them.  It also increases our exposure to security issues, as our each tool used can become compromised independently.  Current known secret management includes git-crypt repos, with sops, that apply kubernetes secrets direct to the cluster; sealed secrets; and external secrets pointing at cloud provider secret storage.

There are a few other methods that treat things that should be secrets incorrectly. For example, baking the 'secrets' into the docker image directly. This is a bad state to be in, and we will treat those situations with more urgency, correcting the pattern as soon as possible after this ADR is accepted.

The goal of this document is to describe the happy path for passing secrets to kubernetes based applications.  In general non-kubernetes secrets management is out of scope for this document, but we will cover how serverless deployments (lambdas) and CI/CD are impacted by this choice, and what we expect those to look like after adopting the ADR.

## Decision

Store the secrets in the cloud provider secret manager (aws secret manager, gcp secret manager), then use external secrets (https://github.com/external-secrets/kubernetes-external-secrets) to retrieve those secrets and present them to pods as env variables.  The reason this storage method is preferred is that the cloud secret managers seem to be the best secured, most tested, easiest to use place to store secrets. External secrets connects to the secret managers and presents the secret(s) in the method most often recommended for kubernetes; the 12 Factor App pattern of using environment variables.  One other nice benefit of this system is that references to the secrets can be stored in source code, so the connection between the app and the secret storage is explicit. The secret value itself is not in source code, which has the benefit of reducing the risk of leaking the secret accidently.

There are currently a few ways the secrets can be written to the cloud secret store. We have some terraform that writes the secrets directly to the secrets stores, but most secrets are populated manually by operators.  We expect both methods to be used going forward.  In general, we expect SREs/Operators with elevated privileges to manage the secrets.  This ADR intentionally doesn't include scope for devs to write new secrets, or update existing ones.

The default assumption for storage patterns in aws secrets store is that you follow the pattern: `<group>/<app>/<environment>/<secretname>` for example `mozmeao/snippets/stage/database_url`  This seems to make writing aws iam access stanzas easy.  Not needing to be rewritten with each new secret added.  But, enough separation to prevent us from accidentally crossing wires.

We want to choose just one secret storage and retrieval method, because having one known good way makes operators experience much simpler.  The alternatives/already existing methods are listed below with a quick note on why we didn't standardize on them.

We are choosing to not use a few other types of secret storage mechanisms, including (but possibly not limited to):
* git-crypt secret repos + sops, to k8s secrets directly.
  * Many manual steps to get secrets to prod
  * Difficult to remove access after people left (git-crypt doesn't support removing keys, you have to re-encrypt)
* Sealed secrets
  * The workflow and pattern is similar to externalsecrets, keeping both therefore doesn't make sense (doubles our maintenance burden, with little extra benefit)
  *  sealed secrets require extra cli tools and setup on operator computers, so is just ever so slightly more difficult to use than externalsecrets
* SSM Parameter Store (lambdas/codebuilds use this)
  * is mostly just an earlier version of secrets manager
  * splitting secrets between two places leads to duplication
  * the workflows are so similar maintaining both seems sub-optimal
* no new systems to be built, for example hashicorp vault
  * that's an entire project in and of itself, so we're choosing to not do that because the 'buy' choice is good enough.
* adding secrets directly to docker images, or directly in source code (high priority to fix these!)
  * Avoiding these because security has informed us this is explicitly a bad practice. Makes it way too easy to leak the secret to the world.



We expect CI/CD pipelines to use their current secret storage, and not try to connect them to the secret store.  The one exception is the cloud native pipeline solutions (e.g AWS CodeBuild), which should use the secrets manager if possible.  We may end up duplicating secrets, but in general we should try to keep application secrets and pipeline secrets separate, with pipeline secrets being manually added in the right context.

## Consequences

- Subject to prioritization and practicality concerns, we will migrate secrets to this solution, which can be a reasonably risky process for many applications.
- We will have fewer methods for managing secrets, which ought to make it easier to rotate secrets, keep them up to date, etc.
- We are gatekeepers for adding new secrets, which may increase unplanned work for our team.
- If we were to lose the secrets manager completely, rebuilding would be a long and arduous process.
- Updating secrets will include manual steps, like rotating pods, to use the new secret.
- Because secret updates need manual intervention we can update one pod, make sure it comes up healthy, and then update the rest of the pods with the new secret.
- CI/CD and repos (including public helm charts) can reference secrets safely, without accidentally leaking the values.
