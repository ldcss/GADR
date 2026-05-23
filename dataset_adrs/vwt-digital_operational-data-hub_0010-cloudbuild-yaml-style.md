# 10. Cloudbuild.yaml style

Date: 2021-04-12

## Status

Accepted

## Context

We feel the need to use a specified cloudbuild.yaml style.

## Decision

We identify different rules that should be followed when creating or editing a cloudbuild.yaml file:

### 1. Start of file
Since cloudbuild.yaml is a yaml file, the file should always start with `---`.

### 2. An ID for every step
Make sure that every step has an ID. Rules for this ID:
* It is a short but clear title containing an explanation of what the step does, a maximum of 50 characters should suffice.
* The words in the ID should be divided by `-`.
* If you cannot explain the step in 50 characters, add a comment above the step explaining what the step does.

### 3. Avoid "waitFor" field
Try to avoid using the `waitFor` field as much as possible since not using it makes sure that the steps are done in the order they are put in the cloudbuild.

### 4. Empty lines between build steps
Use empty lines between build steps to increase readability.

### 5. Order of steps
The following rules should be followed when deciding on the order of the steps in the cloudbuild:
* The first step of the cloudbuild should always be the deployment of the data catalog.
* The subsequent steps should be the cloning of the necessary Github repositories.
* Cloud function permissions should be set in the build step after the deployment of the cloud function.
* If a scheduler is deployed in a step and it schedules a specific function which is also deployed in the cloud build, the step containing the deployment of the scheduler should be deployed right after the step which deploys the permissions of the cloud function.
* If a chain test is added, make sure that it is the last step in de cloudbuild.

### 6. Avoid if-else statements based on branches
Avoid if-else statements based on branch names.

### 7. Build container
Always use `'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'` als build container (in the `name` field of the step). Different entrypoints can be used with this container.

### 8. Bash pipe
When using bash as entrypoint in a cloud build step, one should always use a pipe.

### 9. Function call in step
If a function call is done in a step, its command plus subcommand should be on one line while its options or flags should be defined on separate lines. One should also use the long options if they are available, e.g. `-q` becomes `--quiet`.

### 10. Do not use gcloud as entrypoint
Do not use `gcloud` as entrypoint but use bash instead when having to call gcloud functionalities.

### 11. Cloud scheduler deletion
When deploying a cloud scheduler, the old "version" of this scheduler should first be deleted before redeployment.

### 12. One line commands without bash entrypoint
When a step only has one line and does not have a bash entrypoint, there are two ways you can define the step. Below is an example of a step where a github repository is cloned.
* ```yaml
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'
    id: 'cloning-repository'
    entrypoint: 'git'
    args:
      - 'clone'
      - '--branch=git-branch'
      - 'github-repository-url'
  ```
* ```yaml
  - name: 'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'
    id: 'cloning-repository'
    entrypoint: 'git'
    args: ['clone', '--branch=git-branch', 'github-repository-url']
  ```

## Example
```yaml
# Deploys function that does something
- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'
  id: 'deploy-function'
  entrypoint: 'bash'
  args:
    - '-c'
    - |
      gcloud functions deploy function-func \
        --entry-point=python_entrypoint \
        --runtime=python37 \
        --trigger-http \
        --project=project-id \
        --region=region \
        --max-instances=1 \
        --timeout=integer \
        --set-env-vars=ENV=environment_var
  dir: 'git-repo/functions/function'

- name: 'gcr.io/google.com/cloudsdktool/cloud-sdk:latest'
  id: 'deploy-permissions-function'
  entrypoint: 'bash'
  args:
    gcloud functions set-iam-policy function-func \
        --region=region \
        --project=project \
        permissions.json
```

## Consequences
