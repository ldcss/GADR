# Build and deploy EASi backend to AWS Fargate

The EASi application backend is a server written in golang.

We want to be able to manage the infrastructure
configuration and service definition together in code.
We want a deployment platform that is low effort to
maintain and has rollback capabilities.

## Considered Alternatives

* *Build AMIs and deploy EC2 instances*
* *Build Docker containers and deploy services to ECS*
* *Build Docker containers and deploy services to ECS: Fargate*

## Decision Outcome

Chosen Alternative: *Build Docker containers and deploy services to ECS: Fargate*

It may take a bit more effort to trail blaze the patterns of
container management at CMS and we might need to do more
TRB consults or Security consults but AWS will do most of the
heavy lifting for scalability and maintenance.

## Pros and Cons of the Alternatives

### *Build AMIs and deploy EC2 instances*

* `+` This is a well practiced deployment pattern
* `+` AMIs are an immutable artifact
* `-` There's a lot of glue to properly instantiate your instances
* `-` Building AMIs is slow
* `-` You have to manage instance lifecycle (*)

`*` There is a new type of autoscaling group that can help manage
instance lifecycle based on uptime of instance but it was _just_
announced. I don't know if or how it works yet.

### *Build Docker containers and deploy services to ECS*

* `+` Docker containers can be immutable artifacts
* `+` Docker containers are a known pattern for Truss
* `-` Docker containers are a new pattern at CMS
* `-` Managing the security of the underlying ECS servers
* `-` You have to manage instance lifecycle

### *Build Docker containers and deploy services to ECS: Fargate*

* `+` Docker containers can be immutable artifacts
* `+` Docker containers are a known pattern for Truss
* `+` AWS manages the security of the underlying servers
* `+` AWS manages the underlying server lifecycle
* `-` Docker containers are a new pattern at CMS
