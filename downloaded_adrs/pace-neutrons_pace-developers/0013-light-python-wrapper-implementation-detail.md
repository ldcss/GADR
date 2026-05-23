[<-previous](0012-matlab-python-wrapper.md) | [next->]()

# 13. Implementation details for the Matlab UI for brille and euphonic

Date: 2021-Jan-10

## Status

Accepted


## Context

As described in [ADR #12](0012-matlab-python-wrapper.md),
PACE aims to provide both a Python and a Matlab user interface (UI) for all its constituent programs.
In addition, these programs should be able to interact with each other regardless of the user's environment.

That ADR decided that the Matlab UI for Brille and Euphonic (which currently only have Python UIs)
would use an interface library called [`light_python_wrapper`](https://github.com/pace-neutrons/light_python_wrapper).
A meeting between the developers of these programs on Jan 7 2021 also agreed the implementation details given here.

In addition, the meeting also decided that any computation or logic required for interfacing Brille/Euphonic
with other PACE programs should be written in *Python* so as to be accessible to both the Matlab and Python UI
without the need for compiled Matlab.


## Decision

* Any computation required for use with Horace or other Matlab programs would be implemented in *Python*.
* This Python code would be distributed as a separate module, to be installable using `pip`.
* The Matlab UI itself would be a pure interface layer (very little computation)
and be provided mainly by `light_python_wrapper`.
* `light_python_wrapper` will be moved to a separate repository, and used as a submodule in
[`horace_euphonic_interface`](https://github.com/pace-neutrons/horace-euphonic-interface)
and [`brillem`](https://github.com/brille/brillem).
* The continuous integration (CI) system would be updated to pull in the submodule for tests
* The CI system would also be used to build a ["Matlab Toolbox"](https://uk.mathworks.com/help/matlab/creating-help.html)
for distribution which would include `light_python_wrapper` (so users do not have to install it separately).
* Using this Matlab Toolbox `mltbx` file and uploading it to the github release allows it to be
[automatically published](https://www.mathworks.com/matlabcentral/about/fx/#Why_GitHub) by the File Exchange.


## Notes

A [pull requests for Euphonic](https://github.com/pace-neutrons/horace-euphonic-interface/pull/4)
implements this architectural design decision.
