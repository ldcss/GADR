# Selection of Dashboard Tooling

* Status: [proposed]

## Context and Problem Statement

The GEWST project with HAQ: CRC has a platform development component, which includes creating exploratory dasboard and conducting analysis on an interactive dashboard.

## Decision Drivers

### Platform Development Requirements

According to the plan, the data platform comprises of the following components:

- **Data Mining Component**: Developing the infrastructure and other components for mining data from the Koshvani platform. These will be developed following ethical data mining practices and will ensure that the data is mined responsibly from the Koshvani platform.
- **Data verification component**: This will ensure that the results produced by the Data Mining Component are verified and thoroughly tested by manual & automated processes before they’re released as part of the platform.
- **Data sharing and Exploratory Data Analysis (EDA) component**: Sharing the data, qualitative and quantitative research with the community and will also ensure that users can perform basic EDA on the data hosted on the platform.
- **Data Visualization Layer/Component**: Develop an interactive dashboard containing dynamic data visualizations to track and explore girl education and well-being spending for data collected in the development process.

### Other Drivers

- The bandhus in the Public Finance team are already occupied on OBI and OCP project.
- There is still no clear direction or plan what the tool will look like.
- There might be numerous research routes and iterations before finalisation.
- Data stories and analysis will play a big part in creating the final platform.

## Considered Options

| Option | Pros | Cons |
|---|---|---|
| `Shiny` Dashboard | - Flexibility of visualisations and story telling<br> - Decreased dependency on occupied bandhus. | - Time consuming process though easy to build. |
| `UBE` Dashboard | - Easy to replicated various charts / CMS from UBE stack. | - Lack of clear direction and dependency on Sherya. |
| `New` Dashboard | - Flexibility of visualisations and story telling<br> - Enhanced possibilities and skillsets. | - Lack of clear direction and dependency on Shivam. |

## Decision Outcome

You can track the decision updates / inputs on the following [issue](https://github.com/CivicDataLab/up-fiscal-data-shiny/issues/1).
