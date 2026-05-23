# ADR: 0010: Support continuous and discrete input

Date: 2018-11-09

## Status

Accepted

## Context

We need to support both discrete and continous input.

Discrete input is the detection of an individual keypress. We need discrete input to support
movement in game menus, state transitions and other "one keypress one action" scenarios.

Continous input is the detection of the state of an input on an ongoing basis. We need continous
import to support linear movement in the game, notably the movement of the toad.

Currently we are using SDL to retrieve discrete input and we have no mechanism for continous input.

One option for implementing continous input would be to use the [SDL_GetKeyboardState](https://wiki.libsdl.org/SDL_GetKeyboardState) function from SDL. We could call this function every frame and
make the results available to every Scene for interpretation.

Another option would be to consume our existing input event stream which is fed from [SDL_PollEvent](https://www.libsdl.org/release/SDL-1.2.15/docs/html/sdlpollevent.html) and transition our own "InputState" based on the "KeyPressed" and "KeyReleased" events.

At the moment I prefer maintaining our own state instead of letting SDL do it as we can reduce the
number of possible key combinations we want to support through the type system.

## Decision

We will support continous and discrete input using the existing poll events architecture and
some new state machinery.

## Consequences

The input layer will need to be refactored again to expose both of these capabilities.
