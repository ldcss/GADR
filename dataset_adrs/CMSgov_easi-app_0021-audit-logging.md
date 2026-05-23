# Audit Logging

**User Story:** [EASi 697](https://jiraent.cms.gov/browse/EASI-697)

As we try to have logs for user actions, we need to better understand where
they live and what extent of logging we will be doing.

The decision to use AWS logging tools is addressed in a previous
[ADR](https://github.com/cms-enterprise/easi-app/blob/main/docs/adr/0009-logging-platform.md).
We decided to use CMS Cloud Splunk because it best facilitated the requirement
of forwarding logs to the CCIC and integrating with the CMS Cloud team.

This document will be focusing on the requirements and rules of audit logging.

## Questions / Answers

### 1) Where will the logging live

CMS Splunk, AWS logging tools (e.g. Cloudwatch, S3)

#### &nbsp;&nbsp; a) How will it be accessed

&nbsp;&nbsp; Cloudwatch -> Splunk (subset of personnel has access)

### 2) What data can be logged (technical limitations only)

List of auditable events:

* Server alerts and error messages
* User log-on and log-off (successful or unsuccessful)
* All system administration activities
* Modification of privileges and access
* Start up and shut down
* Application modifications
* Application alerts and error messages
* Configuration changes
* Account creation, modification, or deletion
* File creation and deletion
* Read access to sensitive information
* Modification to sensitive information
* Printing sensitive information
* Anomalous (e.g., non-attributable) activity
* Data as required for privacy monitoring privacy controls
* Concurrent log on from different work stations
* Override of access control mechanisms
* Process creation

Verify that proper logging is enabled to audit administrator activities.
Information collected will be compliant with the Federal Rules of Evidence.

Audit events should contain information that specifies:

* Date and time of the event
* Component of the information system (e.g., software or hardware component)
* Where the event occurred
* Type of event
* User/subject identity
* Outcome (success or failure) of the event
* Execution of privileged functions
* Command line (for process creation events)

### 3) Is there data that cannot be logged

The following should not usually be recorded __directly__ in the logs, but instead
should be removed, masked, sanitized, hashed or __encrypted__: (if we end up having
some of these they will need to be encrypted)

* Application source code
* Session identification values (consider replacing with a hashed value if needed
to track session specific events)
* Access tokens
* Sensitive personal data and some forms of personally identifiable information
(PII) e.g. health, government identifiers, vulnerable people
* Authentication passwords
* Database connection strings
* Encryption keys and other master secrets
* Bank account or payment card holder data
* Data of a higher security classification than the logging system is allowed to
store
* Commercially-sensitive information
* Information it is illegal to collect in the relevant jurisdictions
* Information a user has opted out of collection, or not consented to e.g. use
of do not track, or where consent to collect has expired

### 4) Will all the info come from us

Yes.

### 5) Will we rely on other sources for auditing

Standard 1: Correlated results from automated tools must be searchable by the CCIC:

* Information is provided to the CCIC in a format compliant with CMS and Federal
(e.g., Continuous Diagnostics and Mitigation) requirements;
* Repository sources include systems, appliances, devices, services, and applications
(including databases); and
* CCIC directed repository information collection rules/requests (e.g., sources,
queries, data calls) must be implemented/provided within the time frame specified
in the request.

Standard 2: As required by CMS, raw audit records must be available in an unaltered
format to the CCIC.

Standard 3: Raw security information/results from relevant automated tools must be
available in an unaltered format to the CCIC.

From an ARS 3.1 standpoint CMS as an organization is responsible for the review/analysis/reporting
of audit records. This is accomplished by dual monitoring by the system security
personnel and the enterprise security monitoring (CCIC). The CCIC provides
Tier 2 monitoring of the application for defense in depth measures. The primary
monitoring of review and analysis of the audit logs should be performed by the
system security personnel (i.e. ISSO).

Security personnel reviews and analyzes information system audit records no less
often than weekly for indications of inappropriate or unusual activity as defined
within the Implementation Standards and reports findings to defined personnel
or roles (defined in the applicable system security plan).

Implementation Standards:

* Standard 1 - Review system records for initialization sequences, logons
(successful and unsuccessful), errors, system processes, security software
(e.g., malicious code protection, intrusion detection, firewall), applications,
performance, and system resource utilization to determine anomalies no less often
than once within a twenty-four (24) hour period and on demand. Generate alert
notification for technical personnel review and assessment.

* Standard 2 - Review network traffic, bandwidth utilization rates, alert notifications,
and border defense devices to determine anomalies no less often than once within
a twenty-four (24) hour period and on demand. Generate alerts for technical personnel
review and assessment.

* Standard 3 - Investigate suspicious activity or suspected violations on the information
system, report findings to appropriate officials and take appropriate action.

* Standard 4 - Use automated utilities to review audit records no less often than
once every seventy-two (72) hours for unusual, unexpected, or suspicious behavior.

* Standard 5 - Inspect administrator groups on demand but no less often than once
every fourteen (14) days to ensure unauthorized administrator, system, and privileged
application accounts have not been created.

* Standard 6 - Perform manual reviews of system audit records randomly on demand
but no less often than once every thirty (30) days.

### 6) How long do we need to keep logged data

We can keep forever. The organization retains audit records for ninety (90) days
and archives old records for one (1) year to provide support for after-the-fact
investigations of security incidents and to meet regulatory and CMS information
retention requirements.
