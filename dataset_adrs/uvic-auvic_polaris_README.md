# What is an architecture decision record?
An ADR is a document that captures an important architectural decision made along with its context and consequences.

# How to submit an ADR
Create a new ADR in your fork and then perform a pull request to have it reviewed.

# file name convention
The name has a present tense imperative verb phrase. This helps readability and matches our commit message format.
The name uses lowercase and underscores (same as this repo). This is a balance of readability and system usability.
The extension is markdown. This can be useful for easy formatting.
## Examples:
choose_database.md
format_timestamps.md
manage_passwords.md
handle_exceptions.md

# Suggestions for writing good ADRs
- Point in Time: Identify when the AD was made
- Rationality: Explain the reason for making the particular AD
- Immutable record: The decisions made in a previously published ADR should not be altered
- Specificity: Each ADR should be about a single AD
## Characteristics of a good context in an ADR:
- Explain your organization's situation and business priorities
- Include rationale and considerations based on social and skills makeups of your teams
Characteristics of good Consequences in an ADR::
- Right approach - "We need to start doing X instead of Y"
- Wrong approach - Do not explain the AD in terms of "Pros" and "Cons" of having made the particular AD
A new ADR may take the place of a previous ADR:
When an AD is made that replaces or invalidates a previous ADR, a new ADR should be created

# Links to example ADRs
https://github.com/joelparkerhenderson/architecture_decision_record/blob/master/adr_template_by_michael_nygard.md
https://github.com/joelparkerhenderson/architecture_decision_record/blob/master/adr_template_madr.md
