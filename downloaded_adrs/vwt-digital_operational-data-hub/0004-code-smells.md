
# 4. Codesmells / Coding by exception.

Date: 2021-02-15

## Status

Accepted

## Context

We feel the need to eliminate practices that could lead to [coding by exception](https://en.wikipedia.org/wiki/Coding_by_exception). Furthermore we want to create some guidelines to prevent some common [code smells](https://en.wikipedia.org/wiki/Code_smell).

## Decision

### 1. Low cyclomatic complexity / Low level of recursion.
Cyclomatic complexity is the number of linearly independent paths in a piece of code. In short, this is determined by the depth of a coding stack. If-statements for-loops, and inline functions all increase the cyclomatic complexity of code. Higher cyclomatic complexity can lead to more coding errors, and less transparent code.
Another reason for this is that a higher cyclomatic complexity can indicate a high level of recursion, which in turn can make code less efficient for larger data sets. 
The cyclomatic complexity of code should be no higher than 3-5 per function or class.

flake8 will be used to enforce this requirement.

### 2. "Do not repeat yourself."
Whenever possible, we should abstract away from duplicated code. It is not a problem to copy and paste a small code snippet once. 
Whenever a piece of code is reused twice, an abstraction should be made to remove the duplication.

### 3. Keep it simple
To ensure reusable code and good collaboration the following rules should be followed:

- Use explicit variable names.
	- Variables like `file` should be named after what they're used for e.g.: `source_pdf_file`
	- Classes that handle data storage should be named after the type of data they store. 
	- `WorkItemStorageHandler` instead of `StoragerHandler`.
- Clear is better than clever.  Favor readability over conciseness.
- Use for loops over list comprehensions.

### 4. Specific small modules
- Write code in small reusable modules.
- A python function should serve one purpose and one purpose only.
- Generally a python file should be 100-150 lines long.

### 5. No code in ```__init__.py```
No code should be put inside an ```__init__.py``` file, since this file is only for exposing internal dependencies to the top level of the package. 
Instead, a main.py file should be used for code.


### 6. Object-oriented code
Python is an object-oriented language, so developers should strive to write object oriented code. This is a challenge for cloud functions specifically. Functions tend to be procedural by nature. In this case, a developer should write one file (main.py), with one entrypoint, which procedurally processes a message. To keep it OOP and testable, abstract different features away. 
For reading an email inbox, use a dedicated `MailService` object. for writing to storage, use a `Storage` object.

An example: [https://github.com/vwt-digital/ews-mail-ingest/blob/develop/functions/ews-mail-ingest/main.py](https://github.com/vwt-digital/ews-mail-ingest/blob/develop/functions/ews-mail-ingest/main.py)

### 7. Avoid unnecessary exceptions.
- Only handle exceptions when they occur. 
- When an exceptions occurs, first try to prevent the exception from occuring. 
- If this is not possible, properly handle the exception. 
- Don't use a `try: except:` block without an exception or with simply a  `pass` statement

### 8. Implement retry policies carefully.
When calling external API’s and services, predetermine the retry policy. Always throw an exception after retries are exhausted. This ensures that when a service’s poor health can be noticed.

For exceptions that occur when calling an external service the function, a warning should be emitted that can be monitored to ensure that this does not occur to often within a given timeframe.

### 9. Use dependency injection

- Code should be loosely coupled from its dependencies. 
- When using an external service, always write an [adapter](https://en.wikipedia.org/wiki/Adapter_pattern), so that it can be tested or changed for another external service.

### 10. No conditionals in deployment

Environments should be exactly the same.
- No references to the environment in a cloudbuild.yaml
- No environment checks in code. 

## Consequences
