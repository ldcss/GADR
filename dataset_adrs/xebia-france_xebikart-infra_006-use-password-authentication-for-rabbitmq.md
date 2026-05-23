# Use Password authentication for RabbitMQ

- Status: Accepted
- Date: 2019-04-10
- Deciders:
    - jmartinsanchez
    - achotard

## Context and Problem Statement

We are deploying a RabbitMQ cluster on GKE and people will need to connect to
it. We want to provide some kind of authentication so it's not totally
open-bar.

What authentication mecanism should we use?

## Considered Options

- Client certificate authentication
- User/Password authentication

## Decision Outcome

Chosen option: **"User/Pawword"**, because:

- We want to make the RabbitMQ cluster quickly available to teams
- It will be easy to change to client certificate auth later on
- It is better than not providing auth at all

We **will replace it by client certificates authentication later**.

## Pros and Cons of the Options

### Client certificate authentication

Pros:

- It is overall the safest solution
- Client certificates can easily be stored in Kubernetes secrets

Cons:

- Certificates rollout is painful and boring

### User/Password authenfication

Pros:

- Easy to setup

Cons:

- Will make us store plain text secrets in the Helm values for now
- Not really safe, especially with basic passwords

We could maybe store these password in Kubernetes secrets so they're not in the
manifest in plain, but we already know we are doing a tradeoff on the security
part here and that we'll fix it with client certificates auth later on.

## Links

- [RabbitMQ access control
  documentation](https://www.rabbitmq.com/access-control.html)
