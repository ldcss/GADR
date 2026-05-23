# Keep Infrastructure Code in a Separate Repo

Should our infrastructure code be collocated with the application code it is
supporting or in a separate repository?

Ideally the infra should be transparent to the application developers. They
should be focused on delivering what they need to in the app without caring
about the infra. The infra works. The infra is the same (enough) in prod and
CI. The app build results in an artifact that gets delivered into the infra
and everyone is happy.

## Decision Drivers

* Visibility of changes to anyone working in the codebases.
* Management of CI/CD configuration.
* Iteration speed.
* Coupling of infra and app changes.

## Considered Options

* Keep everything in the same repository
* Separate repo for Infrastructure

## Decision Outcome

* *Separate repo for Infrastructure.*

Decoupling the infrastructure and application deployments allows iteration to
happen on both of those aspects of the project at separate speeds without
hindering one another. We have experience in making this repo separation work
and can easily configure CI and deployment tooling to allow for proper
orchestration to bring these two pieces together.

Please see the full good/bad list below.

## Pros and Cons of the Options

### Keep everything in the same repository

Put all code application, infrastructure configuration, and any supporting
tooling in the same repository.

* Good, because you're able to see the application and the supporting  
infrastructure definitions all in the same repository. This makes searching  
the code base easier.
* Good, because all of the documentation including ADRs can be located  
in the same repository.
* Bad, because this couples infrastructure and application deployments.
* Bad, because it will take effort to get standard CI tools (such as  
CircleCI) to perform the right build actions on the right subdirectories.
* Bad, if we want to open source this repository, CMS might object to keeping  
the infrastructure code with it.

### Separate repo for Infrastructure

Keep application code and supporting tooling in a repository together and
create a second repository for infrastructure configuration.

Note that you may need to pull out tools into their own projects and manage
those separately. (Historically at Truss an example of this would be
`setup-new-aws-user`.)

* Good, because this separates concerns of the code. Application developers  
should be focused on the application first without caring about the  
infrastructure. They should have the ability to ...
* Good, because this decouples infrastructure and application deployments.
    1. The application and infra can iterate at different speeds.
    1. Infra changes won't be blocked by slow CI/CD builds.
    1. Application changes won't be blocked by timeouts or broken infra  
    configuration.
* Good, because it's easier to scope the CI needs for each part of the  
project at the repository level.
* Bad, because if there is supporting tooling in the infra repo and it  
isn't integrated into the application repo or kept to up to date along side  
the application repo, then you may run into some issues.
* Bad, because commit history and documentation may be spread across the  
repositories. It may be harder to pinpoint changes or updates to documentation.
