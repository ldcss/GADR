Context
-------
We all could see a working GUI yet, but now it's time to analyze the algorithm correctness.
It is a plotting/statistics library to pick.

Decision
--------
Use `XChart`, a lightweight library with limited statistics capabilities, for plotting.

Rationalization
---------------
The first choice `krangl` and `kravis` libraries turned out uncompatible with Windows for the variety of reasons. 
This has been reported as an issue to the community of these Kotlin libraries, but meanwhile the progress of the project can't be blocked with that anymore.
So it's decided to pick XChart visualization abilities for now, which of course has less abilities than advanced `ggplot` and will require additional effort to bring, say, linear model predictions to the plot.