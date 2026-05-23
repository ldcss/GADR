# ADR3: Sessions over Cookies

For an online application that allows multiple users to login and utilise its functionality, it is important that user information is stored to prevent the user from having to constantly login and re-enter information when they utilise the application multiple times over a short period of time. This information is stored in order to preserve the state of the application. The two ways that the information is stored is via sessions or cookies.

For a session, a file is created in a temperoray directory on the database where the variables used for the session are stored. The data is readily available to all the pages of the website or application when the user is logged on. Each user gets an unique session ID which is used to authenticate and establish a trusted connection to the specific user.

For a cookie, textfile are stored of the users machine and it is sent to the database to identify the user, when they login. If there are no cookies stored on the users machine, the database will send cookies to the browser which will then store them in local memory for future tracking purposes.

With cookies being stored on the local machine, it makes them vulnerable to theft. If the confidential user information is stolen from cookies, hackers can use this information to perform malicious activities on the application or other online entities essential to the user, such as online banking.

## Decision

We have decided to use sessions that will be stored on the database over cookies that are stored locally.

## Status

Accepted

## Consequences

    * Increases the level of abstractions as important information will not be available to the user.
    * The user cannot modify the data from the session as its stored on the online database on Azure.