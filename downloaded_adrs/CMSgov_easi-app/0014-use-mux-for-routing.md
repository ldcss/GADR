# Use gorilla/mux for Routing

We need a way to serve routes so that we can create an application with functionality
that is useful for the front end. A router is helpful for handling multiple dynamic
endpoints, each in their own unique way and mass handling endpoints. This is helpful
for developers to iteratively add new API endpoints, and ultimately ensures faster
delivery to our end users.

## Considered Alternatives

* [gorilla/mux](https://github.com/gorilla/mux)
* [gin-gonic/gin](https://github.com/gin-gonic/gin)
* Use the Standard Library Only
* Write our own routing

## Decision Outcome

* Chosen Alternative: [gorilla/mux](https://github.com/gorilla/mux)
* We've decided that gorilla/mux is the right solution
as it is maintained by [Gorilla Tool Kit](https://www.gorillatoolkit.org/).
It handles routing in a way that conforms to golang best
practices. Truss has used other Gorilla tools before.
* This also lets us follow more common API patterns in
golang as described in
[this blog post
](https://medium.com/statuscode/how-i-write-go-http-services-after-seven-years-37c208122831)

## Pros and Cons of the Alternatives <!-- optional -->

### [gorilla/mux](https://github.com/gorilla/mux)

* `+` Truss has used gorilla tools before
* `+` Allows us to follow well-known golang practices
* `+` Been tested on other projects
* `+` Allows for a complex pattern matching on routes
* `-` Requires importing a package

### [gin-gonic/gin](https://github.com/gin-gonic/gin)

* `+` Has a lot of structure for many aspects of building out a golang application
* `-` Doesn’t use go standard lib patterns like `HandlerFunc`
* `-` Doesn't follow a lot of well-known golang practices
* `-` Has more features than we need (including logging, validation,
rendering, middleware, let's encrypt support and more)
* `-` Requires importing a package

### Use the Standard Library Only

* `+` No package imports or dependency locking
* `-` It only allows for static routes.

### Write our own routing

* `+` We get exactly what we want and need
* `+` No package imports or dependency locking
* `-` We have to maintain and handle any
security implications
* `-` Requires upfront work to build out features we want
