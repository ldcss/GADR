# Use SVG Icons

**User Story:** [EASI - 1515](https://jiraent.cms.gov/browse/EASI-1515)

Current implementation of icons within EASI mostly use Font-Awesome icon fonts.  The current USWDS standard recommendation, as well as popular community recommendation, is to use SVG elements to represent icons.

## Considered Alternatives

* Truss/USWDS SVG
* Font Awesome font icons
* Material Icon font icons

## Decision Outcome

* Chosen Alternative: Truss/USWDS SVG icons.

Initially there was browser compatibility issues that prevented EASI from moving forward with SVG icon implementation due to Chrome’s default rasterization.  By injecting the SVG element as a React component (by way of SVGR library), rasterization of otherwise IMG element is bypassed.  Truss' updated icon library converts SVG to SVGR.  We will use Truss' Icon component for displaying SVG as SVGR once updated uswds-react library.

## Pros and Cons of the Alternatives

### Truss/USWDS SVG

* `+` Stays in standard with USWDS guidelines and community best practices
* `+` Accessibility - SVG's are armed with built in semantic elements. SVG's are treated as an image and not as a text. Compatible with WAI - ARIA specifications
* `+` SVG’s have slightly better performance and stability
* `+` More control over style and animation
* `-` Less browser platform compatibility
* `-` More work to migrate from existing Font-Awesome icon implementations

### Font-Awesome Font Icons

* `+` Already in place/ubiquitous across EASI codebase
* `+` Easy to implement by nature of classes
* `+` Great cross platform compatibility
* `-` More rigid/less flexible in terms of styling and animation
* `-` Does not come equipped with native HTML tags for accessibility

### Material Icon font Icons

* `+` Easy to migrate from Font-Awesome to Material as both are implemented by means of classes
* `+` Great cross platform compatibility
* `+` Icons more closely aligned/copied directly from USWDS icon library
* `-` More rigid/less flexible in terms of styling and animation
* `-` Does not come equipped with native HTML tags for accessibility
