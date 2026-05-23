# Build frontend static files and deploy to AWS s3

The EASi frontend is built in React.
It is common practice to build the static assets for the
React app and host them somewhere highly available.

We'll want them to be easily accessible and easy to integrate
into our architecture.
Preferably we would manage the CDN or file server in
Terraform along with our other infrastructure configuration.

## Considered Alternatives

* *Build static files and put them in Docker image with backend*
* *Build frontend files and put it in Docker image by itself*
* *Build static files and serve them from S3*

## Decision Outcome

Chosen Alternative: *Build static files and serve them from S3*

This does mean we'll need to configure the web server in a
way that allows the end user to directly refer to the static
files in s3.

## Pros and Cons of the Alternatives

### *Build static files and put them in Docker image with backend*

* `+` Everything can be built and tracked in one container
* `+` Simpler deployment/CI workflows
* `+/-` Tightly couples the frontend with the backend
* `-` Docker container could get bloated

### *Build frontend files and put it in Docker image by itself*

* `-` Will be annoying to serve from the backend
* `-` Why build a container just to ship files around?

### *Build static files and serve them from S3*

* `+` S3 can be managed in Terraform
* `+` Truss knows how to configure this
* `+` Truss knows how to configure s3 for this
* `+` If this doesn't scale well, we could put Cloudfront in front of it
* `-` We'll have to do some work to make sure thee backend can serve it

## References

* [create-react-app prod build documentation](https://create-react-app.dev/docs/production-build/#static-file-caching)
