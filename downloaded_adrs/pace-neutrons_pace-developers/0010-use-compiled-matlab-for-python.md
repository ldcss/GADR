[<-previous](0009-brille-integration.md) | [next->](0011-use-mex-for-pyHorace-python-calls.md)

# 10. Use Compiled Matlab library for Python users to run PACE

Date: 2020-Nov-29

## Status

Accepted


## Context

PACE is a collection of programs written in various languages including Matlab
and Python, but the aim is that *users* should be able to use either Python
*or* Matlab to run PACE programs.

Matlab has [built-in functionality](https://www.mathworks.com/help/matlab/call-python-libraries.html)
to call Python programs however the reverse is not true - principally because
Matlab requires a (paid-for) license to use.

Thus to allow Python users to call the current Matlab PACE codes
([Horace](https://github.com/pace-neutrons/Horace/)/[Herbert](https://github.com/pace-neutrons/Herbert/))
it should either be translated to Python or C++ and a wrapper to Python and Matlab created,
or the Matlab Compiler Runtime (MCR) toolbox should be used to "compile" 
`horace`/`herbert` for distribution as a Python package, as detailed
[here](../../python_interface/design/01_pace_python_high_level_discussion.md).
Using the MCR would also allow users to use Horace without a Matlab license,
whilst enabling us to leave the Horace code mainly in the Matlab language.


## Decision

The decision was made to use a compiled Matlab library for Python users to
run PACE.

This is because it was judged to be unfeasible to translate the `horace`/`herbert`
codebase to C/C++.


## Consequences

Consequences are discussed in detail in the design documents linked above,
and in further architectural decisions records and design documents to be
written as prototyping continues.

