# Feature Toggling

**Status:** Accepted

## Context

As the app is a live for the client we need feature toggle functionality to allow to us work on features without them affecting the functionality of the live system.
- Allow multiple pairs to work on same feature which contain multiple stories that will need to be merged with the master branch before the full feature is implemented
- Feature toggling needed to be a light weight solution
- Feature toggles needed to have different values per enviroment
- On 5/06/23 Feature toggles for the biopsy form have been removed because the biopsy feature works in all environments

## Decision

To implement feature toggles we used github secrets (in links) and feed them into the app using the workflow yml files.
In the yml files under the build production bundle as below
    e.g.
    - name: Build production bundle
            env:
            REACT_APP_BIOPSY_FORM_FEATURE_TOGGLE: ${{secrets.BIOPSY_FORM_FEATURE_TOGGLE_PROD}}

and also in the enviroment for the end to end tests
    e.g.
    - name: Run end to end tests
            env:
            REACT_APP_BIOPSY_FORM_FEATURE_TOGGLE: ${{secrets.BIOPSY_FORM_FEATURE_TOGGLE_PROD}}

We then are then able to access the values in the react using process.env
    e.g.
    const biopsyBannerFeatureToggle = (process.env.REACT_APP_BIOPSY_FORM_FEATURE_TOGGLE === "TRUE");

Setting the secret to TRUE makes the feature appear


## Links

- https://github.com/BMMRO-tech/BMMRO/settings/secrets/actions
