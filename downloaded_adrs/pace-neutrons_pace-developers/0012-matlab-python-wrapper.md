[<-previous](0011-use-mex-for-pyHorace-python-calls.md) | [next->](0013-light-python-wrapper-implementation-detail.md)

# 12. A Matlab wrapper for Python PACE projects

Date: 2021-Jan-01

## Status

Accepted


## Context

Both Euphonic and Brille are PACE projects with primarily a Python user interface (UI).
PACE, however, aims to provide both a Python and a Matlab UI to users,
and also to foster inter-operability between projects which are written both in Matlab and Python.
In particular, `pyHorace` ([prototype](https://github.com/mducle/hugo)) cannot use the 
[standard method](https://uk.mathworks.com/help/matlab/call-python-libraries.html) for Matlab to run Python code, 
where calls to Python from Matlab are prefixed with `py.` followed by the full module specification.
For example, `r = py.numpy.random.rand()` uses `numpy` to generate a random number.
This is because such a call causes Matlab to 
[automatically spawn](https://uk.mathworks.com/help/matlab/ref/pyenv.html) a dependent Python interpreter,
which can be either created within the same process as the Matlab interpreter (`InProcess`)
or in an external process (`OutOfProcess`).
`pyHorace` already runs within a Python interpreter and the compiled Matlab library *must* be loaded in-process.
Thus, if Matlab spawns a second Python intepreter with the default `InProcess` execution mode,
the two Python interpreters will conflict causing memory errors and a crash.
We can force Matlab to launch the dependent Python interpreter `OutOfProcess`
but this imposes a significant performance penalty
(extensive testing was not done but Brille+SpinW runs about 10x slower than with `InProcess`). 


## Proposal

So, we propose that the Matlab UI to Euphonic and Brille would be through a Python wrapper class.
There would be two implementation of this class.
One (used by the Matlab UI) would have calls to `py.*` internally, whilst the other
(used by the Python UI) would use the mechanism described in the [python interface design](../../python_interface/design).
Most importantly, no Matlab code which would be compiled would have references to `py.*`
which would otherwise cause a crash in `pyHorace`.

An important benefit of this Python wrapper class is that mimimal Matlab code would be needed
to expose Euphonic or Brille (or indeed any other Python program) to Matlab.
The [proposed wrapper](https://github.com/pace-neutrons/light_python_wrapper)
also handles data conversion and translation between Python and Matlab keyword arguments and some error checking.
Finally, the wrapper also exposes the `pydoc` documentation system
allowing users in Matlab to access the Python documentation transparently,
and to use tab-completion to access the properties and methods of the Python class or object.


## Decision

At a meeting on Jan 7 2021, the developers of `pyHorace`, `brillem` and `horace-euphonic-interface` agreed to accept this proposal.
`brillem` and `horace-euphonic-interface` will be refactored to use the `light_python_wrapper` proposed here.
The meeting also agreed implementation details which will be described in [ADR #13](0013-light-python-wrapper-implementation-detail.md).


## Consequences

The current [`horace-euphonic-interface`](https://github.com/pace-neutrons/horace-euphonic-interface/) and
[`brillem`](https://github.com/brille/brillem/) code would need to be refactored to use the wrapper.
Pull requests [for Euphonic](https://github.com/pace-neutrons/horace-euphonic-interface/pull/4)
and [brillem](https://github.com/brille/brillem/pull/4) will implement this refactoring.
