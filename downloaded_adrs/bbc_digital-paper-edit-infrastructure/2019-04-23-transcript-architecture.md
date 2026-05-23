# Architecture for Digital Paper Edit

* Status: Accepted <!-- optional -->
* Deciders: Pietro, Dave, Eimi, James, Alli <!-- Laurien, Mark Langton, James Gruessing -->
* Date: 2019-06-21

Technical Story: https://github.com/bbc/digital-paper-edit/issues/1 <!-- optional -->
Additional Stories:
- https://github.com/bbc/digital-paper-edit-api/issues/1

## Context and Problem Statement

Digital Paper Edit has three milestones. Transcript, Paper-edit, and Annotation.
We want to make sure that during the Transcript phase, we have a solid
architecture to provide storage for uploaded content and transcription to be
used in later phases. We want to consider technologies from a resilience,
scalability, cost point of view, opensource compatibility and extensibility.

## Decision Drivers

* resilience
* scalability
* cost
* number of users
* opensource compatibility
* extensibility

## Considered Options

* Framework and infrastructure: Docker vs Serverless vs Cosmos
* Components: Lambda vs EC2 (AWS)
* Storage: local vs S3
* DB: PostgreSQL (RDS) vs DynamoDB vs MongoDB
* Queues: STS vs RabbitMQ

### Potential Problems in Options

#### Framework and infrastructure: Serverless vs Docker vs Cosmos

Serverless framework makes it easy to deploy serverless and
many other components using a cli. It might be easy to begin
with and is quick to deploy serverless, but becomes more difficult to maintain
with transfer (local development vs production). It also isn't platform
agnostic, which was what was initially suggested. It will give you the
flexibility of using another platform, but you will still need to configure
platform specific variables in your code. Developing and using this means we
also lack transparency and resilience because the deployment occurs on someone's
local development.

Docker was considered to simplify the orchestration of microservices. Using docker means we could
have a separation of concerns - the OS and the application. However, using this means we would still
need to select a platform (AWS / GCP) and deploying it on the VM. This
also implies that there is an extra level of abstraction: a Docker image (VM)
inside a cloud VM. Debugging it also requires extra set up. If we decided to use
Docker, we will not be able to use Cosmos which would give you the bulk of the
configuration including HTTPS access for free.

Using AWS and Cosmos means tying into the AWS architecture, makes it very
difficult to move away. There is also overhead on learning how to use Cosmos.
There is also less flexibility in the way we would do deployments - we would
need to set up in Jenkins and be restricted to RHEL7, using RPMs as the
packaging method.

#### Components: Lambda vs EC2 (AWS)

##### Lambda Pros and Cons

From [this article](https://dzone.com/articles/the-pros-and-cons-of-aws-lambda),
the pros and cons can be summarised as the following.

Pros:

* Reduced cost of execution
* Improved application resiliency
* Decouple server architecture to code
* [Idempotent](https://en.wikipedia.org/wiki/Idempotence)
* Resource allocated when needed

Cons:

* Loss of control over environment
  * machine - not guaranteed to have the same AMI
  * no OS capabilities
  * hot/cold function - causes delays
* Packaging lambda with dependencies could be problematic
* More complex call patterns
  * Runtime limitations + Time outs
  * Time outs removed with step-functions? - unverified
* Could be slower
* May not be beneficial for FFMPEG
  * Unknowns around FFMPEG binary requirements

**Cold Lambda**
Articles read:

* <https://read.acloud.guru/does-coding-language-memory-or-package-size-affect-cold-starts-of-aws-lambda-a15e26d12c76>
* <https://kevinslin.com/aws/lambda_cold_start_idle/#results-us-east-1>
* <https://read.acloud.guru/how-long-does-aws-lambda-keep-your-idle-functions-around-before-a-cold-start-bf715d3b810>

tl;dr the three articles above:
Lambda idleness causes

1. lambda is terminated
2. a call can timeout or return an error
3. the next successful call will be “cold”, meaning slower

* Cold starts can happen when idle time is around the 1h mark but this is not
set in stone.
* Cold starts can vary depending on the allocated memory, code size, and the
  language the lambda is running.
* Python works best in these scenarios (very little time taken to start once
  cold) and Java / C# takes longest (static typing)
* The worst case scenario is ~5s (C# with 128 memory size).

In order to avoid the cold restarts, we would need to create "Step Functions" to
retain Lambdas "warm". The Step Functions will periodically call Lambdas (every
30 minutes or so) to reduce idle time.

##### Message delivery and Queues

Using both SNS and SQS are well known patterns. SNS fans out messages to services subscribed to the topic. Services such as HTTPS, Queues, and Lambdas can subscribe to the topic. This is typically called the Pub/Sub model.
SNS and SQS are often combined to fanout a single message to many different services in real-time. SQS is considered for our architecture for retry logic. SQS is a best effort FIFO queue which works for us. SQS's cost is based on the number of polling calls are done on the queue. The first million is free, and it's $0.40 for every subsequent million calls.

The consumer of the queue can be either EC2 or Lambda.

Lambda is beneficial in this case if we wanted asynchronous behaviour when there are jobs in the queue. However, since the microservices all have a uniform approach (subscribe to queue, update DB via API), it will be nicer to retain a uniform approach. Other than saving the cost of polling, there are no clear benefits of using a Lambda.

Articles read:

* <https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-best-practices.html>
* <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html>
* <https://aws.amazon.com/sns/faqs/#reliability>
* <https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html>
* <https://medium.com/@TomKeeber/top-sns-aws-design-patterns-19b6acc82017>
* <https://d20tech.com/2018/fanout-with-sns-sqs-lambda/>

#### Storage: local vs S3

S3 will benefit us in terms of resilience and remote storage. However this could introduce issues
for infoSec if we are storing business critical items. S3 is easy to integrate with Platform STT.

#### Database: Sqlite vs PostgreSQL vs DynamoDB vs MongoDB

Using PostgreSQL flexibility of using JSON in columns. MongoDB and DynamoDB can
be too verbose. We were quite clear on the shape of the
database model already.

I was reading an article about [Guardian’s migration from MongoDB to Postgres](https://www.infoq.com/news/2019/01/guardian-mongodb-postgresql).
It seems like many organisations are moving to Postgres and RDS (you can see
from the article linked before). I think if we wanted this to be a long-lived
project, we want to ensure that it’s reliable and resilient. If we wanted to
use JSON data, then yes we need it to be Postgres. 

Sqlite is not good enough to be a fully production database. It doesn’t scale
very well either. However Sqlite could be used inside Electron, for single user
access. Also using PostgreSQL already meant that the JSON would give us enough flexibility.

##### EC2 local server vs RDS

Considered requirements such as:

* Maintaining state of transcripts once it’s uploaded
* speed to access the database
* cost

The database is critical to the operation and we also need modularity.
It separates out the database as a separate server, that is not maintained by
us, which is quite useful. RDS will give us the benefit of backing up as well.
If the server was on EC2, the database could lose information when the instance
failsover. Additionally, based on the size of the database, we would need to
increase the size of the machine, adding on to the cost. Although, for what we
have it will be a smaller cost than having an RDS instance initially.

### We ruled out

* Hosting a website in S3 with CloudFront - no HTTPS cert-based authentication,
only IP address based authentication.

## Decision Outcome

We are going for **Option 3**.

Option 1 (only EC2)
![Option 1 (only EC2)](./dpe-transcript-EC2.png)

Option 2 (EC2, Lambda and gateway)
![Option 2 (EC2, Lambda and gateway)](./dpe-transcript-EC2_Lambda.png)

Option 3 (EC2, Lambda, SNS, and SQS)
![Option 3 (EC2, Lambda, SNS, and SQS)](./dpe-transcript-fleshed-out.png)

All options will have the advantages of:

* being maintainable,
* being transparent
* being transferable
* using existing pipelines
  * It will have the benefits of using Cosmos, which means we will automatically
have cert-based security and ELBs. We will also have a solid CI process around
the project, including transparency around deployment issues.

All options will have the disadvantages of:

* Initial learning curve around Cosmos (need to understand RHE7).
* Extra files for Cosmos will be in an opensource repository, which will require
  additional documentation and security checking.
* Cost of AWS - not entirely sure how much it will be right now, but it will be
  a minimum of 4 instances running in `t2.small` for Option 1, and 2
  `t2.small` instances for Option 2, plus lambda executions as well as SQS and
  S3.
* Locking in with AWS.

### Option 1 (only EC2)

#### Advantages

* Common pattern and will be easier to set up locally.

This is good for the opensource developers - who will not need AWS accounts to
test integration locally with Lambdas and Gateways.

#### Disadvantages

* Operational concerns that might be unnecessary

### Option 2 (EC2, Lambda and gateway)

#### Advantages

* Cheaper as there isn't a full instance running - Lambda.
* Better for the environment (less operational CO2 cost)

#### Disadvantages

* There could be a time-out issue for Lambda
* Difficulty in debugging due to Lambda
* Operating System is abstracted away (loss of control)

### Option 3 (EC2, Lambda, SNS, and SQS)

This has been developed two months after. The architecture is fleshed out in this option.
It shows, clearer responsibilities with defined interfaces.
We've added:

1. SNS and SQS (fanout pattern) for reliable job delivery to microservices.
2. Each microservice to have a queue for asymmetrical queue growth.
3. S3 signed URL communication via API, rather than direct upload from API. This will improve data transmission from different components.
4. STT Queue jobs to be published by Audio FFMPEG Service, subscribed STT client (proxy), and pushed to STT service, treated as a black box.
5. On completion of STT task, the client will update the API directly.

The video preview section is tinted with yellow as it is not currently in-scope.

#### Advantages

* Fault tolerance from using queues
* Avoiding timeout issues with Lambdas for running long jobs
* A uniform interface across the media processing microservices (polling queues, posting to the API)
* Upload is not via the API, which supposedly improves data transmission time.
... and benefits from the previous options.

#### Disadvantages

* Additional components and technologies
* Polling - although cost is negligible with optimisation.
