# Use linter for CSS

* Date: 2019-03-16

## Context and Problem Statement

While some form of linting as part of the development chain, seems to mostly [standard for JavaScript / Typescript](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results#js-linters) projects, [the same cannot be said when it comes to CSS](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results#css-linting) and its flavours (Scss, Less, ...).

Consistency for CSS selectors and rules can be hard to maintain in a project involving many team-members with varying CSS knowledge and experience.

In order not to rely solely on a manual review process, tooling may be used to support enforcing a defined CSS styleguide during the project lifecycle.

Especially when using a standard CSS styleguide like [BEM](http://getbem.com/introduction/), [OOCSS](http://oocss.org/) or [Atomic](https://github.com/nemophrost/atomic-css) or some extension / combination of those, tooling support for enforcing format rules, can be especially helpful for team-members not yet familiar with the notation.

## Considered Options

### Tooling support through linting

Existing solutions:
* no linting support for (S)CSS
* [stylelint](https://github.com/stylelint/stylelint)
* [CSSLint](https://github.com/CSSLint/csslint)
* [SCSS Lint](https://github.com/brigade/scss-lint)
* [SASS Lint](https://github.com/sasstools/sass-lint)

### CSS Styleguides
* none
* [BEM](http://getbem.com/introduction/)
* [OOCSS](http://oocss.org/)
* [Atomic](https://github.com/nemophrost/atomic-css)

## Choosen Option

[stylelint](https://github.com/stylelint/stylelint) together with [BEM ruleset](https://github.com/simonsmith/stylelint-selector-bem-pattern)

**Reasons**

### Stylelint

* Widest support for various CSS flavours (e.g., SCSS, Sass, Less)
* CLI tool available, i.e., can be automated in development setup
* best supported tool ([6329 stars on Github](https://github.com/stylelint/stylelint))
* [well maintained](https://github.com/stylelint/stylelint/graphs/contributors)

### BEM

* [well documented](http://getbem.com/)
* Rules are well defined and, once the rules are understood, it is obvious what a CSS selector must look like for any specific element or modifier
* tends to produce unique classes out of the box
* clear separation of concepts
* [widest acceptance within CSS community](https://ashleynolan.co.uk/blog/frontend-tooling-survey-2018-results#css-naming) (see answer: 'feel comfortable using')
* does not necessarily require tool support
