# 11. Prefer APT to CPAN for Perl libraries

Date: 2020-04-02

Status
------

Accepted (de facto)

Context
-------

We have a number of applications and servers that need numerous Perl libraries
installed. We have historically managed the libraries at a system level and
coordinated versions with application teams. While there are now compelling
options like [Carton](https://metacpan.org/pod/Carton), which allow an
application to manage and isolate its dependencies, most of our apps would
require changes to be ready to use something like this.

To aid in keeping the versions stable and ensuring that underlying system
libraries like OpenSSL are in sync, Debian packages many CPAN libraries at
specific versions for a release. These are still at a system level, but we
have an already-running process that would catch updates in the case of a
major bug fix or security release.

In service of completing OS and hardware upgrades, we are seeking primarily to
identify the dependencies and to be able to reproduce our application
environments. In the long term, applications are likely to be containerized or
otherwise placed under PSGI/Plack, where many of these concerns could be
isolated more readily. This decision is a record of current realities, rather
than a long-term position.

Decision
--------

Where possible, when installing Perl libraries at the system level, we will
use the Debian-released package. Where practical, we will use
[dh-make-perl](https://manpages.debian.org/stretch/dh-make-perl/dh-make-perl.1p.en.html)
to create local .deb packages from those in CPAN, but not released by Debian.
We will use `nebula::cpan` as a last resort.

Conseqeuences
-------------

Using Debian-released libraries means that we are limited to the versions
selected in their process. This could be a stabilizing or limiting force.
Producing our own packages requires additional maintenance and monitoring.
Using bare CPAN installs could result in different versions on different
systems, depending on when the installation happens.
