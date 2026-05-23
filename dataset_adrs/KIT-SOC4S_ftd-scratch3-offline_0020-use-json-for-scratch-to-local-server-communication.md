# 20. Use json for scratch to local server communication

Date: 2019-11-02

## Status

Accepted

## Context

We are using POST HTTP requests to communicate with the local server.  
To pass multiple parameters we would use requests with `multipart/form-data` or `text/plain` type.  
Creating correctly encoded multipart requests is tricky.  

## Decision

We will use json for scratch to local server communication.  
I.e. responses from server to scratch will be json objects similar to this:  

````json
{
	"status" : "", | "SUCCESS" or "FAILED"
	"errorMessage" : "", | null when no error happened, otherwise an error message
	"result" : "" | null when there is no output (e.g. in case of an error), otherwise the result
}
````

## Consequences

Values will have to be converted from json to java objects and vice versa.  
Conversion could theoretically fail.