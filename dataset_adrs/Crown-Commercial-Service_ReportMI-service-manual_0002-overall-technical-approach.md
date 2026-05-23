# 2. Overall technical approach

Date: 2018-06-06

## Status

Accepted

## Context

The Data Submission Service is a new digital system for suppliers to submit
management information to CCS. It replaces the current Management Information
System Online (MISO).

This paper seeks approval for the overall technical approach for the new
service.

### Management Information System Online (MISO)
MISO is an online service run by CCS for suppliers to submit data about work
undertaken through CCS commercial agreements. Suppliers submit data on a monthly
basis via a complex Excel spreadsheet.

The data submitted through MISO is used to calculate the management fee that is
charged to suppliers. This data is also used by Commercial Agreement Managers
(CAMs) to help with management of suppliers and agreements as well as inform
future agreement design.

MISO was developed in 2011 with only minor updates since.

The service frequently experiences poor performance with frequent errors. It
delivers a poor user experience, and requires a large amount of manual work to
add new commercial agreements and new suppliers.

The number of transactions taken by MISO has increased significantly over recent
years, rising from around 5000 per month in 2015, to over 8000 per month
in 2018. Transactions peak around G-Cloud commercial agreement boundaries (with
nearly 10,000 transactions in June 2017). This increase puts a further strain on
an already stretched service.

### Estate in flux
The technology estate within CCS is in a state of flux. Several important parts
are being replaced over the next 6 months, including eSourcing (how commercial
agreements are established), Finance & HR and the roll-out of the Crown
Marketplace.

Additionally, there is ongoing work to replace the CCS website, develop the
organisation's data strategy, technical architecture and early plans to develop
and improve the identity and access management services.

### Data Submission Service Alpha
The Digital Services Team has been working on a prototyping phase to identify
options for a new service to replace MISO.

This phase has involved user research with suppliers and staff within CCS who
administer MISO. It's looked at ways of improving processes and investigated
potential technology choices.

The team is now ready to start producing a Minimum Viable Service with an aim to
take real data submissions from suppliers later this year. The medium-term aim
is to switch off the existing MISO service in 2019.

## Decision

The new service will need to have the following characteristics:

- **Scalability** - the service must cope with high peaks in demand -
particularly around submission deadlines. Outside of peak times, the service is
infrequently used. Over time, the number of transactions is likely to grow,
particularly with the introductions of G-Cloud 10, Digital Outcomes and
Specialists 3 and Dynamic Purchasing System (DPS) where suppliers can leave and
join a commercial agreement at any time.

- **Flexibility** - the service needs to collect different types of data for
different commercial agreements. This includes invoice data, contract data,
data to support decision making. Over time, CCS may need to collect different
types of data, particularly as agreements and industries change.

- **Adaptable** - as the CCS technical landscape changes, the service will need
to change along with it. For example, in future it will need to support a new
finance system, and potential integration with Crown Marketplace, eSourcing and
the CCS website.

These characteristics lend themselves to developing a system with small pieces
that can be easily iterated or replaced as requirements change over time.

The new data submission service will comprise the following pieces:

1. **Submission app** - a public facing front-end for suppliers to submit
returns. This will comprise a specially designed user-interface to make the
journey for suppliers as simple as possible, providing timely and useful
feedback to help reduce errors, using well-tested design patterns from the
GOV.UK toolkit alongside the CCS branding.

1. **Data storage layer** - to store the data submitted to CCS. This will act as
the 'core' of the new service, and the source of truth for submission data. This
will be accessed via an API, allowing other CCS services to use the data as
required.
1. **File transformation service** - a small service to take various file inputs
from suppliers, extract required data and store it in the data storage layer.
This service will need to support various file formats including custom Excel
documents, CSVs, PDFs and Open Office formats.

1. **Data validation service** - a small service to validate data submitted by
suppliers and calculate the approximate management fee required. This will need
to adapt over time as different data is collected from suppliers and different
methods of calculating the management fee are introduced.

1. **Notification service** - a small service to manage sending of notifications
to users. This service will automatically generate notifications, and handle
responses (eg bounces, out of office replies etc), reducing the burden on the
CCS support staff. The service will integrate with GOV.UK Notify for sending
notifications.

1. **Data exports** - a series of regular 'batch' data exports to provide
submission data to other systems, including the Data Warehouse and the legacy
finance system.

1. **Administration app** - a front-end for CCS staff to support the operation
of the data submission service. This will comprise a customised interface to
make support tasks as simple as possible, allowing staff to focus on more
important work.

1. **Onboarding app** - a front-end for CCS staff to manage the onboarding of
new commercial agreements and suppliers. This will compromise a customised
interface to allow CCS to specify commercial agreement data collection
requirements, validation rules, management fee calculation formula, and handle
the onboarding of new users/suppliers.

Each of these components will make use of the most appropriate and simplest
technology to perform the required functions and will be integrated using well
defined JSON APIs. Each piece should be easy to maintain, iterate and enhance,
and should also be easy to replace in future.

Where possible, the service will make use of managed cloud services to provide
features such as automatic scaling, high availability and resiliency.

The service will make use of existing government and CCS services where possible
- for example GOV.UK Notify, the Supplier Registration Service, Digital
Marketplace etc.

## Consequences

To establish the new data submission service, CCS will need to:

* Commission a team to produce and integrate the various components, including
future support and operation. There is a contract in place with a supplier
(through the Digital Outcomes and Specialists Framework) which covers the
development of an MVP service.

Producing a new service comprised of small pieces that can be iterated, improved
and replaced over time will:

* Allow CCS to take advantage of pay-as-you-use cloud technologies, which can
scale up as needed to handle peaks, but can also scale down to support periods
of low use. This will make the most efficient use of the infrastructure
available. Many cloud services now charge by the millisecond, rather than by
month or year.

* Allow CCS to quickly and cheaply change or replace components as the rest of
the estate evolves - for example we will be able to replace the Finance system
export with real-time APIs as the replacement Workday service becomes available.

* Reduce the burden on CCS staff by automating existing manual tasks and
reducing the amount of support required

* Make submission of data from suppliers easier by providing: a simpler user
interface using recognisable design patterns, more helpful error messages,
quicker feedback loops and a more stable service.
