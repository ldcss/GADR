# 2. Use docker for 12factor app goal

Date: 2020-05-20

## Status

Accepted

## Context

One of the main goals I'm interested on is in to provide a 12factor app
 architecture to the solution.

etcd is a daemon that runs using:

a. environment variables or arguments in command line
b. config-file

All are valid for a 12factor app, but which is faster/better to implement?

I have read most of etcd invocations use command line arguments, but that's not
 going to work fine with Docker.

I can create a config file in a volume and map it from the docker container in
 runtime.  That is how it should work in kubernetes using config maps.

But for something more 12factor alike, like in heroku, I would rather prefer to
use ENV VARS.  Etcd has a good support for them.


## Decision

I'm going to try first with a config file, and then I will try to inject env
 vars through a docker env-file option.

As I want to create a three node cluster, I would need three env_files... Umm.

## Consequences

To support SSL encryption I need to set the CA certificate as well as the
 server files from a volume.  I don't like that as then I should mount a volume
 and manage it.  It would be better if the certificate and key could be 
 available as env vars (I have done it before).
