# Extraction of data by Time

* Status: [accepted]

## Context and Problem Statement

The data extraction w/ transaction timestamp from Koshvani platform is a challenging task.
- The temporal data directly available on the platform is not easy to extract
- The validation of temporal data to ensure accuracy depends on factors
    - Districts/Treasuries which have updated their data
    - Data/Time of data upload vs extraction from departments

## Decision Drivers

The platform shares the data updation status for each treasury at a daily level. But due to the factors stated above, an in-depth check and analysis is required to extract the correct data.

## Decision Outcome

- Do a daily level data extraction from the platform
- Conduct analysis to identify daily, weekly and monthly expenditure numbers
- Select the accurate time period and mention methodology for the same
- Ignore previous time period missed in this analysis.

Conduct the analysis on accurate data collection at in November, 2020 to take decision.
