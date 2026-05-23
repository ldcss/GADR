# ADR 3: Theming Framework

* [Table of contents](#)
  * [Context](#context)
  * [Decision](#decision)
  * [Status](#status)
  * [Consequences](#consequences)
  * [More reading](#more-reading)
  * [Updates](#updates)

## Context

To achieve a mature and robust design system, we must follow the top-notch front-end trends. The most famous movement right now is thinking about themes instead of customizable components. This way, we can create customizable layouts that can interact with different platforms optimally.

As you may think, doing so is extremely hard. So, we must choose a proper framework to make our lives easier.

## Decision

Among most frameworks, [ThemeUI](https://theme-ui.com/) stands out for the following reasons:

* It is incredibly light (only 19kb unpacked)
* It is highly customizable (we can use the `sx` props to use theme tokens without hooks)
* It is slightly opinionated (more than [styled-system](https://styled-system.com/) but less than [rebass](https://rebassjs.org/))
* It contains some common structures

We've not decided to use Rebass, since most of the community is already changing to ThemeUI, and also it allows us to do a more robust structure in our themes.

## Status

**DEPRECATED** _check [update 1](#update-1)_

## Consequences

Since we're not using MaterialUI or any other "complete" framework, we will develop many standard components (such as Dialogs, Drawers, and others). But, on the other hand, we can code those as we please.

---

## More reading

* [ThemeUI's docs](https://theme-ui.com/getting-started)

## Updates

### Update 1

After [business/ADR#001](https://github.com/budproj/architecture-decision-log/blob/main/records/business/001-reducing-initial-technical-complexity.md), we've decided to stop the development of a decoupled design system.
