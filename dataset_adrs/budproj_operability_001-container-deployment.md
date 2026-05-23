# ADR 1: Container Deployment

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)

## Context

Since we're using Docker and Kubernetes to provide our applications to our users, we need to find a way to build and deploy those containers in our infrastructure.

It is important to note that previous experiences showed us that completely integrated CI/CD pipelines create slow deployment processes. We need to avoid complete integration without losing speed and developer experience.

## Decision

We've decided to use [Hashicorp's Waypoint](https://www.waypointproject.io/) to handle the build/deployment task for us. It is a pretty new tool (released for public in 2020), but Hashicorp made some of the most used and stable tools in the market (like Terraform and Vault).

Waypoint can handle the container build process, deployment, and release. Since we're using a Gitops process, it still lacks some plugins for our deployment/release steps, but using it only to build even helps us make the deployment process more accessible.

We've tried this tool in our [Design System application](https://github.com/budproj/design-system). It was straightforward to create containers for our storybooks (the front-end of this application).

The next step is to create a Gitops plugin that can deploy the updated image manifest in our Argo Git repository or find a way to make Argo receive information regarding Waypoint deployment and release.

## Status

Accepted.

## Consequences

Since this is a new tool, it is always dangerous to lack community acceptance. But, we've found some issues with their CLI and received pretty quick answers.

Hashicorp has done an outstanding job.

---

## More reading

* [Waypoint's docs](https://www.waypointproject.io/docs)
