
# *Use react-testing-library in place of Enzyme*

**User Story:**  *[ES 809](https://jiraent.cms.gov/browse/ES-809)*

  Currently, our frontend test coverage is abysmal. It's sitting right around 30%.
  As a team, we've talked about being more intentional about writing unit
  tests, but often times unit tests were taking longer than the feature
  themselves. We realized that writing tests with [Enzyme](https://enzymejs.github.io/enzyme/)
  was making testing harder and confusing.

[Enzyme](https://enzymejs.github.io/enzyme/) was released in 2016 by AirBnb.
At the time, it was the gold standard for testing in the React ecosystem.
However by 2019, the React API has changed dramatically and support for
[Enzyme](https://enzymejs.github.io/enzyme/) has decreased with  [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/)
picking up the market share.

**Sources**
[Time to say goodbye - Enzyme.js](https://www.piotrstaniow.pl/goodbye-enzyme)

## Considered Alternatives

* [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/)

  PROS
  * It has the most support in the industry. This means we will have better
  resources to help encourage us to write more and better tests.
  * react-testing-library uses the DOM, which means no more confusing shallow vs.
  deep rendering.
  * Accessibility first: RTL provides simple ways to target elements by
  [role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)
  or [accessible name](https://www.w3.org/TR/accname-1.1/).
  It also has developer friendly ways to test keyboard actions and focus. This was
  all difficult to do in Enzyme.
  * Easy to use selectors

  CONS
  * Another library/API to learn
  * The transition from Enzyme to RTL might get messy. We'll have tests with two
  different libraries.

* Stick with Enzyme

## Decision Outcome

* [react-testing-library](https://testing-library.com/docs/react-testing-library/intro/)

We decided to go with React Testing Library for all of the reasons above.
We believe that it will encourage us to write more unit tests by making testing
easier.

## Pros and Cons of the Alternatives

* Stick with Enzyme

  PROS
  * It's what we use now. We have examples on how to do things.
  * Lots of resources online.

  CONS
  * Tests are hard to setup/write.
  * Online resources are outdated since RTL is the preferred testing library.
  * It's not the recommended testing suite by React.
  * Selectors don't account for accessibility.
