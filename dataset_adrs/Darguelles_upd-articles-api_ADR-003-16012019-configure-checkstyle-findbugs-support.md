### **ADR-003 - Checkstyle / Findbugs plugin integration**

**Context**

Code quality is very important and we need some way to ensure the code we are sending to production is clean code based on good practices and without bugs that can cause some unexpected behaviors. Sonar is a good option in our Integration server but how we can check our code in the local environment?

**Decision**

There are two very famous plugins to help us. [Findbugs](http://findbugs.sourceforge.net/) will scan the code and detect any possible bug that can cause an unexpected exception or some vulnerability in our code. Same way [Checkstyle](http://checkstyle.sourceforge.net/) will help us to be aligned with the code standard depending on the platform, in this case Java.

**Status**

Accepted

**Consequences**

Both plugins will be executed when the build command is executed. Currently Findbugs is activated to prevent build to be done if detects some code vulnerability or bug. It will generate a report in HTML code to analyze the point of failure. Checkstyle is configured to alert us about the code bad syntax, but will not stop the build.
These two configurations can be modified on the `build.gradle` file.