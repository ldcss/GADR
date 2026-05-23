# Make visual regression tests reproducible on jenkins

* Status: accepted
* Date: 2022-01-11

Technical Story: PLATUI-1475

## Context and Problem Statement

Jenkins's builds would fail if our visual regression test reference images for classic services were updated from images
generated on our local machines. We identified that the issue was because of different available fonts between systems.
So we needed a way for our tests for classic services to always have the same fonts available during visual regression
tests.

### Technical details

Classic Services are not built on top of our libraries, and instead of the GDS Transport font that the tracking consent
banner relies on they use a font called Open Sans. A copy of the Open Sans font is provided by classic services, but the
Open Sans font is not listed as one of the tracking consent banners preferred fallback fonts. So when someone views a
classic service, their browser will attempt to display the banner using Arial, or, if that's unavailable, the browsers
default sans-serif font.

On jenkins we've found the browsers used during visual regression tests do not have Arial available, whereas, on our
local machines, we will normally either have Arial available or we will have a different default sans-serif font. Which
means that jenkins isn't able to recreate the results of reference images created on our local machines, and we aren't
able to recreate locally the results of reference images created on jenkins.

## Considered Options

* **Option 1:** disable visual regression tests to avoid overhead of working around this problem
* **Option 2:** install the arial font for browsers used by jenkins
* **Option 3:** update our classic services fixture to include a copy of the GDS Transport font
* **Option 4:** get jenkins to use the same docker image we use locally to run visual regression tests
* **Option 5:** add Open Sans as a fallback font for the cookie consent banner

## Decision Outcome

Chosen option: **option 3**, because option 1 would only be desirable if we could not otherwise fix the problems and
were faced with continuing to use our current workaround, option 2 would potentially impact other tests relying on the
current behaviour of browsers used by jenkins, and option 4 -while being most correct- would be impractical for us
because of limitations to the way docker can be used on jenkins. Option 5 is listed but was outside the scope for
consideration as part of current work.

### Positive Consequences

* Where the visual regression tests are run will no longer vary which font the banner is displayed using, giving us
  reproducible screenshots with our current setup.

### Negative Consequences

* Captured test images for classic services aren't exactly as would display for a user, because for a user the banner
  would be displayed using either Arial or the users default sans-serif font. This isn't very consequential to us for
  the purposes of our tests.
* Operating system or browser text rendering could still impact reproducibility, but because we use docker locally that
  should not cause any problems.