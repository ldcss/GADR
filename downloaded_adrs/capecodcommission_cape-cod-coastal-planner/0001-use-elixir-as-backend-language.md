# 1. Use Elixir as Backend Language
Date: 6/18/2018

## Status
Accepted

## Context
Because this project is going to be delivered as a Beta project by the end of the year, it will be likely that its needs will grow as feedback from real users begins to filter in, as new ideas are conceived, new platforms are required, and as sources of funding are renewed. In order to accommodate these concerns, CHIP needs a simple, flexible, yet powerful backend that is well situated for both changes in feature requirements and changes in technology. 

## Decision
Elixir is a modern language built on the rock-solid foundation of the Erlang/OTP runtime which has over 30+ years of running highly critical systems with as little downtime as possible. While Erlang itself has a reputation of being arcane, Elixir introduces an elegant new syntax and many new features that have created a vibrant and enthusiastic following both commercially and within dev circles. Phoenix, the de-facto web framework for Elixir, capitalizes on the features of Elixir and Erlang/OTP to provide a very rich developer experience and the capabilities to develop any kind of app you could imagine: traditional MVC, REST, GraphQL, real-time streaming, etc. 

## Consequences
Some of Elixir's key benefits include:

- It's a functional and immutable language, which bring with it a host of benefits like
    - referential transparency
    - reduced cognitive load in understanding data flow
    - easier to write unit tests
    - eliminates an entire class of bugs that are introduced with mutable/OOP paradigms
    - allows for better optimizations by compiler because it can safely make more assumptions
- Is arguably the best language/platform for concurrent and distributed programs (ie: the Web!)
    - by using incredibly light-weight, isolated processes that can have thousands upon thousands running concurrently on the same machine (vertical scaling)
    - by instrinsically using the Actor model, each process can communicate with other processes on any machine within the network, or on a single machine with multiple cores, in a thread-safe manner (distribution & horizontal scaling)
    - by using Phoenix Channels and Presence (Conflict-free replicated data types) it can easily be used to build reliable distributed real-time systems 
    - by using Nerves it can be embedded into IoT devices and retain all its benefits to allow for sophisticated, modern IoT solutions
- Unique approach to fault-tolerance with it's "Let it Fail!" mantra
    - you can largely ignore exception handling due to the ability to use Supervisors, which are processes that you can utilize to monitor other processes and in the event of an exception, choose from a number of strategies to restart the process and its related processes in the last known valid state.
- It's highly performant, consistently delivering responses in microseconds, even under heavy load (think 2m+ concurrent websockets actively transmitting real-world data)
- It has an elegant syntax drawn from Ruby, and as such, many veteran Ruby programmers are moving to Elixir for the combination of that familiar syntax and improved horsepower.

Some things developers will need to be aware of:

- Though it's gaining lots of traction and has battle-tested underpinnings, it's still a relatively new language and ecosystem. Finding run-of-the-mill developers at the drop of a hat may be more difficult, but you'll also be more likely to attract better talent that may stick around longer if you can market to them and bear the longer hiring process.
- Deployments can be a little trickier, requiring some more manual tooling beyond a simple `git push master` style deployment, but are getting easier with tools like Distillery
- Being a functional, immutable language, developers familiar with the OOP and mutable data paradigm may have to make some more initial effort in order to successfully shift their mindset, and though they are well-defined, Elixir/Erlang/OTP have some unique software patterns that will need to be learned. The rewards of learning this paradigm, however, are most certainly worth the effort.
- Though unlikely, developers may need to learn a bit of Erlang to do more advanced things or if a library they want to use doesn't exist for Elixir yet.
