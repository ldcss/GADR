# Automated Zero Trust PAL

## Status

Proposed

## Context

Some customers who operate in regulated industries or offer SaaS products to their end customers, require Zero Trust environments; meaning that 3rd parties (including Microsoft Partners) should not have access to any environment which contains PII, financial or medical data. This requirement is often backed by legal contracts with the customer's end-customer, who are often also regulated. Although this offers benefits to the 3rd parties around mitigating risk and liability, and limits GDPR responsibilities, it causes problems with access rights based attribution of Azure Consumed Revenue (ACR), required for partner competency consumption targets.

The process for creating a Zero Trust Partner Admin Link is as follows:

1) The Partner shares their MPN ID with the Customer.
2) The Customer exports their list of subscriptions as a CSV, which then can then edited to remove any non-relevant subscriptions.
3) The Customer (with the relevant permissions) creates an AAD Application that is linked to The Partner's MPN ID and retains complete control over the associated credentials that need not be shared with The Partner.

## Decision

We can automate this process by encapsulating it in two PowerShell Cmdlets packaged as a module available from the [PowerShell Gallery](https://www.powershellgallery.com/).

`Export-CustomerSubscriptionsAsCsvForPartnerAdminLink` - run by The Customer to generate a CSV file listing their Azure Subscriptions. This can be edited to remove non-applicable subscriptions.
`Set-ZeroTrustPartnerAdminLink` - run by The Customer to create a dedicated AAD Application. Then assigns this Application the "Contributor Role" to each of the subscriptions listed in the CSV file, and then uses the `AzManagementPartner` module to link the Application to The Partner's MPN Id to complete the Partner Admin Link.

## Consequences

The Partner has an identity in each Customer which is used to configure PAL.
The Customer has a clearly named AAD Application which they control that signifies Partner Contribution.
The ephemeral credentials associated with the above AAD Application are short-lived and not exposed outside the automated process.
The Partner has no access to the necessarily privileged Application identity, thus satisfying the Zero Trust requirement.
Microsoft can see the relationship between The Customer and The Partner.