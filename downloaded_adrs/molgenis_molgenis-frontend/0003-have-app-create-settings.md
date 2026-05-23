# 3. Have App create app setting table 

Date: 2020-09-23

## Status

Accepted

## Context

Apps (for example the data-explorer-2 or the biobank-explorer) may need settings data to function properly. As these settings are dynamic (may be changed at run time), and may change between deployments these settings need to be stored somewhere (molgenis database). This poses two problems; 1) how to link the app with the settings data, 2) how to control access to the settings.

## Decision

We leave it up to the app to create the settings entity. Each app creates 0 or 1 settings entities. By default everyone can read the settings data. Depending on the app the entity contains 1 or more rows ( in case of multiple rows the app is responsible using the correct row(s) in each context). 
Rejected alternatives:

- Add settings via bootstrapped entity in molgenis core; This was deemed as insufficiently flexible due to the dependance on Java knowledge and (possible major version) core release.  
- Use of app manager; App-manager does not facilitate an automated deployment process. App manager restricts the app architecture and settings structure.
- Use of entity meta data: Does not allow for settings per 'entity and app' combination. For instance the dataexplorer needs n settings rows or n tables.
- Proxy settings request to external repository; Deemed as hard to manage, app and proxy settings need to be kept in sync, also requires knowledge of proxy (nginx, apache) to configure.

## Consequences

If an app needs settings data to function properly, these settings need to be created. If settings data may not been seen by some users/roles the app developer must use the permission api to restrict access. An app should use no settings or default settings (stored in the app code) to be releasable without any dependency. Settings data may be created using the default molgenis features (emx, cli script, api, webapp). Just like any of the molgenis entity a settings row may contain a single attribute ( type text) that uses a json blob to store the settings data. 
