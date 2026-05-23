[<-previous](0008-pace-syntax-guiding-principles.md) | [next->](0010-use-compiled-matlab-for-python.md)

# 9. Integration of Brille within PACE projects

Date: 2020-Nov-29

## Status

Accepted


## Context

[brille](https://github.com/brille/brille) is a library for computing symmetry operations
and linear interpolation within an irreducible part of the first Brillouin zone.
Whilst its symmetry operations functionality can be used stand-alone,
the interpolation functionality should be integrated with codes
which compute quantities in reciprocal space
(such as [euphonic](https://github.com/pace-neutrons/euphonic) and [spinW](https://github.com/spinw/spinw))
to make these programs more user friendly.

At present there are separate projects, [brilleu](https://github.com/brille/brilleu/)
and [brillem](https://github.com/brille/brillem/) to achieve this integration.
In both cases brille/X interface constructs a brille object from X and handles calling the X method(s) 
to determine the information required for brille's interpolation.
This relationship could be flipped if each X constructs its own brille object and
then uses it to perform interpolation.

## Decision

A [meeting](https://stfc365.sharepoint.com/:b:/r/sites/PACEProject/Shared%20Documents/Meetings/PACE-General/20201001_brilleX_Xbrille.pdf?csf=1&web=1&e=9XBRUe)
was held and the decision was made that the integration of the interpolation functionality of brille
should not be done by the external projects `brilleu` and `brillem`.
Instead, the interface between the calculator X and brille should be embedded within X which will
construct is own brille object and then use this to perform the interpolation.

## Consequences

* Code in `brilleu` will either be merged into `euphonic` or `brilleu` will be a dependency of `euphonic`
* This will allow `euphonic` to use `brille` to compute the density of states, the Debye-Waller factor or powder averaging.
* Code specific to `spinW` in `brillem` will be moved to `spinW` itself,
leaving a minimal `brillem` for Matlab users to access the functionality of `brille`.
