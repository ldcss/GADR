# Godaddy structured JSON logger for Java services

## Context

We need machine-readable logging so that we can do better analytics and our logging is consistent with the Python services, which use Structlog.

We are aiming to meet the ONS's logging standard, which is documented here: https://github.com/ONSdigital/software-engineer-community/blob/master/standards/logging.md

## Decision

We investigated the available open source projects which would give us an enhanced API to make it easier to log key-value pairs in the desired JSON format. Projects with few contributors and without recent releases were not considered to be viable candidates. It seems that Godaddy have a nice enhancement to the vanilla SLF4J API, which is quite convenient for the developer to use.

The proposal to use the Godaddy logger was put on Slack in the developers channel and a vote was held. 6 developers voted "YES" and there weren't any "NO" votes or votes for other solutions.

Godaddy logging API allows you to do logging like this: `log.with("key", "value").error("Here be error messagez", exception);`

More on the Godaddy logger: https://github.com/godaddy/godaddy-logger/

## Consequences

This would require us removing our `@Slf4j` Lombok annotations and replacing them with `private static final Logger log = LoggerFactory.getLogger(XXX.class, LoggingConfigs.getCurrent().useJson());`

There are 145+ places in the Java code where the `@Slf4j` annotation is used.

Any new classes created would have to use the Godaddy logger, for consistency, and Java developers need to get used to using the structured logging API feature, instead of putting key-value pairs into the log messages.