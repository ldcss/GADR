[<-previous](0010-use-compiled-matlab-for-python.md) | [next->](0012-matlab-python-wrapper.md)

# 11. pyHorace Matlab code should use a mex interface to call Python functions

Date: 2020-Dec-02

## Status

Proposed


## Context

`pyHorace` ([prototype](https://github.com/mducle/hugo)) is the proposed Python module for PACE
which packages the Matlab Horace/Herbert codes as a "compiled" library.
The Matlab code within this library needs to interact with Python codes in the host.
Specifically for fitting and model evaluation, Horace has to be able to call a user defined model function.
As the compiled Matlab library does not allow users to use their own `m-file`,
user model functions would have to be written in Python (or C/C++/Fortran - subject of a separate ADR).

However, the implementation of the compiled Matlab library is such that compiled Matlab functions cannot call
Python functions directly using the standard API. 
This is because the standard API for Matlab to call Python assumes that Matlab can spawn its own Python interpreter.
In `pyHorace`, this would clash with the user-launched parent Python intepreter and cause a crash.

[This design document](../../01_pace_python_high_level_discussion.md#-calling-user-defined-functions)
outlined two main methods for the compiled Matlab code to call a Python function.

1. Using a `mex` file.
2. Using a "reverse communications interface" (RCI).

In the `mex` method, a reference to the Python function is given to the `mex` file which uses the CPython
API to call that function (in Python) and then automatically converts (copies) the results to Matlab (`Array`) format.

In the RCI approach, the compiled Matlab program never explicitly calls a Python function. 
Instead whenever the Matlab code needs to call a Python function, the user instead calls a **Python** wrapper
which only exchanges data with Matlab. This is explained in detail in the [RCI section](#rci) below.
Because of the need to the wrapper, this is not a general purpose approach but requires code in each specific
instance where we want to employ it (e.g. in `multifit`).
This may prove too restrictive for integrating Brille.

Despite this, the RCI approach uses only the documented Matlab-Python API which should make it more stable and robust.
On the other hand, the `mex` option allows the current Matlab code to be used without modifications and is more flexible.
But, as it uses a `mex` file, unhandled exceptions in the `mex` file can lead to hard crashes.
In addition, `mex` functions _cannot_ use non-Matlab (non-`Array` types) data as input or outputs.
Thus all data must be converted to Matlab format from Python, and vice versa which involves at least one data copy.
This restriction means that not all Python functions can be supported by this method 
(e.g. those which return non-convertible types such as Python classes) 
except with special work-arounds as in the case of Brille.
This also means that the reference to the Python function cannot be passed directly to the `mex` function.
Rather, the Python code stores it in a global dictionary and the (string) key is passed to the `mex`.


## Decision

The decision was taken to use the `mex` method for compiled Matlab code to call Python functions.
This is because using the RCI approach would require extensive changes to the `multifit` and `SpinW` Matlab code to
handle the pyHorace use case.
Futhermore these changes would be incompatible with the Matlab interface which would result in two different versions
of the multifit `mfclass` and SpinW `spinw` classes.
On the other hand, using the `mex` approach, the current Matlab code can be used "as-is" in pyHorace.


## Consequences

User model functions written in Python (which includes Euphonic and Brille) cannot return non-convertible data.
That is, scalar values and standard containers (lists, tuples, dicts, numpy arrays) can be returned but Python objects cannot.
Instead, arbitrary Python objects may be handled using a global dictionary similarly to how function references are handled.
The current [minimum viable implementation](https://github.com/mducle/hugo/blob/master/src/call_python.cpp) can handle the
needs of the SpinW-Brille interface where Brille (Python) objects are passed to the (Matlab) SpinW methods, but would have to
be improved for more general usage.


## <a name="rci"></a> Reverse Communications Interface

Taking the example of `multifit`, we define a Python wrapper, which for concreteness we call `multifit_py`.
Instead of calling the Matlab `multifit` code directly, the user calls `multifit_py` and gives it a Python function reference.
`multifit_py` then calls a modified version of `multifit` which just performs the initialisation of the problem
and returns to `multifit_py` the initial parameters at which to evaluate the user model. 
`multifit_py` then calls the user model function (in Python) with these parameters and calls `multifit` with the result.
`multifit` then calculates the residuals and Jacobian and determines the next parameters, whereupon it returns
to `multifit_py` the new parameters, which `multifit_py` evaluates and calls `multifit` with the result, etc.

Thus, the Python code always calls the Matlab code and only data is exchanged bi-directionally,
which satisfies the standard Python-Matlab interface.
However, this also means that a Python wrapper and changes to the Matlab code is needed for this method to work.

These changes to the Matlab code may be quite extensive, especially in the two specific use cases where we need
Matlab to call Python: that of `multifit` and the SpinW-Brille interface.
