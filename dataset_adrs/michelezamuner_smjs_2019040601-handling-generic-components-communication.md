# Handling generic components communication


## Context

The easiest technical solution to let different layers communicate, for example adapters and application, is direct method calls, like injecting the presenter into the interactor, and let the interactor call methods on the presenter object. However, this is not the most generic case of communication, since it doesn't support the situation of concurrent components, or components running on different processes or address spaces.


## Decision


### Messaging

We can think of multiple adapters connecting to the same port at the same time. The easiest case is that of secondary adapters: if we have a `notifications` secondary port that is sending notifications, we might want to attach several different adapters, like a logging adapter, an email adapter, etc., to that port at the same time, so that when a message is available, all adapters will notify their recipients of it. If the secondary port is an interface construct of the programming language (like a `class` or an `interface`) demanding an object to be injected into it, then only one adapter can ever be available at the same time to be used by the interactor. Of course we could provide a "smart" adapter that multiplexes the calls to different other adapters behind the scenes, but we want to have a clean and generic solution.

The same situation can happen for primary ports as well, even though in this case we need to think of adapters running on different processes or threads (while the secondary port case could happen also when all components are sharing the same thread) because primary adapters are what run the actual execution thread. So, we want different devices to be able to use the same primary port at the same time, like posting a new order from a Web interface, and a Web API, at the same time. If the adapters and the application run in the same process and address space, we can still use direct method calls, of course handling all concurrency issues.

To understand what the most generic communication structure is, we have to remember that a port, for example a presenter, is not necessarily a programming construct, like a `class` or an `interface` construct, but it's the concept representing the set of messages that can be sent within a certain context, for example the messages related to presenting an output. In the most common case, these messages are implemented as public methods of a `class` or `interface` construct, but nothing prevents us to implement them with message objects, handled by a message bus.

If the port is just a set of messages, then what are adapters? They are the set of message handlers registered to respond to those messages. These handlers might very well be methods of old presenter objects: instead of being directly called by the interactor, they're called by the message bus this time, but conceptually it's the same thing (and this would allow to reuse the same components in different deploy situations, by just adding an intermediate bus). Also the fact that messages may not have any handler registered doesn't really represent a different situation, because also with direct calls we couldn't be sure that an actual presentation was performed, because we were just calling a method on an interface, and the concrete class injected could have been a null object!

So, we could think of direct procedure calls like a special case of the more generic messaging communication case: if components are running on the same address space, then we can simplify the design by using direct calls; if adapters are not accessing ports concurrently either, we won't need to handle the communication concurrently; furthermore, if there is only one presenter being used by the interactor, and the interactor is calling it only once, and not asynchronously, and there is only one presenter and view, then the interactor might as well just directly return the response, and the controller can just create the view and do the mapping of the response itself (which is just what happens in your regular web application).


### Micro-services

The general messaging communication protocol leads naturally to the micro-services deployment strategy. The message bus is called *API gateway* in micro-services parlance, and it represents the entire application API, as seen by the clients: thus, the API gateway is actually part of the application layer.

A simplified implementation of the API gateway allows interactors to be located inside the gateway component itself, while then each interactor would use the gateway to both get requests to the primary ports, and to communicate with secondary adapters through the secondary ports: both ports are sets of messages implemented by the API gateway. This strategy makes sense when each interactor doesn't need to be deployed on its own service, and this is usually the case since interactors are not called by other interactors, but just by the gateway. However, in some cases some interactor will need to be horizontally scaled, meaning replicated to bear a bigger load: in this case of course we want to deploy the interactor to its own service, and the API gateway would communicate with it through an internal protocol, instead of through a direct method call, even though conceptually there's no difference.

The API gateway is thus a surface enveloping all application components, and allowing them to communicate with the external world: primary ports would be connected with primary adapters, and secondary ports would be connected to secondary adapters.


## Status

Proposed


## Consequences

In the most generic design, communication between components happens via message bus.

It's possible to simplify the design in specific areas if the right conditions are met.
