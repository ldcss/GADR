# Use external config file
The spring framework looks for the `config/application.yml` next to the `spring-boot-app.war` for external configuration.

## Considered Alternatives

* Define all configuration inside `resources/application.yml`
* Define all configuration inside `config/application.yml`
* Define some configuration inside `config/application.yml`

## Decision Outcome

* Chosen Alternative: Define some configuration inside `cnfig/application.yml`

## Pros and Cons of the Alternatives <!-- optional -->

### Define some configuration inside `cnfig/application.yml`
Configuration properties that are final for an application can be defined inside `resources/application.yml` and will be packed into the war file.

Configuration properties that are changing all the time and depend on the end user (authentication, names, urls) should be defined in `config/application.yml`.

#### Intellij setup
- Open `ctrl + shift + alt + s` 'Project Setting' > Modules
- Click  Spring > 'Customize Spring Boot (Icon)'
- Add `config/application.yml`
