# 5. How to deal with workspaces

Date: 2020-08-12

## Status

Accepted

## Context

In LifeCycle we use a 2 step approach to share the data within the LifeCycle project.

**Step 1** - Datasets containing all the harmonised data within LifeCycle
- lc_core_gecko_1_1 - *projects in Opal, workspaces in the Armadillo*
  - 1_1_core_non_rep_1_1 - *tables in Opal, R data.frame objects in Armadillo*
  - 1_1_core_yearly_rep_1_1
  - 1_1_core_monthly_rep_1_1
  - 1_1_core_trimester_rep_1_1
- lc_outcome_gecko_1_1 - *projects in Opal, workspaces in the Armadillo*
  - 1_1_core_non_rep_1_1 - *tables in Opal, R data.frame objects in Armadillo*
  - 1_1_core_yearly_rep_1_1
  - 1_1_core_monthly_rep_1_1
  - 1_1_core_trimester_rep_1_1

**Step 2** - Study specific datasets which contains only the variables you want to expose
  - lc_core_gecko_1_1 - *projects in Opal, RData files in the Armadillo*
    - 1_1_core_non_rep_diabetes_1_1 - *views in Opal, R data.frame objects in Armadillo*
  - lc_core_gecko_1_1 - *projects in Opal, RData files in the Armadillo*
    - 1_1_core_non_rep_diabetes_1_1 - *views in Opal, R data.frame objects in Armadillo*

### Versioning
In the current version scheme of LifeCycle we distinguish 2 versions: 
- dictionary version 
- data version

The scheme is as shown below:

`y_y_#dictionary_kind#_#cohort#_x_x`.

The `y_y` version = the dictionary version (data model version)
The `x_x` version = the data version (version of the data release)

### Accessing data
Based upon the cohort guidelines on exposing data to researchers one way or the other is chosen to give researchers access to the data.
In Opal you need both datasets. 
- a dataset containing all the harmonised data
- (if applicable) views to expose specific datasets

These views do not contain the data, only the representation of the variables. In Opal you can manage permissions per view, which makes it possible to put all the tables and views related to one dictionary version in one project.

## Decision
Within the Armadillo we have the ability to nest the dictionaries. Which makes it possible to specify the dictionary version and data version on a sublevel. The structure in the Armadillo will be used in the following manner:

- gecko-all 
  - 2_1-core-1_0
    - non-rep
    - yearly-rep
    - monthly-rep
    - trimester-rep
  - 1_1-outcome-1_0
    - non-rep
    - yearly-rep
    - monthly-rep
    - weekly-rep
- gecko-diabetes
  - 2_1-core-1_0
    - non-rep
    - yearly-rep

We currently do not support more than 1 level of nesting folders in a project.

Three levels can be distinguished:
### 1. Project level
This can be all the data or a study specific data. On this level we can manage permissions.
### 2. Folder level
The second level contains the collection of data frames or tables you want to expose. This usually contains the version of the model and data release as well.
### 3. Table level 
You can interpret this level as the data level containing tables that can be queried.
  
## Consequences
- You can only manage permissions on the toplevel. Which results in a project per study or cohort.
- Versioning is not implemented in the tables. Which results in minimal impact for the researcher to upgrade to a new model or data version
- You cannot load different versions of the same data in one R session.
