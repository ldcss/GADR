# 6. Let the build step generate config for the client code

Date: 2020-11-07

## Status

Accepted

Extends [5. Minimize the amount of code that must be tested in the browser](0005-minimize-the-amount-of-code-that-must-be-tested-in-the-browser.md)

## Context

We want to minimize the amount of code that must be tested in the browser so
it's easier to build this thing.

We have to do some things in the browser:
 - listen for key presses
 - navigate to a new page
   - triggered by a key press
   - triggered by a click
 - open a model to prompt for parameters, then navigate to a new page
   - triggered by a key press
   - triggered by a click
 - keep track of where in the link tree the user is
   - display the appropriate links for that location
   - do appropriate things on key press for that location

It is possible to model the client as state and commands:
 - state
    - location
 - commands
    - change location
    - navigate to link
    - prompt for parameters then navigate to link

This can be configured with:
 - for a given location:
   - map key presses to commands
   - what to show?

And implemented with the following:
 1. render the appropriate HTML for the location
 2. prepare to execute commands:
   1. attach unobtrusive javascript event handlers for the rendered html (to
      handle clicks)
   2. listen for key presses; execute the appropriate command on press
 3. execute commands
   1. change location: update state & repeat these steps
   2. navigate: change the window location
   3. navigate with parameter: prompt for input and then change the window location

## Decision

Let the client code be configured with data in the following format (generated
by the build step)

```json
{
  "": {
    "html": "<ul><li>....</li>....</ul>",
    "keys": {
      "a": ["location", "a"],
      "g": ["navigate", "https://google.com"]
    }
  },
  "a": {
    "html": "<ul><li>....</li>....</ul>",
    "keys": {
      "n": ["navigate": "https://nifty.org/{PROMPT}"],
      "l": ["navigate": "https://lintish.com"]
    }
  }
}

```

## Consequences

### Client side
To test the client, we should have a sample config that covers the interesting
cases. We must check:
  - see the right list of links
  - do the following via key press and via mouse click
    - change location
        - see new list of links
    - navigate
        - see new web page
  - Esc key to navigate back
    - from child page: see previous list of links
    - from landing page: no effect
  - location stored in url hash so location persists on refresh
    - change location via mouse click, reload, see same content
    - change location via key press, reload, see same content

This isn't a trivial set of test cases, but it's less than if the configuration
wasn't prepared in such a convenient format.

Maybe I'll decide to automate these tests. I'll need to also run them manually
to check the overall experience.

### Build step
 - can test with approval tests
 - must keep the HTML quite simple
 - will need to decide how to merge the config and the HTML template at build
   time
