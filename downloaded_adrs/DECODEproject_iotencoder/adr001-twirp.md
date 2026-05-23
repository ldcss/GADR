# ADR001: Using Twirp to implement Datastore API

## Context

This project is a component within a project called DECODE, which is a
European Commission funded project which aims to explore and pilot new
technologies that give people more control over how they store, manage and
use personal data.

The specific subtask this project belongs to is an Internet of Things (IoT)
pilot which aims to demonstrate an architecture by which individuals retain
autonomy over data collected and published by IoT devices within their homes.

The agreed architecture for the pilot requires the implementation of three
independant components which together provide a mechanism for:

1.  registering and claiming ownership of an IoT device
2.  creating encrypted stream of data from the device
3.  providing a mechanism for storing this encrypted data somewhere
4.  provide a mechanism for allowing users with the correct decryption keys to
    download and decrypt saved data.

The components required to do this are as follows:

1.  An encrypted datastore - must be able to persist encrypted data to robust
    storage, and then allow that data to be retrieved by clients, who can then
    decrypt and read the data provided they have the correct key.
2.  A stream encoder - must be able to subscribe to raw events published by
    the IoT device, encrypt that data using encryption keys supplied for the
    device, and then write these encrypted events to the datastore.
3.  A device registration service - must be able to allow users to claim a
    device or devices, and then create encrypted streams for those devices.

Because DECODE is explicitly attempting to provide tools that can work in a
decentralised way, the decision has already been taken to implement the above
functionality via the separate components described above, so this decision
record is not about that; rather here we are just proposing a technology we
can use to expose and implement the API for the datastore, such that it is
easily usable by other components within the system.

### Constraints

* Components must support running on distributed nodes, meaning all
  communication between components must happen over the network using standard
  protocols.
* Components are to be operated by SmartCitizen once running in "production".
* Components are required to support a range of client languages, Go being used
  internally to the Thingful team, then perhaps one or more of Ruby, Python or
  JavaScript for Eurecat or SmartCitizen (TBD).

### Options

We identified the following options for the component:

* RESTful JSON over HTTP - stateless, v.simple to understand conceptually, uses standard
  HTTP, easy to integrate with other services, easy to test and debug via curl
  from the command line.

* JSONRPC (http://www.jsonrpc.org/) - lightweight remote procedure call
  protocol, uses JSON (readable), transport agnostic, can be tested/debugged
  via curl from the command line.

* Twirp (https://twitchtv.github.io/twirp/docs/intro.html) - lightweight RPC
  framework developed by TwitchTV, uses protocol buffers
  (https://developers.google.com/protocol-buffers/) to define messages and
  services, uses HTTP 1.1, natively exposes both protocol buffer and JSON
  endpoints, automatic generation of clients and server stubs, able to be
  tested from the command line via curl as all protocol buffer endpoints have
  a matching JSON endpoint that we can simply `POST` requests to.

* GRPC (https://grpc.io/) - modern RPC framework open sourced by Google, uses
  protocol buffers to define messages and services, allows automatic generation
  of clients and server stubs, requires HTTP 2.

* SOAP/XMLRPC - an XML based RPC framework, v.heavyweight. No one wants to use
  this.

## Decision

We will use Twirp to implement the datastore service's API.

Reasoning:

* automatic client generation from a single protocol buffer definition is a
  really nice feature.
* uses HTTP 1.1 so easier to integrate with existing infrastructure than GRPC
* natively exposes a JSON/HTTP endpoint meaning we have the same relatively
  easy CLI testing or debuggability as a standard REST API, but with the more
  efficient protocol buffer implementation that real clients should use.

A single repository has been created that will hold all protocol buffer
service definitions for the services being developed for DECODE. The location
of that repository at time of writing is:
https://github.com/thingful/decode-protorepo

The language bindings for clients generated from this repo will be pushed
into their own repositories via an automated script. These language bindings
will then be packaged in a language appropriate way so meaning they are easy
to use for any developers attempting to write code that interacts with the
service (i.e. Go will just use the repo, but for other languages the bindings
will be packaged into the expected format for the language and deployed to
the standard package index).

Given this project uses Go, the Go bindings for the datastore are available
here: https://github.com/thingful/twirp-datastore-go

## Status

Accepted.

## Consequences

* Using Twirp will allow us to automate the generation of clients for the
  following languages: Go, Python, Ruby and Javascript.

* Protocol buffers allow for more compact and efficient serialization of
  messages to be sent between components. In addition as clients are generated
  for us automatically there is no need to manually write tedious code to parse
  or encode data.

* Using protocol buffers may not be familiar to other consortium partners
  meaning there might be some confusion about how they will use the system. It
  is hoped that because we can provide them with a generated client library
  automatically then this will mitigate this.

* Twirp is a relatively new protocol and not supported by a Google level
  company so there is a risk that long term it might not be fully supported,
  however the project already has over 2000 stars on Github, and an active
  Slack channel indicating that there is a reasonable level of interest and
  community growing around the protocol.
