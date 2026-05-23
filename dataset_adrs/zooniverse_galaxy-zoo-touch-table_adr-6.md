## ADR 6: Choosing a Test Framework
July 26, 2019

### Context
The app needs tests. This is a must. Although test driven development is best, the app added tests after development began to test logic and encourage future changes do not break functionality. It would be best to test all aspects of the MVVM architecture, but view models are where the majority of the app logic lives.

### Decision
Several testing frameworks exist for .NET apps, with the main three being xUnit, NUnit and MSTest. The app uses xUnit to test view models, but any of the other two frameworks would've also been suitable. I chose xUnit because the testing syntax looked cleaner, the framework was a bit newer, and I found some nice tutorials that recommended xUnit above the other two. Perhaps most importantly, I wanted to get started with testing instead of spending too much time debating the merits of which one to chose.

Perhaps just as important as which testing framework to use is which mocking package to use when faking API or other function calls in my tests. For that, Moq seems to be the clear winner. It's easy to find documentation online about using Moq with each testing framework.

### Status
Accepted

### Consequences
Getting started with testing is an undertaking, and it is very easy to let tests fall by the wayside when the touch table has a deadline and new features need to be added quickly. However, many xUnit tutorials seem incomplete and only test the view models. I'm curious if this is a sufficient amount of test coverage.

_In Retrospect:_ Unfortunately, I added tests later in the development process, and that caused some unnecessary delay while I was restructuring the architecture. This could have been avoided if I was a bit more familiar with how [Moq](https://www.nuget.org/packages/moq/) worked from the outset of building the app. I also had to explore using [Unity](https://www.nuget.org/packages/Unity/) to make sure dependency injection was in place for my unit tests. For more information in using Unity, refer to the `ContainerHelper` class in the `Lib` folder of the app.
