# Architecture

## Origin

Due to experience from previous projects, it became apparent that neither Salesforce nor Screendoor were adequate for the needs of a small-to-midsize governmental department within the City. Whereas Salesforce was too complex, slow, oversized, and expensive- Screendoor was too limited and not accessible enough, and in time- would also eventually become too expensive. At the time (2017), there were no robust, actively maintained open source CRM or workflow management applications available for use that was flexible enough to meet the requirements of OOC which included having an externally removable/detachable database structure.

## Considered Alternatives
* Salesforce
* Screendoor
* Sugar CRM
* OpenCounter
* OpenCities
* A microservice architecture

## Decision Outcome

* Decision: A microservice architecture

None of the other solutions addressed all of our requirements and had no roadmap to do so in the near future. Sugar CRM was no longer supported, OpenCounter was limited, and OpenCities was data-inaccessible. Architecturally, making a SAAS monolith is too resource intensive and not very flexible or future-proof. Therefore, a microservice architecture would include but not be limited to: a form builder, a workflow/permit/customer/approval manager, and an emailer.

# Form Builder

## Considered Alternatives
* Salesforce Configurator 1.0 (Vertiba)
* Salesforce Configurator 2.0 (Vertiba)
* Screendoor
* Formstack (Salesforce)
* Form Assembly (Salesforce)
* Google Forms
* Typeform
* formsite
* HubSpot
* Cognito Forms
* Clearbit Forms
* Gravity Forms
* JotForm
* FormTools
* Wufoo
* FormBakery
* JSON-based form generators
* Make our own

## Requirements
* Fast loading and reactive
* Easy form creation GUI
* Drag n drop form creation
* Full CSS form access
* Multiple templates and layouts
* Multi page and multi step forms
* Save and load unfinished form data
* Atomic HTML substitution based on pattern library
* Rearrangeable DOM
* API Webhooks
* Mobile responsive (preferably mobile first)
* Autosaving
* Conditional questions
* Calculations
* Standard form validation (advanced/regex validation a plus)
* Payment integration
* Salesforce integration
* Accela integration
* Drupal integration
* API access or connector for third party integration
* Affordability

* Decision: Make our own

Yes, the requirement list is bordering on ridiculous so to say that every alternative was eliminated for not meeting all the requirements is not really a fair assesment. A comparison Matrix was created and alternatives were weighed on these main merits:

* Feature set
* User experience
* Data accessibility
* Flexibility, future-proofing
* Cost

### A rough breakdown of Alternatives

* Anything Salesforce related would fair about average in most categories but fail horribly on cost. Even an online form builder with a Salesforce connector would shoot up disproportionately in cost (ie: going from $50/month to $900/month just to get it to talk to Salesforce).
* Most remaining online form builders would be inadequate on either data accessibility or flexibility/future-proofing by not allowing a combination of particular look and feel, DB access/import/export, API access, webhooks and/or integrations.
* JS framework and JSON-related form builders did not have a robust feature set and/or the UX aspects were completely missing.
* An open source library based off Bootstrap was chosen (Bootstrap Form Builder) to start building our own. Plain PHP was turned down in favor of a JS hybrid to allow a more modern feel and UX.

### Pros and Cons of making our own

* `+` Feature set, flexibility, and future-proofing are not limited.
* `+` Webhooks and integrations can easily scale.
* `+` Does not require learning a full JS MV* framework, has a smaller footprint.
* `+` Faster loading for end-users because embedded forms and editor libraries can be decoupled.
* `+` Based on Bootstrap which is widely adopted and supported and is mobile responsive by design.
* `+` Supports a popular, proven validation library (Bootstrap Validator by 1000hz) that is rule-based, allows advanced custom rules, and not reliant on server calls.
* `+` Chosen form builder starter has decent UX (including drag n drop), outputs source code, and is highly malleable.
* `+` Does not lock you into a subscription or particular (pay-to-play) system.
* `+` Full control over where the data goes and we own all the code.
* `+` Cheaper to get started.
* `-` Initial feature set is slightly below average.
* `-` We have to do the brunt of the heavy lifting above basic form creation.
* `-` Not a turnkey solution.
* `-` Does not include the email and workflow aspects and lacks any user auth or submission datastore.