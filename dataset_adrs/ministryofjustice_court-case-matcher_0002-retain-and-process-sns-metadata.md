# 2. Retain and process SNS metadata

Date: 2021-05-28

## Status

Accepted

## Context

The service receives case messages from the SQS queue `court-cases-queue`. These messages, being produced from an SNS subscription, are embedded in JSON containing metadata about the message. It is possible to remove this metadata through configuration of AWS, thereby allowing for easier processing of the case itself in court-case-matcher or to retain it. 

The metadata includes the following fields
* `messageId`
* `topicArn`
* `timestamp`

## Decision

We have decided to retain the message metadata. There is no immediate use for the fields at but the cost of processing is low and there's a possibility that `messageId` will be useful for tracing. 

### Links

Description of the terraform field for enabling delivery of the message without metadata.
https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/sns_topic_subscription#raw_message_delivery


