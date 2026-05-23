# Use [Amazon Kinesis Data Analysis](https://aws.amazon.com/kinesis/data-analytics/) to process raw data

* Status: accepted

## Context and Problem Statement

Vehicles recognized in a video stream are transmitted as raw data to the Traffic Processing Service and should be processed Near Real-Time (NRT). Raw data are coming via unbounded streams. To make decisions, each vehicle should be [windowed using a session](https://ci.apache.org/projects/flink/flink-docs-stable/dev/stream/operators/windows.html#session-windows) approach. Decisions require joins from different data sources (several cameras, red light sensors, etc.). Throughput per data source is around 200 points per second. Each one size less than 1 Kb size. 

## Considered Options

* Use Apache Hadoop to process raw data
* Use Apache Spark to process raw data
* Use Apache Flink to process raw data
* *Use [Amazon Kinesis Data Analysis](https://aws.amazon.com/kinesis/data-analytics/) to process raw data*
* Use Apache Storm to process raw data
* Use Apache Kafka to process raw data
* Use AWS Kinesis Firehose to process raw data
* Use AWS IoT Analytics to process raw data
* Use custom logic to process raw data

## Rationale
Custom logic would be complex and doesn’t make sense when there is a variety of existing solutions.

Apache Hadoop is designed for batch processing and is not suitable for unbounded data streams due to it adds lag.

Spark can be used but it is not a real-time dataflow based engine. It works in micro-batches to simulate Near Real-time processing and doesn't support statefulness.

Storm doesn't provide a high-level stream processing/analysis API as Flink does e.g. Map, GroupBy, Window, and Join, etc. which needs to be manually coded in Storm.

AWS Kinesis Firehose has a minimum buffer of 60 seconds. It also has limited per record transformation capabilities using AWS Lambda. It’s not enough.

AWS IoT Analytics doesn’t support time windowed operations.

Benefits from Kafka’s core competency are performance, scalability, security, reliability. Flink, on the other hand, is a great fit for applications that are deployed in existing clusters and benefit from throughput, latency, event time semantics, savepoints, and operational features. The only disadvantage is that Apache Flink requires system management efforts.

Amazon Kinesis Data Analysis is serverless and offers using Apache Spark or SQL to process data in the realtime data stream, consequently, this is considered the best option

## Feedback
Apache Beam has not been considered due to it’s unified programming model that is used on top of engines (e.g. Bean on Flink).
