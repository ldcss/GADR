# 1. Fallback all pointer events to mouse events

## Status
Accepted

## Context
- Originally we wanted to use just PointerEvents API for capturing events because the API covers mouse and pointer inputs.
- Unfortunately Safari and iOS have very limited support. Safari does currently have an experimental API for it but the movementX and movementY properties are always 0. 
- MovementX/Y is a clean browser only method for determining distance without having to track previous coordinates.
- Mobile is a secondary concern for this app, but pointer events on desktop Safari is also unsupported :(


## Decision
All pointer event interactions have a mouse event fallback.

## Consequences
- Supporting both mouse and pointer is annoying because a mouse click will trigger both the pointer and the mouse event.
- Normally we could just do a simple check for pointer event support eg. `"onpointerdown" in window === true`. However, Safari's incomplete experimental implementation means such a detection will result in false positives.
  - As a work around we can check for "touch" event support. This appears to be behind pointer event support on the Safari roadmap.
- This will need to be reassessed in the future when pointer events are better supported.
- In the worst case scenario this will support all standard desktop browsers, android browsers, but NOT ios safari. 
