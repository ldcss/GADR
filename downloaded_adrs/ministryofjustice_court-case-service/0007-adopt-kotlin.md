# 7. Adopt Kotlin

Date: 2021-10-28

## Status

Accepted

## Context

Kotlin has become the language of choice for back end development within HMPPS Digital.   

## Decision

Adopt Kotlin as preferred language for new code within court-case-service. Where practical, migrate classes as we change them. 

## Consequences

- Developers can focus on key Kotlin skills which will be beneficial in the long term
- Ability to use Kotlin features including inherent null safety and immutability 
- Codebase will become a hybrid of Kotlin and Java code. There's some risk this will be detrimental to maintainability
- JPA presents some [challenges in Kotlin](https://www.jpa-buddy.com/blog/best-practices-and-common-pitfalls/) which if poorly implemented could negatively impact application stability

This last point is the main risk, but also one which as developers we're going to have to become comfortable with over time anyway for work on new projects. With this in mind, particular care should be taking when adopting Kotlin for JPA Entities, and data classes should not be used for this purpose. When in doubt, at the team's discretion it may be appropriate to continue using Java in preference to Kotlin, particularly where using Kotlin is considered risky or prohibitively difficult compared to the expected benefit.
