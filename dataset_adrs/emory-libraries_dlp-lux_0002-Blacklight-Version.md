# 2. Blacklight Version

* Status: Accepted
* Date: 2019-11-22

## Context
In order to facilitate work on dlp-lux, we need to make a decision about which verion of Blacklight to run.

## Decision
We will use Blacklight 7.

This allows us to avoid problems deploying the application, and sets us up for the future when Blacklight 7 is
supported by Hyrax.

This decision accepts that minor styling differences may occur between Lux and Curate.

## Consequences
We will use Bootstrap 4 rather than 3.

Because we will use Bootstrap 4, this may slow down tickets as the team becomes familiar with this version.

## Alternatives

### Using Blacklight 6
- PRO: This is the verion of Blacklight that Hyrax currently uses.
- CON: Deploying this verion requires significant development. The bug encountered is
  https://github.com/psu-libraries/psulib_blacklight/issues/95
- CON: Current Blacklight development is happening on version 7
