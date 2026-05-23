# Open Source CMS EASi Application Code

The EASi application team is beginning
to set up source code repositories.
Part of this process involves answering where the code should live
and who should have access to it.
[Open Sourcing](https://opensource.org/osd)
allows for the free sharing and modification of code
and provides a number of benefits to the EASi team
and outside community.

Note that for the purpose of this ADR,
we're referring to *just* the application code.
This does not refer to the infrastructure code
that is used to manage production environments
and cloud services.

## Considered Alternatives

* Open source application code
* Keep application code close sourced to CMS

## Decision Outcome

* Chosen Alternative: *Open source application code*

Open Sourcing the EASi application,
provides wins on many surfaces.
On an organizational level,
it increases CMS and federal government technology transparency
which fosters public trust.
Other federal agencies,
such as agencies within the Department of Health and Human Services,
will be able to benefit from EASi's success
within both their development and user communities.
While the EASi development team would remain maintainers
and deciders of code contributions,
open source code allows us
to accept community input and contributions.
Sharing code among our internal Truss Engineering practice
is also how we better our engineering discipline,
and ultimately better serve our clients.

While sensitive data could potentially be shared through public repositories,
modern security practices,
such secret storage separate of code,
can mitigate this risk.

Truss has had great success with this in the past,
one example being the
[MilMove Application Code](https://github.com/transcom/mymove),
which has already been a strong base
for bootstrapping the EASi application.

## Pros and Cons of the Alternatives

### *Open source application code*

* `+` Can easily share code
  with anyone,
  including CMS employees,
  Truss employees,
  or general software community.
* `+` Community contribute code.
* `+` Other agencies can copy, modify, and deploy their own EASi.
* `+` Community can audit security practices and report bugs.
* `+` Provides public transparency.
* `-` Possible sensitive data public commits.

### *Keep application code close sourced to CMS*

* `+` Less concern for what,
  possibly private,
  information resides in repository.
* `-` Hard to share code.
* `-` Hard to share documentation.
* `-` Code cannot be easily reused by outside community.

### Resources

* [Federal Source Code Policy](https://sourcecode.cio.gov/OSS/)
* [MilMove Open Source Repository](https://github.com/transcom/mymove)
