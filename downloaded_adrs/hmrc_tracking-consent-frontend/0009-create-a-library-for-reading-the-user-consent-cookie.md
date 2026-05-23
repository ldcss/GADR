# Create a library for reading the user consent cookie

* Status: accepted 
* Date: 2021-03-16

Technical Story: PLATUI-1027, PLATUI-1064

## Context and Problem Statement

Tracking consent stores cookie consent information in a userConsent cookie as URL-encoded JSON. This information is available
to frontend microservices in Javascript running in a user's browser and in the request headers passed to the Scala 
Play controllers running on the server-side.

Before frontend services can interpret the cookie, they need to decode and parse it using a Scala JSON library. They also need
to apply some business logic to ensure in cases of uncertainty, the user is, by default, assumed to have rejected cookies.

For Javascript code, we propose to make the existing UserPreferences object available in the window object. This will mean
services integrating with tracking consent will have a method available to them for parsing the cookie using the latest
business logic. Additionally, they will have a method for subscribing and being notified about changes to cookie preferences in real-time.

For Scala code, the situation is more problematic. Services will only have the raw userConsent cookie itself passed down in the `Cookie` header.
To avoid teams having to copy and paste substantial quantities of Scala boilerplate replicating the existing Javascript logic 
across services, should we look to centralise this logic so it can be more easily maintained across the platform and if so how?

Ideally we would like a Scala controller to be able to do something like:

```scala
  private val themeCookie = Cookie(name = "theme", value = "dark", maxAge = Some(365.days.toSeconds.toInt))

  private def allowedCookies(implicit request: RequestHeader) =
    if (userPreferences.preferences.settings) Seq(themeCookie) else Seq.empty

  val termsAndConditions: Action[AnyContent] = Action { implicit request =>
    Ok(termsAndConditionsPage()).withCookies(allowedCookies: _*)
  }
```

## Decision Drivers

* the need to keep repetitious boilerplate to a minimum, with changes needed of the order of a single line code change.
* the need to centralise the maintenance of the cookie reading logic, so it is easier to roll out changes
* the importance of having loosely coupled microservices and avoidance of unnecessarily introducing additional hard 
networked dependencies into microservices
* the need for simplicity and for the fewest number of moving parts
* the preference for not introducing a requirement for microservices to add additional libraries 

## Considered Options

* Option 1: Add the needed logic to play-ui and play-frontend-hmrc
* Option 2: Add the needed logic to bootstrap-play
* Option 3: Create a micro-library to contain the logic, with the intention that this would be added to one of the
above libraries as a transitive dependency
* Option 4: Create a hosted API to decode and an accompanying client library
* Option 5: Do nothing

## Decision Outcome

Chosen option 3: because it meets most if not all the above criteria.

### Positive Consequences

* Services can determine acceptance or rejection of non-essential cookies in a single line of code.
* Changes to the cookie parsing logic can be rolled out relatively easily by #team-plat-ui
* Consuming services do not rely on any additional networked dependencies
* No additional libraries would be needed (assuming the micro-library is added to play-frontend-hmrc or bootstrap-play)

### Negative Consequences

* Any version change to the userConsent cookie has the potential to break functionality relying on non-essential cookies
in consuming services. We may need to look at introducing the ability to have the concept of minor versions or only increment the version for breaking
changes e.g. removal or change to the meaning of a cookie type.

## Pros and Cons of the Options

### Option 1: Add the needed logic to play-ui and play-frontend-hmrc

* Good, because play-ui and play-frontend-hmrc already has knowledge of tracking consent
* Bad, because the logic will have to be duplicated across two libraries.
* Bad, because domain/business logic arguably doesn't live in a frontend component library

### Option 2: Add the needed logic to bootstrap-play

* Good, because bootstrap-play already has some knowledge of cookies
* Bad, because we would need to introduce knowledge of tracking consent into bootstrap-play. We already have such knowledge
in play-ui, play-frontend-hmrc and tracking-consent-frontend. See [Law of Demeter](https://en.wikipedia.org/wiki/Law_of_Demeter)
* Bad because bootstrap-play is not owned by #team-plat-ui, and this would hamper our ability to roll out changes
to the cookie reading logic as it would require approval by another team.

### Option 3: Create a micro-library to contain the logic

* Good, because #team-plat-ui can own the new library and make changes at the same time as changes to
tracking-consent-frontend
* Good, because it defers the decision of which library to transitively add it to allowing us to proceed with implementation. It keeps open the option to add to either bootstrap-play or play-frontend-hmrc/play-ui at a later date.
As a fallback we can advise teams add it on its own.
* Good, because it's a simple solution and easy to implement and rollout.

### Option 4: Create a hosted API to decode and an accompanying client library

* Good, because we can potentially roll out changes centrally. However, it's likely any change to the API would require
an update to the client library too.
* Bad because it introduces the need to host and maintain a backend microservice, which would be expensive in terms of 
ongoing running and maintenance costs, and would substantially increase complexity and the number of moving parts.
* Bad because it introduces tight coupling between microservices
* Bad because it complicates local development, teams would need to spin up another dependency using service manager.
* Bad because we would likely still need to create a library for it to simplify integration.
* Bad because it's unlikely it would be achievable in the needed timescales.

### Option 5: Do nothing

* Good, because it would require no further technical development
* Bad, because teams would need to introduce substantial boilerplate into their services
* Bad, because any bugs in the boilerplate would be difficult to fix
* Bad, because it would be extremely difficult to roll out changes to the business logic across the platform
