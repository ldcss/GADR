# 1. ETL Feed Parsers

Date: 2020-10-29

## Status

Accepted

## Context

We need a clearly defined way for handling data feed files for processing, what are the expected inputs and outputs from the parsers and how will this feed into the whole parsing process for ETL ?

## Decision

1. A EAM Parser Factory: this produces a content reader which will be used by all written parsers for reading the contents of a giving data source.

1. A Processing Adapter per EAM data feed type which has registered different parsers which handle the retrieval of different types of data out of giving data feed source (e.g CreditSuisse XML). 

1. Custom Data Extractors (e.g IncomeCashFlowParsers, OrderBroker) which are responsible for extracting different data types from the ContentReader, these are then accumulated by the data feed ProcessingAdapter into a unified format which can be transformed into portions of the expected PriveXML format.

1. The custom data extractors will have rights to define specific errors for their data extraction process and how that will affect that specific extraction or for a giving set of files. We will have errors which may be critical and cause immediate failure or which can be considered non-critical and only stop giving feed extraction or ensure it is logged and continued from. The key is that such details should not be the responsibility of the core and as far as only specific errors which the core is concerned with towards stopping immediately for that giving source or a set of sources.


![Target Parser Flow](../assets/images/workflows/image1.png)


## Consequences

ETL team is only expected to work on implementing new parsers for handling new or old feeds being onboarded. This means we must define the interface which ETL teams implementation must consistently meet.

We have no plans to decide how ETL team implements the parsing logic but require that the function, library or package produce meet the following requirements:

1. The function must accept a list of files, this list could contain one file or a set of files for feed types which require multiple files for parsing their contents.

1. The function must return a list which contains an object containing the list of transactions and positions for a given ticker object within each item. That is one item has a ticker and a set of positions and transactions for that ticker.

1. Since we are writing in python (but regardless of language) all defined errors must use a specified class which will allow the core to understand what should occur in the occurrence of specific types of errors during parsing. This must always be respected. If more information is desired to be attached then subclassing must be used at all times for this.

![Code Interface](../assets/images/workflows/image7.png)

## Questions and Answers

1. What happens when new versions of a feed must be supported with existing format?

	We must ensure that the formats do not share any commonality and their differences is wide enough to force the need for two parsers, and if so, ensure the determining logic can consistently in all cases decide which format belongs to which parser, which ensures on every case that the appropriate parsing logic is used. We require no change in how we archive these issues.

2. What happens when the difference between two formats for the same feed have similar data except for a small set of differences?

	We ensure to only have 1 parser for both which will take into account parsing the small differences between these two. We must not proliferate multiple parsers for such small differences.

