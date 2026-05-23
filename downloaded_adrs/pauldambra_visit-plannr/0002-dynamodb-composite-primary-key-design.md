# 2. DynamoDB composite primary key design

Date: 2018-03-04

## Status

Accepted

## Context

"[In DynamoDB, tables, items, and attributes are the core components that you work with. A table is a collection of items, and each item is a collection of attributes. DynamoDB uses primary keys to uniquely identify each item in a table and secondary indexes to provide more querying flexibility.](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html)"

There are two types of primary key in dynamodb.

The first kind is having just a partition key. The partition key is a hash and determines where on physical storage the item is placed. The partition key must be unique.

The second kind is a composite primary key. It consists of a partition key and a sort key. The partition key stays the same but doesn't need to be unique in isolation. Rather the sort key/ partition key pair must be unique.

In a real system this would probably push towards StreamName as the partition key: so that events that logically live together physically live together. And Event Number in the stream as the sort key. So that the order of items as they are stored on physical media matches the order they are likely to be read.

This introduces unwanted complexity at this time in the code for tracking event numbers.

## Decision

For now instead of an Event Number as the sort key we will introduce a UUID EventId. And use StreamName as the HASH key. StreamNames will need to be unique anyway.

## Consequences

This will need performance testing to check that there is no significant impact of the items being effectively randomly sorted.
