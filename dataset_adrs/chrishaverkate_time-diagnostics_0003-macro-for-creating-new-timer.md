# 3. Macro for creating new timer
Date: 2020-11-15

## Status
Implemented

## Context
Creating and holding a timer object can introduce errors and noise in the code that's using it. It's also hard to remove for release code to optimize performance.

Example:
```c++
#include <time_diagnostics.h>
TimeDiagnostics td<2>;
static const TIMER_ID = 0;

{
    Timer t = td.get_timer(TIMER_ID);
    // ... user code
}
```

## Decision
Provide a macro that can be used to start a new timer and can be disabled during recompile.

Example:
```c++
// uncomment this to remove timers for release code
// #define DISABLE_TIME_DIAGNOSTICS
#include <time_diagnostics.h>
TimeDiagnostics td<2>;
static const TIMER_ID = 0;

{
    START_TIMER(td, TIMER_ID);
    // ... user code
}
```

## Consequences
**Advantages**
* User does not have to explicitly create and name timer objects. They have no user input after creation anyway.
* A simple definition of ```DISABLE_TIME_DIAGNOSTICS``` turns all ```START_TIMER()``` macros into empty statements, removing any overhead of using them.
* Stands out from other code and clarifies intent.

**Disadvantages**
* It's a macro...
