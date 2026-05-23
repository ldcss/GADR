<!-- https://github.com/joelparkerhenderson/architecture_decision_record/blob/master/adr_template_madr.md -->

# Geometry Shaders

* Status: TBD
* Deciders: [@lithiumtoast](https://github.com/lithiumtoast)
* Date: 2020-08-01 <!-- YYYY-MM-DD when the decision was last updated -->

Communication: https://github.com/craftworkgames/Extended/issues/1

## Context and Problem Statement

Should `Extended` support geometry shaders?

## Decision Drivers <!-- optional -->

* Metal does not support geometry shaders.
* Performance of geometry shaders implementations are not consistent accross hardware vendors.
* Performance problems when geometry shaders are generating primitives that are to be stored in slower access mediums off chip.
* Another stage in the graphics pipeline which is competing for resources which could effectively be used somewhere else such as the vertex or fragment stage.
* The practical function of geometry shaders can effectively be done instead using vertex shaders with advanced techniques, compute shaders, tesselation, or instancing. 
* MonoGame does not support geometry shaders resulting in some, if not most, developers who are not unfamiliar with how geometry shaders work or even their purpose.

## Considered Options

* Do not support geometry shaders.
* Support geometry shaders, but only allow their use for specific graphics APIs.
    - Use a "feature flag"; the developer would be responsible for deciding whether geometry shaders are to be enabled or available for *their* app on the desired target platform and hardware.

## Decision Outcome

None taken yet.

## Links <!-- optional -->

* [Vertex Shader Tricks by Bill Bilodeau at GDC 2014](https://archive.org/details/GDC2014Bilodeau)
* [A Fistful of Frames by Klonan & posila at the Factario (video game) blog](https://factorio.com/blog/post/fff-251)
* [Why Geometry Shaders Are Slow (Unless you’re Intel) by Joshua Barczak](http://www.joshbarczak.com/blog/?p=667)