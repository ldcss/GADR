# App Tech Stack

## Context and Problem Statement

I want to choose a technology stack that would allow us integrating into GoG Galaxy 2.0 ecosystem with ease, provide a rich modern-looking UI and be less familiar technology I could learn.

## Decision Drivers

* learning new technology
* should be a desktop standalone application
* being able to run GoG Galaxy 2.0 plugins
* being able to read GoG Galaxy 2.0 database (SQLite3)
* modern looking UI

## Considered Options

* WPF
* Windows React Native
* React
* Python + Tkinter
* Python + React (embedded)

## Decision Outcome

Chosen option: "Python + React (embedded)", because it allows for modern-looking UI while maintaining the Python connection to GoG Galaxy 2.0 ecosystem.

### Positive Consequences

* Rich UI tools.
* Ability to easily interact with (Python based) GoG Galaxy 2.0 plugins.
* Learning ability.

### Negative Consequences

* Additional complexity in repository, mixing frontend (React) and backend (Python) code.
* Might run into additional issues due to the need of running a server for a desktop app.
* Follow up: there needs to be some sort of launcher to run both backend and frontend.

## Pros and Cons of the Options

### WPF

* Good, because meant for desktop apps
* Good, because allows for modern-looking UI
* Bad, because known (less learning)

### Windows React Native

* Good, because meant for desktop apps
* Good, because allows for modern-looking UI
* Good, because allows learning React
* Bad, because the output is UWP app

### React

* Good, because allows for modern-looking UI
* Good, because allows learning React
* Bad, because not a desktop technology, hard to integrate into GoG Galaxy 2.0 client

### Python + Tkinter

* Good, because meant for desktop apps
* Good, because allows learning Python
* Good, because should allow for easy integration into GoG Galaxy 2.0 ecosystem
* Bad, because the UI looks outdated

### Python + React (embedded)

* Good, because allows for modern-looking UI
* Good, because allows learning Python
* Good, because allows learning React
* Good, because should allow for easy integration into GoG Galaxy 2.0 ecosystem
* Bad, because of added complexity runnin a server for a desktop application
* Bad, because of added complexity in the repository 
