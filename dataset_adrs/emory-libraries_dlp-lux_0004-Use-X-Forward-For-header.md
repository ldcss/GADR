# 4. Use X-Forward-For Header

## Context

The lux application needs to provide filtering of content via client IP address. Currently the only IP addresses the application ever sees is the Application Load Balancer's.

## Decision

Enable the injection of the X-Forward-For header at the F5. This was accomplished by changing an existing setting on a HTTP profile. Additionally, the apache conf will be modified on all
dlp instances to conside the X-Forward-For header, if present, the client IP address. Additionally apache access logs will be modified to show the header as well as the true client IP.

This will make the access and rails application logs' contain more relevant information instead of displaying the same load balancer IP addresses repeatedly.

## Consequences

Our cap_deploy role needs to be modified so that this change is not lost during a rebuild.

Being on VPN interferes with the client IP, it appears to be the "tunnel IP" instead of the actual IP.

If the infrastructure of the dlp project is changed, e.g. F5 is removed, we may have to change apache or the application code.

If the X-Forward-For header injection is disabled on the F5, IP filtering will silently stop working. We should consider setting up some sort of test to check if the header is present.

## Alternatives

### Programatically search for header instead of IP

- PRO: Less dependant on external infrastructure.
- CON: More complicated code, does not fix issue with ALB IPs in log files.
