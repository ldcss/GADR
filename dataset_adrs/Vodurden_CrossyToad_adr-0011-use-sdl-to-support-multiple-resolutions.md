# ADR 0011: Use SDL to support multiple resolutions

Date: 2018-11-10

## Status

Accepted

## Context

We want to support a variety of screen resolutions, but we're planning to used fixed resolution
tiles to render the game.

Classic frogger is traditionally played on a 15x13 grid of tiles with some extra space vertical
space to draw the UI. We want to do something similar where the games internal coordinates
represent this grid but the renderer is able to map this to any resolution.

One way I've seen this solved is to use multiple coordinate systems: One coordinate system
reprersenting "Pixels on the screen" and one coordinate system representing "Physical locations
in the game world"

Most of the game logic would be implemented in terms of the "World Coordinates" which would
then be converted to screen coordinates by the renderer.

Another way to solve this is to target a specific resolution in our game logic and leverage
SDL2's "logical screen" feature to scale our game to any given resolution.

I attempted a spike of the world coordinates and found it added a lot of complexity to the
existing codebase. Given the extra complexity I'm going to stick with leveraging SDL2's
logical rendering feature to solve this problem. It might be something to revisit in the
future.

## Decision

We will use SDL to support multiple resolutions by targeting an internal screen

## Consequences

The screen and physics modules will need to be updated to support this change.
