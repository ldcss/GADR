# Managing logs


## Context

Every application needs to manage logs, of different levels, and sending them to different channels.


## Decision

We want to use the normal approach regarding managing logs, according to which any logging concern should be confined to the adapter layer, leaving the application layer independent from them. However, since contents to be logged are also produced in the application layer, we need a way to communicate them to the logger. The usual solution is to add a message bus to the use case services, so that any information that is relevant to be communicated to the outside world, from an application logic point of view, can be sent as a message, so that some adapter is then able to catch these messages, and maybe send them to the logger.

For example, logs are the only way we have to display debug stack traces. In fact, we already have in place a mechanism to display errors to the end users, which is a specific use case for it: however, this use case is, as just stated, focused to communicate with the end user, and for this reason the contents it displays should be user friendly. This means that application errors will be specific messages informing the user for example of an input validation error, while system errors will likely be just generic messages without any technical detail, which wouldn't be interesting for the end user. Both kinds of errors, then, won't contain any stack trace, when displayed to the end user, and thus we cannot use errors displayed to the user interface as a debug mechanism.

What is left for debugging, then, are logs. In particular, the error handler application interactor will send complete error objects as messages, in addition to displaying the generic error messages. These error messages will then be caught by a logger handler, which will decide if writing the stack trace or not according to the current application runtime mode or environment.

Debug mode is a different "build" or environment of the application. Applications written in a compiled language usually can be built in debug mode, since activating debug means adding a lot of code that slows everything down. In applications written in interpreter languages this is not really possible, but we still want to maintain the same semantic, so debug mode should be a configuration, or environment choice, and not like a command line argument, or user-provided selection anyway. We can select if debug mode is enabled or not according to the execution environment: for example "dev" and "test" application modes usually have debug enabled, while "production" mode has not.

We can decide to do multiple things in debug mode: for starters, we decide that we want to show stack traces instead of simple error messages, and to log all messages, even non error ones. During acceptance tests, we don't want to display logs to the main output (for example to STDERR) because acceptance tests should test the application as it works for the end user, which won't see debug logs, but at the same time we want to have debug information available: what we'll do is then writing debug logs to a file instead of to the console. When in "dev" mode, instead (running the application manually), we'll redirect error logs to the console as well, for direct debugging.

Now, should we show stack traces only when in debug mode? If the application is not in debug mode, we can avoid writing stack traces of application logs, because they still contain information about the error, because they're meant to be informative for the end user as well (think for example of the input errors); however, system errors not in debug mode will be just generic user friendly message, containing no useful information for understanding what's the error: for this reason, we should write stack traces of system errors also when not in debug mode, of course not displaying them to the end user.


## Status

Proposed


## Consequences

The application layers stays independent from any logging concerns, while it just sends meaningful application messages, that can be used by adapters, or even other use cases, for any reason, for example logging.

Stack traces are not displayed to the main error output, but as error logs, which in development mode can be redirected to the standard error, if this turns out to be handy. The main error output should only display user friendly messages.
