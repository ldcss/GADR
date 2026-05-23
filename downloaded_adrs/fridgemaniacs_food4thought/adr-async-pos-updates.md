# ADR 3. Use asynchronic calls for updating Smart Fridge and Kiosk POS systems

## STATUS
Accepted

## CONTEXT
POS systems need to know about discounts that we provide to our users.

We update POS systems every time when they create account and are eligible for a discount
or when we introduce new discount that existing accounts are eligible for.

Both scenarios originate from client application actions (create account & create discount).
We can block that action (and UI as well) until we update POS systems as well, 
or we can finish action and update POS systems asynchronously. 

## DECISION
We will update POS systems asynchronously.

Original action (create account & create discount) should not be dependant (fail) on POS systems API failure.

## CONSEQUENCES
There might be some delay before user can use their discount in one of the POS.

We decided this is OK because user rarely creates account before they buy their food.
