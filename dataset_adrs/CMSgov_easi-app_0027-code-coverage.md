# Add code coverage and threshold

**User Story:** [ES 653](https://jiraent.cms.gov/browse/ES-653)

In an effort to improve code quality and testing practices, we identified a need
for better visibility into current code coverage statistics. This ADR addresses
how we will approach code coverage reporting and thresholds in CI.

## Considered Alternatives

* Add code coverage, no threshold
* Add code coverage, with threshold below current coverage
* Add code coverage, with target threshold

## Decision Outcome

* Chosen Alternative: Add coverage, with threshold below current coverage, as
  this is a low-lift, first step to increase visibility into: (1) current
  code coverage and (2) potential drift if code coverage falls below a certain
  level. The specific threshold is out of scope of this ADR, and can be adjusted
  over time, with the goal of ultimately reaching a higher target threshold.

## Pros and Cons of the Alternatives <!-- optional -->

### Add code coverage, no threshold

* `+` Minimal impact to engineers, as builds will not fail if coverage falls
  below a certain threshold
* `-` Limited incentive to increase code coverage
* `-` Limited visibility into falling code coverage

### Add code coverage, with threshold below current coverage

* `+` Requires no immediate work to write more tests
* `+` Increases visibility into falling code coverage, as CI builds would fail if
  coverage falls below the threshold
* `+` Increases the incentive to maintain or improve code coverage
* `+` The threshold could be adjusted downward, as needed, so as not to block
  development work
* `+` As code coverage improves, the threshold could be increased
* `-` Reduces incentive to reach a target threshold

### Add code coverage, with target threshold

* `+` Most immediate incentive to improve test coverage
* `-` Writing new tests to meet the target threshold would require an unknown
  level of effort
* `-` Would block further development work until target threshold is achieved
