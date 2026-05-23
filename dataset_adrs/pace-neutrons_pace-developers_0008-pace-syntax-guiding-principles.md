[<-previous](0007-developer-scripts-storage-location.md) | [next->](0009-brille-integration.md)

# 8. PACE Syntax Guiding Principles

Date: 2020-Oct-19

## Status

Proposed


## Context

Whilst the core framework of PACE is the Horace (and Herbert) projects,
PACE involves many other codes, including [Euphonic](https://github.com/pace-neutrons/Euphonic),
[Brille](https://github.com/brille/brille) and [SpinW](https://spinw.org).
The way in which these programs interact with each other is presently unclear.
Furthermore the programs are written in several different languages.
In this ADR we propose some guiding principles in the design of the interfaces
between the programs or components which make up PACE.
This was discussed at a meeting whose
[minutes are here.](https://stfc365.sharepoint.com/:w:/r/sites/PACEProject/Shared%20Documents/Meetings/PACE-General/pace_syntax_meeting1_minutes.docx))

## Decision

The guiding principle for PACE-supported programs is **commonality**.
That is, interacting with the different programs of PACE should be **seamless**
to the user, and the user interface presented to them should be **uniform**.

The uniform interface means that function names and how users specify parameters
or arguments to functions in Matlab and Python flavours of PACE should align
as closely as possible.

## Consequences

There are several implications stemming from this guiding principle:

* There should be a single downloadble distribution which bundles all the 
necessary components (presently: Horace, Euphonic, Brille and SpinW).
* User syntax should follow the same format for each program,
and should be similar between Matlab and Python interfaces.
Specifically the same method and keyword names should be used.
* Syntax should be "Pythonic" (prefer keyword to positional arguments;
reasonable defaults for as many input arguments as practicable);
This applies to both Matlab and Python interfaces,
since the end goal is to migrate entirely to Python.
* Since the Matlab and Python *languages*'s argument syntax are not a superset,
exactly what (sub-set) of syntax PACE should use should be clearly defined
in a separate architectural decisions record.
* In the mean time, there should be both Matlab and Python interfaces for 
all functionalities (including handling polycrystalline/powder data).
* There should be uniform API for interactions between the different programs
(and with external third party programs).
