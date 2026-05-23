# 2. Overall System Architecture

Date: 2019-04-21

## Status

Accepted

## Context

To put down an architecture for the system as a whole.

## Decision

The system consists of the following components:
* Global components:
  * Alexa Smart Home Skill
  * AWS Lambda
  * AWS API Gateway websocket endpoint
* Per user-components:
  * Google Account containing an automatically set-up Google Spreadsheet
  * Universal Remote Controller (URC) device

### Alexa Smart Home Skill

* Takes care of activation and hands off control to AWS Lambda
* Links to user's Google Account

### AWS Lambda

* Receives and keeps websocket connection from each URC and sends commands to the URCs
* Reads configuration data from user's Google Spreadsheet

TODO: this needs to be worked out further, following 

### Google Account with Spreadsheet

The Spreadsheet contains all necessary configuration data to control the user's specific environment:
* URCID
* IR/RF transmission sequences grouped by appliance
* mappings of commands to transmission sequences, e.g. "Turn On TV" --> specific IR transmission sequence to turn on TV set

### Universal Remote Controller

* ESP8266 system with IR and RF transmitter
* has a baked-in unique URCID (from DS2401)
* upon startup establishes websocket connection to AWS API Gateway (passing its URCID), and keeping that connection permanently alive
* receives and executes commands that AWS Lambda sends via AWS API Gateway

## Consequences

What becomes easier or more difficult to do and any risks introduced by the change that will need to be mitigated.
