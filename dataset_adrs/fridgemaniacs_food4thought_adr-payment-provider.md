# ADR 1. Smart Fridge and Kiosk POS will handle payments

## STATUS
Accepted

## CONTEXT
Customers need to be able to pay for their food.

Currently we are supporting 3 ways of acquiring food: Smart Fridge, Kiosk and Home delivery.
* Smart Fridge solution, [Byte Technology](https://bytetechnology.co/retailers/foodservice/), supports payments with credit/debig card.
* Kiosk and Home delivery payments are handled by [Toast POS](https://pos.toasttab.com/), which also supports payment with credit/debit card.

Customers are also sometimes eligible for discount or free meal coupon. This is provided through their Farmacy Food account.

Problem is that system that is responsible for communication with payment provider needs to know about those discounts.

This could be achieved by:
* handling payments on our system - assuming that both Smart Fridge and Kiosk POS can communicate purchase to our systems,
* handling payments on Smart Fridge and Kiosk POS systems - assuming that their systems allow setting up discounts for specified credit/debit cards (as unique customer identifier),

## DECISION
We will let Smart Fridge and Kiosk POS systems handle payments.

We dismissed solution with handling payments on our systems because of concerns around latency and reliability of our backends.\
For operations as important as payments, it is paramount that they stay fast and reliable. \
Adding additional backend communication would only lower the changes for it to be true.
 
Additional advantage is that now our architecture doesn't have to focus on characteristics important to reliable payment processing.

## CONSEQUENCES
We will require Smart Fridge and Kiosk POS solution that supports setting up discounts for specific customers (e.g. by using credit/debit card UID).
