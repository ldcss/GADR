# Evaluate Existing React Component Libraries

## Background

Evaluation of existing libraries to see if there is a useful way to extend them to fit our goals. We are evaluating based on the following criteria:

- **Progressive enhancement**: All components support a usable fallback when javascript and css are disabled.
- **Meets core components list**
- **Minimal css compiled**
- **Open source**
- **Supports react**
- **Theme Supported**: Suports a theme that can be applied to all components
- **Themeable (Fully customizable css)**: Theme allows for custom css for all properties. The value of this is to meet the goal of having core components that are accessible and progressively enhance, which can then be themed to meet any design needs.
- **Tree shaking**
- **Well-maintained**
- **In use by large companies**
- **Accessibility**
- **Typescript**

## Findings

| Library                                                 | Progressive Enhancement | Meets core components list | Minimal css compiled | Open source | Supports react          | Theme Supported | Themeable (Fully customizable css) | Tree shaking | Well-maintained | In use by large companies | Accessibility | Typescript |
| ------------------------------------------------------- | ----------------------- | -------------------------- | -------------------- | ----------- | ----------------------- | --------------- | ---------------------------------- | ------------ | --------------- | ------------------------- | ------------- | ---------- |
| [Canvas-kit](https://workday.github.io/canvas-kit/)     |                         |                            | &#10004;             | &#10004;    | &#10004;                | &#10004;        |                                    | &#10004;     | &#10004;        | &#10004;                  | &#10004;      | &#10004;   |
| [Wix-style-react](https://www.wix-style-react.com/)     |                         |                            |                      | &#10004;    | &#10004; <sup>[1]</sup> |                 |                                    | &#10004;     | &#10004;        |                           |               | &#10004;   |
| [Reaviz](https://reaviz.io/)                            |                         |                            | &#10004;             | &#10004;    | &#10004;                |                 |                                    | &#10004;     | &#10004;        |                           |               | &#10004;   |
| [Reakit](https://reakit.io/docs/styling/)               |                         |                            | &#10004;             | &#10004;    | &#10004;                |                 | &#10004;<sup>[2]</sup>             | &#10004;     | &#10004;        |                           | &#10004;      | &#10004;   |
| [Grommet](https://storybook.grommet.io/)                |                         |                            | &#10004;             | &#10004;    | &#10004;                | &#10004;        |                                    | &#10004;     | &#10004;        | &#10004;                  |               | &#10004;   |
| [Elementalui](https://github.com/elementalui/elemental) |                         |                            |                      | &#10004;    | &#10004;                |                 |                                    | &#10004;     |                 |                           |               |
| [Rebass](https://rebassjs.org/theming)                  |                         |                            | &#10004;             | &#10004;    | &#10004;                | &#10004;        |                                    |              | &#10004;        |                           |               |
| [Rsuitejs](https://rsuitejs.com/)                       |                         |                            |                      | &#10004;    | &#10004;                | &#10004;        |                                    | &#10004;     | &#10004;        |                           |               | &#10004;   |

[1]: Dependency on [stylable](https://stylable.io/) requires additional configuration with some common nextjs setups.

[2]: Reakit has no opinion on styling, and could allow fully custom css, but we would have to add it (Not out of the box).

### Notes

- [Belle](https://github.com/nikgraf/belle) was briefly considered, but dropped after seeing it's lack of maintenance

## Decision

The critrion of fully themeable css will make it challenging to extend an existing library. While useful design, testing and accessibility practices can be re-used, we have chosen to incorporate what we can into our library as opposed to extending an existing library.
