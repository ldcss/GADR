# ADR 01: API Tech Stack

* Status: accepted
* Date: November 1, 2019 (retrospective)

## Context
The Zooniverse maintains numerous Rails APIs, mostly built between three and five years ago. These vary wildly in the amount of attention they've received and all use gems that are deprecated, unmaintained, or otherwise generally not a good idea in TYOOL 2019. As such, research was necessary into what was more modern, standardized API functionality.

Any solution would need to meet the following requirements:
* CRUD and serialization
* Pagination
* Filtration
* Authentication and Authorization

## Considered Options
Options in this context refers to a few different things. OOTB Rails is of course sufficient for building a full-featured API. However, we've come to expect certain features that lighten the cognitive load on both the app dev and the FE dev. I broke the question down into these possibilities.

#### API Format
* Plain straight JSON representations of resources
  * Pro: Straightforward to build, no extra parts required
  * Con: Another non-standard API in our stable
* JSON:API Spec
  * Pro: Follows a proven standard, lots of drop-in options for stuff that'd be manual otherwise
  * Con: Bit of a learning curve for both front and back end devs


### Option 1: Rails Only (Non-JSON:API)
Using mostly OOTB Rails gear, the API would be simpler and initially less featureful. That said, there are drop-in gems to provide some of the required features. This could be mean rolling something entirely freeform or building an internal schema validation system. Here is an example stack that could do either:
  * Auth: Pundit (this is a given across all options)
  * Pagination: Kaminari
  * Serialization: `.to_json` or Blueprinter for a internally-defined JSON schema
  * Filtration: Ransack or custom

Pros
* More straightforward to build, with the focus being on getting something working.
* Less overall complexity than the JSON:API spec.

Cons
* Still a lot of decisions to make about gems for pagination, filtration, etc.
* Another non-standard API in our stable.
* Our other apps dip into the JSON:API spec, by managing "links" (relationships) in some and manually implementing pieces of the spec in others. A new, totally bespoke interface seems like movement in the wrong direction.

### Option 2: JSON:API Spec
The JSON:API spec (jsonapi.org) is a schema standard that intends to normalize the way APIs are interacted with on the web. It's not perfect and it might not even be strictly necessary, but it allows for code to be written (for clients, gems, every piece mentioned up top) that all make the same assumptions. There are Rails solutions for this that exist everywhere on the spectrum between "full replacement of literally all controller code" and "helpers to deserialize".

I'll get to the internal differences below, but here's the upshot:

Pros
* Follows a proven standard.
* Lots of drop-in options for stuff that'd be manual otherwise, both client and server side.
* Abundant existing documentation for knowing how something should be acting. A client can surface bugs in server code by knowing what it should be expecting and not getting it.
* Learning/professional development, opportunity to catch up with the Rails world

Cons
* Learning curve.
* Potentially overkill for a project this size.
* Not the fastest route to a functional API.

With all that said, there are a few sub-options here:

#### Suboption 1: JSONAPI::Resources (https://jsonapi-resources.com/)
The big one in the space. This is a full drop-in replacement for...almost everything. It is designed such that your controllers are literally _entirely empty_, just inheriting from or including the gem's classes and boom, API. Gives you CRUD on everything (whether you want it or not) and handles all the interaction between the request and the model, pretty much.

#### Suboption 2: DIY JSON:API
Build a stack that does what it needs to do without the magic. A similar stack of gems as above (pundit, kaminari, ransack) and include some basic JSON:API-formatted serialization (fast_jsonapi). Seems like there's been a lot of churn in this space lately, though, and for the record, here's a few options that may seem fine at first blush but I ended up vetoing:

* ActiveModelSerializers: fully maintenance mode. No updates since mid-2018. This was the big one for a long time (several of our apps use it) but its own README says to look elsewhere.
* jsonapi-rb: Confusingly similarly named to the next option, it's the one that AMS points to as a first alternative. However, it hasn't seen a lot of activity recently, either, with PRs that have been open since 2017 and whole sections of the documentation labeled "TODO".

#### Suboption 3: jsonapi.rb (https://github.com/stas/jsonapi.rb)
I found this gem while I was doing research precisely I how I would do suboption 2. This is a >500 LOC gem that bundles together gems I was planning on using (primarily ransack and fast_jsonapi) and ties them together with some boilerplate code. That boilerplate does validation, error handling/formatting, getting data to/from Ransack for filtering/sorting, pagination (and links).


## Decision Outcome
At the end of the day it was difficult to not choose the JSON:API spec for a greenfield project. It was a balance of standardization vs. gadgetiness, basic non-DRY controllers on one end, GraphQL on the other. It is a spec that our front end devs are sort-of familiar with on account of our existing services' sort-of implementations of it. It gave me the opportunity to go down the rabbit hole a bit to learn what's out there, and some of those discoveries were surprising (ActiveModelSerializers is fully deprecated, who'd have guessed?)

With that in mind, I test drove a few of the suboptions. JSONAPI::Resources was more a framework, and while I'm sure that this relatively simple use case could be handled by it, I found myself getting hung up on straightforward questions because I wasn't sure I was using all of the magic correctly. This definitely seemed like overkill for what I wanted to accomplish. Furthermore, all of that magic and extra (required) documentation reading would make it that much more difficult to onboard someone new to work on this app.

In the end, I decided to go with jsonapi.rb. It leans on existing, popular tech to do the hard stuff (fast_jsonapi and ransack for serialization and filter/sort, respectively). And pretty much everything else it does is stuff that I'd have to implement manually. This way, though, I can see exactly what it's doing, how it's being done, and override it if necessary. There's no sorcery or empty controllers, just simple classes/methods that are clear and extendable.

I even fixed an example in the README and my PR was merged a couple hours later, so it's certainly active. That said, it would be a relatively straightforward process to disentangle this gem entirely from the rest of the app by just grabbing a few of the necessary classes out of its /lib and throwing them into the app's.