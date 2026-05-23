## ADR 9: Using Sentry for Error Reporting
July 26, 2019

### Context
Now that the touch table is on the museum floor, we expect new errors to crop up, especially as the table is now used throughout the day by multiple people at a time. The main issue we had on the first week is the table frequently crashing after short bursts of activity. It is not the most productive approach to keep an eye on the table, discover crashes by checking the event viewer, reboot the app, and hope it works while a patch is being made.

Ideally, the table will automatically report errors as they occur so developers can debug remotely without having to keep constant watch on the table.

### Decision
One huge issue here is the table crashing and leaving a bare Windows desktop on the museum floor. In response to this, a batch script is running on the table's command prompt that restarts the application if it detects app closure from a crash.

As for automated errors reporting, we will implement Sentry to send an email whenever the table experiences a new crash. Although many of the small bugs were addressed the first week, it's likely new bugs will appear as the table stays on the floor. This way, even though the app will restart on a crash, developers will know when a bug needs to be patched.

### Status
Accepted

### Consequences
The application is more or less running on autopilot using both Sentry and a batch script. Hopefully, this does not cause lack of urgency when a bug does appear. Sentry mentions where the app crashes and provides some breadcrumbs to trace back the bug, and this should be sufficient for remote debugging.
