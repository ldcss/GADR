# 7. Use S3 for uploading and fetching documents

Date: 2022-10-27

## Status

Accepted

## Context

Our service allows residents to upload requested documents and officer to then view those documents (for approval or rejection).
However, we found that there was a limit to the size of file that can be uploaded (and downloaded) because we sent the document as a base-64 encoded string.
A base-64 encoded string increases the file size by roughly 33%. As our AWS architecture could only handle a certain size, this meant a limit on what we
could send.

We did look into streaming documents, but we could not go with that solution because we were restricted due to API Gateway.

## Decision

We decided to leverage AWS S3's API to create a Presigned URL and then upload via a link that S3 provided. We made sure that
this link was only available for a short time. We did some threat modelling on this option (due to previous conversations about how S3
provided a public link) but after talking to the security team at Hackney and presenting our findings, we realised it was potentially safer
using this link from S3 than a base-64 encoded string. This is because the link can expire, whereas a string will never expire.

For Evidence API, this meant making sure that the creation of a document submission included the S3 Presigned Url in the response so that the frontend
can upload directly to S3. This [document on Google Drive](https://docs.google.com/document/d/1l3gihtvRaxxO4cVXcSau0fJTsv9PhLJa4p7QPyqhBXY/edit?usp=sharing)
is pretty good at showing the process for uploading -- find the header called 'How do we upload a document?'

## Consequences

As mentioned above, it did make sharing documents safer, as people now needed to be logged in to view the document, as the S3 link would expire
after some time. Additionally it did drastically increase the file limit for what can be uploaded to S3 -- we've currently set the limit to 50MB.

On the downside, if a resident tries to upload a large or many files and they have poor internet connection, the page could potentially take a long time before
a resident is taken to the confirmation page.

Additionally, as the frontend now needs to make a request to get the S3 link and then another request to upload the document, we have found
some incidents of users closing the browser before the document could be downloaded. We added a flag on the frontend to remind people to keep
the page open.
