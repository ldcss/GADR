# ADR 2. Using serverless architecture for Farmacy Food backend

## STATUS
Accepted

## CONTEXT
In ADR 1, we have decided to extract all billing logic and payment processing out of our systems and let Smart Fridge and Kiosk POS handle it.

This leaves us with supporting:
* "Hungry Person" web & mobile client,
  * pick a meal at specific location,
  * leave feedback for verified purchase,
  * create account to get a discount,
* "Ghost Kitchen" web client,
  * manage food descriptions (for clients and POS systems),
  * view feedback report,
  * view inventory and purchase report,
  * manage discounts,

Expected volume (or traffic):
"We're hoping to have a customer base in early 2021 of about 1,000 dedicated customers." Farmacy Food

## DECISION
We will use serverless architecture.

Based on relatively low expected volume and simple business logic, it makes sense to us to choose not very complex architecture.
Even one of the monolithic architectures (e.g. layered architecture) would do just fine since Farmacy Food is not expecting to scale dramatically in coming years. 

Another advantage of choosing serverless architecture is low operational costs together with easy maintenance.
Perfect for startup like Farmacy Food.

## CONSEQUENCES
There are few disadvantages to using serverless architecture from a vendor.

For example, vendor lock-in and lack of flexibility (for example to optimize performance to your specific needs)
might become issue when the company grows.

But we have decided that for now it is way more important to support lean development and to test new features fast and cheap.
