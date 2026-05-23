## ADR 5: Using the Messenger
July 26, 2019

### Context
Given the unique use case of having six classifiers on a single interface, there will likely be times the classifiers will need to communicate with one another and the app on a global scale. This is most apparent when considering notifications: where one classifier will have to send messages, subjects, and answers to another classifier. It simply isn't enough to have one parent view model communicate with a child and vice-versa. There should be a pub/sub technology used to remove some of the complexity in architecture.

### Decision
Although some WPF frameworks come shipped with a messenger, I will build my own simple messenger to better understand what is happening behind the scenes with a messenger. Building a messenger from scratch while also remove some reliance on a third-party framework.

### Status
Accepted

### Consequences
While a messenger does fulfill some needs in the app (inter-classifier communication), it is easy to become too dependent on a messenger. That said, a messenger should be used sparingly and only when there is no other way for the view models (or other components) to communicate with one another.

_In Retrospect:_ The messenger is incredibly useful for a multi-touch table. While I initially relied too much on the messenger, some later refactoring removed that dependence in lieu of more parent-child communication in the view models. I also found the messenger was helpful when some of the view models needed to initiate animation in a view due to an event firing.
