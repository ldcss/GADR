# Use 1Password for sharing secrets

* EASi engineers occasionally need access to secrets to test the app locally.
  For example, API keys for services the app depends upon. These secrets rotate
  periodically, sometimes outside of our control, and sometimes without
  warning. This creates a challenge: how can we share an updated secret in a
  secure way with minimal interruption to ongoing app engineering work?

* Decision drivers:
  1. EASi engineers need to be able to stay up-to-date on secret values that
     are required for app development.
  1. There should be a central source of truth for the secrets.
  1. The scheme for storing, sharing, and retrieving secrets should be
     consistent with our understanding of best security practices.
  1. The scheme should also be user-friendly and accessible without assuming
     any knowledge of back-end infrastructure or overly complex authentication
     mechanisms.

## Considered Alternatives

* Email
* Slack DMs
* 1Password
* AWS SSM / ParameterStore

## Decision Outcome

Chosen Alternative: Use a 1Password vault for sharing secrets.

* 1Password allows us to control access to the secrets repository on a per-user
  basis, and updates to any secret will be available to other users on the
  vault immediately.  With a separate vault within 1Password, we need not share
  secrets with other Truss personnel who are not assigned to the project.
* 1Password also has familiar and user-friendly graphical interfaces via the
  web and a multi-platform desktop application.
* Access to secrets can be revoked as quickly and as easily as it was granted.

Consequences:

* We will need to create a vault, which takes time and costs money.
* Some synchronization will be required on how to use the vault and what
  secrets to store in it.
* Secrets that are required by the easi-backend app will have to be updated in
  SSM anyway, which means changing them requires updating the value in two
  places (1Password and SSM).

## Pros and Cons of the Alternatives

### Email

* `+` Fast.
* `-` Poor access controls: once an email is sent, its contents cannot be recalled.
* `-` Emails can be easily shared with a wide audience inadvertently, resulting
  in a pervasive risk of uncontrolled disclosure.
* `-` If we have to manage any secrets that cannot be rotated, there will be no
  way to guarantee that sent emails are burned after reading: rather, they will
  likely live on in the archived email of whoever received them.
* `-` There would be no central source of truth on what the current secrets
  are, which complicates onboarding/off-boarding, engineers returning from
  vacation, etc.

### Slack DMs

* `+` It's easy to find people in Slack, and we all use it.
* `+` Only two people are in a DM thread. Although it is possible to share
  contents of a DM conversation, it is not as easy to do so inadvertently as
  with email.
* `-` Due to CMS record-keeping policies, DMs cannot be deleted and may be
  subject to subpoena or FOIA requests.
* `-` There is no central source of truth.

### 1Password

* `+` Per-user access controls.
* `+` Since 1Password is specifically designed for the purpose of securely
  storing and sharing secrets, it provides a good user experience and is
  already in wide use.
* `+` We can restrict the vault to project engineers according to the principle
  of least access.
* `+` 1Password enables sharing secrets without breaking the security model.
* `-` We have to create a vault, which costs money.
* `-` Some secrets will have to be updated in 1Password and SSM when they
  change, such as API keys.
* `-` We have to grant and revoke everyone's access individually.

### AWS SSM / ParameterStore

_See also:_ [Use AWS SSM Parameter Store for Config/Secrets management](./0008-ssm-for-configsecrets.md)

* `+` Provides a _single_ source of truth: Updates in SSM are automatically
  shared with the easi-backend app.
* `+` We already depend on ParameterStore to store secrets for the app, so
  there is no new point of potential security failure.
* `-` Spin-up for a new engineer on gaining access to SSM is time consuming and
  complex.
* `-` Neither the web console nor the cli interface are user-friendly and
  intuitive to the uninitiated.
