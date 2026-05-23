# Logging

## Context

* Running a service is easier if you know what it is doing

## Decision

* We will follow the logging principles of the 12 factor app: http://12factor.net/logs
* We will only ever send output to console. Never write logs to file.
* For example in production we could redirect the app output using: ```lein run | logger``` then we can see the output by using  ```tail -n 0 -f /var/log/system.log```
* Semantic logging should be used where appropriate

## Alternatives

* Timbre and clojure/tools.logging are good options if we need to do anything more advanced.