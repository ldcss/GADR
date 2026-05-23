# 8. Create a document submission without a parent evidence request

Date: 2022-10-27

## Status

Accepted

## Context

The process for uploading documents in Evidence API is like so:
1. Create an evidence request with the contact info of someone who will upload documents ('resident')
2. The resident receives a request for evidence
3. The resident uploads documents against that evidence request
4. Officer then reviews the documents to say if they approve or reject the documents

Everything is hinging on the creation of an evidence request. However, we've received a new use case to upload documents against
a 'resident' in our system, not an evidence request. This requires a rethink how our data model works because a 'document submission' entity
is created against an evidence request. However, if no evidence request exists (as you don't need to request evidence for a resident you already have)
then how do we create a document submission?

A full, in-depth explanation of the problem can be found [on the Google Drive here](https://docs.google.com/document/d/1l3gihtvRaxxO4cVXcSau0fJTsv9PhLJa4p7QPyqhBXY/edit?usp=sharing)

## Decision

We had 4 options:
1. Create dummy evidence requests
2. Create a linker table to show the relationship between document submissions with residents
3. Add a new column to document submissions linking them to resident ids.
4. Use TargetID in Documents API to avoid Evidence API directly.

TargetID seemed to be the best option. See reasons in document above and
[here](https://docs.google.com/document/d/17AfmnrYR7c9wJV3a3Z-3btaV0RubK_P3j0qgj3LxDiE/edit?usp=sharing)

However, we realised that due to the way pagination would work, it would be very difficult to filter the documents
on status on the frontend. So we opted for option 3.

## Consequences

Access control would be an issue, so we'll likely need to duplicate the Team on evidence requests and document submissions.
Further information can be found [here](https://docs.google.com/document/d/1thfTybKCKDHMYgC6-5HlO42jJZ4j6zHHKYKoJrD-mCE/edit?usp=sharing).

We've found so far that decoupling the document submission from an evidence request is proving to be more difficult than
first thought. This is an on-going situation.