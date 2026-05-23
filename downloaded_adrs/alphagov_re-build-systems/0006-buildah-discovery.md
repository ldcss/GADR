# 6. Buildah Discovery Work

Date: 2018-09-03

## Status

Accepted

## Context

There is a desire from users to be able to build docker images as an artifact from their jobs, this creates a security problem because of technical limitations within docker.  This ADR is the result of discovery work to discern whether there are alternative solutions to building docker images securely.  The discovery focussed on evaluating the software product called [Buildah].

## Technical Problem

As the workers run within a docker container, they may need to build another docker image as an artifact.  To do so requires that the host servers docker socket be exposed to the worker container.  The docker daemon runs as root and has full control of the host server, meaning malicious code running within the workers docker container could trivially gain access to the host system by mounting (via -v) the host systems root.

As Docker does not support RBAC to control and restrict access to its socket there is no way provided by docker to prevent this privilege escalation method occuring.  

Buildah solves this problem by being able to build a docker container without the need to use docker and the vulnerable socket.

## Buildah Discovery Notes

1. Needs root access to run buildah commands - requires the same privileges as docker to run
1. Is a bit ackward to install, but we could package it up, meaning we'd have to maintain it
1. Requires non-standard repos (ppas) for installation
	- ppa:alexlarsson/flatpak (lead flatpak developer)
	- ppa:gophers/archive (go)
	- ppa:projectatomic/ppa (buildah official repo)
1. Builds the image and then we need to send to local docker, docker.io or ECR (if compatible) so that the image can be used
1. Worked well overall
1. Supports
	1. --build-arg
	1. --volume
	1. [Documentation](https://github.com/projectatomic/buildah/blob/master/docs/buildah-bud.md)
1.  Recommend that re-build creates a container specifically for buildah, and have that run and create artifact docker images which are then upload somewhere ready for consumption
1. If buildah artifact images are stored on the worker
	1. will be faster to build then run
	1. mean we have to manage those images (nuking old ones)
	1. may need to expose the docker socket (and re-introduce the problem we are trying to avoid)
1. If buildah images are stored on docker.io
	1. images will need to be uploaded after creation, then downloaded again to be executed, making things slower
1. If uploaded to a public docker.io
	1. we'd need to be careful about exposing secrets
1. If uploaded to a private docker.io
	1. data sovereignty concern
	1. work upon secrets management to allow the the upload and download
1. If docker images stored within ecr
	1. not 100% certain this is possible as it is not specifically noted
	1. should be fast
	1. can be managed by iam roles, endpoints, security groups etc
	1. can be version controlled and kept private
1. Other similar tools to Buildah and comparison table [here](https://github.com/GoogleContainerTools/kaniko#comparison-with-other-tools)

## Decision

Buildah addresses the problems of docker container privilege escalation, is feature rich to support typical use cases (as it is feature compatible with docker), and provides us a means in which to provide docker image artifacts.

## Consequences

There was no indepth discovery of alternative products which may be more appropriate.  Further discovery on other products might be neccessary.  


[Buildah]: https://www.redhat.com/en/blog/daemon-haunted-container-world-no-longer-introducing-buildah-10
