# Firebase

**Status:** Accepted

## Context

We need a platform that can help us with the following requirements:

- Cross-platform connection to the input form: Information collection can happen through phone or tablet in real time or be entered into manually through a computer at a later stage. The database we use should be able to connect to all input media.
- Collate information of all types (text, videos, photographs, etc): When making observations out at sea, researchers capture pictures and videos along with textual information such as weather conditions and distance. Being able to bring together different types of data will greatly reduce post-collection maintenance efforts.
- Work around intermittent internet connection: Given the environmental conditions on a boat in the middle of the ocean, consistent internet connection is not a given. Thus, our tech stack must provide offline capabilities with minimal-to-no data loss.
- Inexpensive scalability: As they move into different forms of information collection such as drones, it is possible that the size of data becomes exponentially bigger than it is today. Thus, the datastore should not only be able to handle storage of that data but also does not put a cost overhead on BMMRO.

## Decision

Firebase is a mobile and web application development platform that is currently owned and maintained by Google.
We've decided to use Firebase because it offers a variety of services under the Google ecosystem that can be leveraged including hosting, databases, authentication, cloud storage, analytics, etc. along with beta features such as translate and email trigger. It also has a free plan that seems to be enough for our needs.

## Links

- [Firebase - Pricing plans](https://firebase.google.com/pricing)
