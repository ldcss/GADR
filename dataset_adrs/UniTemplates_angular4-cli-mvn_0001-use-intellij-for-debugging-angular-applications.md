# Use intellij for debugging angular applications

Angular applications can be debugged by setting breakpoints in intellij or break points in browser debug tool.


## Considered Alternatives

* *Using Chrome internal debugger*
* *Using Intellij debugging*

## Decision Outcome

* Chosen Alternative: *Using Intellij debugging*

### HowTo debug angular applications in Intellij 
1. run `npm start`
2. Setup JavaScript Debug configuration:
  - Open Run/Debug Configuration (left of run and debug buttons)
  - Add new Configuration `JavaScript Debug`
  - Set URL `http://localhost:4200`
  - Set Remote Url `webpack:///.` for application directory
3. Select new configuration and click debug button
4. Ensure that `JetBrains IDE Support` browser extension ist installed and enabled in Chrome (Click Intellij popup link)

### What does work
- All breakpoints that are triggered by user interactions
    - Test breakpoint in app.components.ts for the logging operation triggered by a button click.

### What does not work (yet?)
- All breakpoints that are involved in the initial loading phase of the application will not be triggered!

