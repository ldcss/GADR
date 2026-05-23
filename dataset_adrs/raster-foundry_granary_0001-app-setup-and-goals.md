---
id: adr-0001-app-setup-and-goals
title: 1 - Application Setup and Goals
---

# Context

We need to create an application without a dependency on Raster Foundry that has
the following capabilities:

- run models on imagery
- kick off model runs when it learns about new imagery
- run models without knowing anything about the content of those models
- summarize past model results
- allow users to respond to model run events

Additionally, we'd like the application to meet several design goals that aren't
core to the pursuit of those features:

- we should deploy continuously
- infrastructure should be kept as light as possible

The main question this ADR seeks to answer is how the API works and how
communication between the external world and the API and the API and the model
runner will work. This ADR will not attempt to answer questions of what a user interface
should accomplish, since that is not germane to the short-term (three month-ish)
uses we envision for this project.

## Specific Components

### Summary

The datamodel for the application includes three core entities, modeled here as
scala case classes without imports (and without bookkeeping fields like `id`):

```scala
// An area of interest
case class AOI(
  // the geographic bounding box imagery must intersect with
  geom: Projected[Geometry],
  // the largest acceptable ground sampling distance for new imagery
  targetResolution: Double,
  // required wavelengths that some of the image's bands must overlap
  wavelengths: List[Double],
  // what model this AOI is associated with
  modelId: UUID
)

// A model
case class Model(
  // the name of the model
  modelName: String,
  // which job definition to use to run predictions using this model
  // the container can't be overridden for a job definition, so we must
  // know this at job submission time
  jobDefinition: String,
  // a description of the prediction command, to which a new image and
  // a notification endpoint can be appended
  command: List[String]
)

// A model run result
case class Prediction(
  // the model that this prediction is for
  modelId: UUID,
  // the AOI that this prediction is for
  aoiId: UUID,
  // an absolute uri for GeoJSON holding the results of this prediction
  uri: URI
)
```

`Model`s will be renamed to something less overloaded for developer sanity at
some later date.

### New imagery from the outside world

When new imagery becomes available from the outside world, this application will
need to match it against models that are interested in that kind of imagery. This
requires tracking some kind of metadata about the incoming imagery. We
developed a fairly complex datamodel in Raster Foundry that tracks information about
imagery, including component files for that imagery and band-level information.
However, we are not a spec, and to the best of our knowledge no one relies on the
Raster Foundry datamodel to describe what imagery updates look like.

Instead, the API will demand that incoming imagery adheres to the [STAC electro-optical](https://github.com/radiantearth/stac-spec/tree/master/extensions/eo)
spec extension. There are several reasons to prefer using STAC for a datamodel.
These include tapping into ongoing work in the geospatial community to standardize
data exchange, making validation easier for anyone hoping to rely on this API,
and reusing our own work around a type-safe STAC datamodel in `geotrellis-server`.

### Running models against new imagery

`POST`ing a new image to the API will cause that image to be matched against
available models. A `model` is some function from raster to raster, raster to
geojson, or raster to number. For simplicity, we'll start with the raster to geojson
case, since it will save us some complexity on figuring out what kinds of
contracts we need to enforce for the other kinds of models and is sufficient for
object detection, chip classification, and semantic segmentation tasks.
`Model`s know what sorts of imagery are acceptable for them to obtain meaningful
results:

- an array of bandwidth requirements
- a minimum spatial resolution
- an `AOI`

We can determine this information for any incoming imagery that adheres to the
`eo` spec using band information.

`Model`s also need to know their own requirements to run. In particular, they
need sufficient information to be able to fill in a `SubmitJob` request for `AWS`
Batch. This includes resource requirements, a docker container accessible from
within the hosting AWS account, a compute environment name, and a command to run.
We require `model`s to carry this information to avoid having to infer it or
guess at it based on heuristics.

Once we identify that a `model` should run against an image, we'll kick off an
AWS Batch job with the model's parameters. The `model`'s command _must_ accept a
STAC item with the `eo` extension as its last parameter.

An important security concern is that the compute environment for running models
must be in a VPC with general internet access (or at least a gateway to make POST
requests to the application), but _without_ access to the database, to prevent
users, even users who've somehow compromised the database credentials, from
executing arbitrary code. If we as a team take responsibility for deployment
code, we should make sure that the resulting configuration passes this check.

### Notifying the API

Since `model`s will be run in some asynchronous workflow, they'll need a way to
notify the API. The form that notification should take is a [STAC item with the labeling extension](https://github.com/radiantearth/stac-spec/tree/master/extensions/label).
Reasons to lean on STAC here are similar to the reasons for leaning on it for new imagery. The API will accept a `POST` to a particular model
that contains a STAC item with an asset that points to predictions on the new im
agery.

It's possible that future work could allow discrimination between predictions th
at need time to run an asynchronous process and models that can do synchronous
prediction. Since we don't know this is necessary or even possible, we'll assume
for now that all predictions happen asynchronously and that all updates to the
Granary API will happen via a later `POST` request.

### Notifying end users

When we create `model`s, we will also create AWS Simple Notification Service
topics for those models. For our purposes we can think of these as an
inexhaustible resource, since each AWS account is allowed 100,000 topics. At a
time in the future when we think we are in danger of going over that limit we
can think about a new strategy or ask for a service limit increase.
Whenever a model is updated -- either a new prediction run has been kicked off,
results are available, or metadata about that model has changed -- we'll send
an event to the SNS topic for that model. The application will be deployable
in any AWS account (including a client's account), so we assume that clients
also have the ability to subscribe to those SNS topics and can subscribe
to notifications.

### Impact of continuous deployment

There are several consequences of the choice to aim for continuous deployment:

- Continuous integration checks passing on a PR _must_ mean that the branch is
  safe to deploy. This will require more care around migrations than usual and
  a more thorough exercise of the application in tests than we have in Raster
  Foundry. As long as this repository is just an API, that probably means
  generative testing of workflows modeled through API interaction both for
  correctness and performance regressions. I believe that we already have the
  tools and expertise on the team to do this.
- The application should also include smoke tests. Smoke tests will be a new
  feature of CI for us. We should be able to rely on the small application scope
  to ensure that we can define a reasonable standard for "not on fire."
- This repository probably shouldn't follow the `git flow` pattern, since the
  relationship between `develop` and `master` will be pretty
  confused (`develop = master` at all times). It is currently `develop` for
  consistency and to avoid the appearance of having made that choice final before
  this ADR has been reviewed.
- To enable the frontend to change without the backend's being ready, we will need
  to work out a sensible story about feature flags. We'll also need to enable the
  backend to change, even in breaking ways, without the frontend needing to know
  or care. A likely candidate to solve the latter problem is API versioning. Later
  ADRs should address implementation details for both of these problems.

### Impact of keeping infrastructure as light as possible

One example of how this motivation has already played out is the choice of
how to run models. We originally considered two possibilities for how to submit
a model run.

The first option was that we demand that consumers deploy some server somewhere
that accepts `POST`s of new imagery, responds with information about where the
output will be written, and eventually notifies the Granary API that it can go
fetch the imagery. The second option is what's written above.

While the option we chose requires more infrastructure -- another AWS service,
the creation of compute environments, job definitions, and roles necessary for
running batch jobs -- this is a case where the "as possible" part of the
motivation does a lot of work. Given that the service is designed for data
scientists easily to run predictions against new imagery, we had to weigh that
increase in infrastructure complexity against the presumed needs of potential
users. Since we believe this potential user's strike zone more likely includes
creating a docker container for running predictions than deploying a RESTful
model-as-a-service with its own (potentially) asynchronous task runner, we
chose for Granary to own this particular piece of infrastructure complexity.

A second example is in the choice of SNS as the notification service. An
alternative was to include webhooks in the application, where users would
tell Granary where they wanted notifications sent. This would have required
us to understand the availability characteristics of those endpoints as well
as to model in the application the possibility that users might want multiple
services to be notified. Instead, by pushing to SNS, we trade consuming a
small part of another AWS service's API for needing to model and respond
appropriately to an unbounded set of external resources. SNS allows us to
achieve a clear separation of concerns.

# Consequences

Because we chose continuous deployment, we'll need to:

- revert the default branch to `master`
- create a pull request template that expresses the constraints
  we've committed to by choosing continuous deployment
- set up CI to deploy on every merge to `master`

We'll also need to do standard startup work for a new Scala backend. Much
of that work was free, thanks to the azavea.g8 template. However, we'll
need to create a datamodel and `DAO`s and routes. We're good at this :tm:
now, so I don't think this needs much elaboration, and most of the details
will come out in implementation I think.

We'll also need to make a decision about where deployment code lives. Since this
is supposed to be open source and portable, I think it makes sense for us
to bring deployment into the open source repository. The downside to that is
that our open source tool will come with some vendor lock-in. On the other
hand, if deployment lives separately, our small open source tool will
probably never be deployed by anyone else.
