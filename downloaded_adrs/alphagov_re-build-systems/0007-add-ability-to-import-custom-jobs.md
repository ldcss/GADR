# 7. Provide ability for the user to import custom jobs

Date: 2018-08-24

## Status

Accepted

## Context

We need the user to be able to define Jenkins jobs in code and be able to import them into Jenkins.

We have identified a number of ways to do this:

1. Define jobs with Groovy and inject the script, as we do for the Jenkins configuration
2. Automatically create the jobs by scanning a Github account
3. [Jenkins Job Builder]
4. [Job DSL plugin]

### Option 1
This is the easiest for us as we don't need to implement anything new. We can use the mechanism of injecting Groovy script which is already available. It is also relatively easy for the user to use. The code for the jobs and configuration can't exceed 16 KB, which is a limitation, but we believe that is enough for compact Jenkins installations (a Jenkins with hundreds of jobs is an anti-pattern). [The limit] is because we use [user data] to implement this option.

### Option 2
 Jenkins provides a way to scan a Github organisation or accounts for repositories containing pipeline configurations in a Jenkinsfile. This should be quite easy for the user but the implementation can be quite complex. This option would require the user to pass extra parameters to the Jenkins Terraform module: at least one regular expression to filter the repositories to match, and a Github personal token. The token is needed because scanning Github as an unauthenticated user is extremely slow but only takes a few minutes for a user with authentication. As the module needs a token as an input, there is extra complexity around managing that secret. This would be relatively straightforward to do using the UI but providing this solution as code would be quite involved.

### Option 3
 (Jenkins Job Builder) is probably the most commonly used at GDS (it's used by Notify, Digital Marketplace) - people generally like it but some issues were pointed out like a difficulty in upgrading to a newer version or in escaping quotes correctly. [GOV.UK] and Pay use a more ad-hoc, homebrewed approach. Both groups rely on Puppet or Chef to inject their jobs into Jenkins. We allow users to install their configuration management tool via cloud-init, so the user is still free to override any mechanism we provide.

### Option 4
 This hasn't been explored in great detail as we felt we'd already found a good solution. However, if we revisit the decision made in this PR, this tool should be evaluated more thoroughly.

## Decision

We decided to implement solution 1 to keep things simple and because of time constraints. Options two and three can still be used but will not be supported. In the future, we may consider to change to another solution if we feel there is the user need.

## Consequences

The user is able to import jobs into Jenkins that are defined in code, the definition of the jobs and configuration can't exceed 16 KB.

[Jenkins Job Builder]: https://docs.openstack.org/infra/jenkins-job-builder/#jenkins-job-builder
[Job DSL plugin]: https://github.com/jenkinsci/job-dsl-plugin
[GOV.UK]: https://docs.publishing.service.gov.uk/manual/testing-projects.html
[user data]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html
[The limit]: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html
