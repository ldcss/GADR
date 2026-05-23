# 6. OpenAPI guidelines

Date: 2021-02-18

## Status

Accepted

## Context

We feel the need to use a naming convention for OAuth scopes.

## Decision


When creating an OpenAPI based REST API, there are the guidelines to adhere to:

To get started, create a valid OpenAPI specification yaml file inside an [app folder](https://github.com/vwt-digital/operational-data-hub/blob/develop/coding_guidelines/adr/0003-repo-directory-structure.md).

Next, use the [OpenAPI generator](  https://github.com/OpenAPITools/openapi-generator) to generate you API server. This will create a Readme, requirements and an openapi_server folder with controllers, models, and a generated openapi/openapi.yaml file.

Normally OpenAPIGenerator is a write-once tool (any changes will be overridden by generating a new project.) However, changing requirements will force you to regenerate a project (Especially when the structure of the data changes.) To ensure a correct usage of the openapigenerator tool, perform the following steps:

### Instruct the SAST scanner to ignore generated files.

-   For flake8, these are:
    
    -   app/setup.py
        
    -   app/openapi_server/util.py
        
    -   app/openapi_server/models/*.py

-   For yamllint this is:
    
    -   app/openapi_server/\_\_init__.py
        
    -   app/openapi_server/openapi/openapi.yaml
        
    -   Any other files that need to be edited.

    

### Making changes to the OpenAPI spec.

Whenever you want to make changes to the specification, it is important not to edit the openapi_server/openapi.yaml file, this will be overridden by the generate command. It is better to change the user created source yaml file and regenerate the project. When generating, for now we'll only regenerate the models. Any other changes will need to be done manually. 


### Enable validate_responses.

To ensure that the Spec is honored, enable validate responses in the openapiserver/\_\_init__.py file (Example can be found [here](https://github.com/vwt-digital-solutions/snbplanningapi/blob/develop/api_server/openapi_server/__init__.py#L20).)

### Use models to your advantage.

To ensure correctness of the response returned by the API, the developer should always work with the models provided by the generator. A model’s to_dict method can be used to construct the response.

### Naming conventions.

Inside the controllers, operations should be named like so:

-   list_<object>s for the REST list operation (GET without id)
    
-   get_<object> for the REST get operation (GET with id)
    
-   create_<object> for the REST create operation. (POST without id)
    
-   update_<object> for the update operation (POST, PUT with id)


## Consequences
Regenerating only the models is a step in the right direction, but not perfect as it could lead to outdated controllers. In the future a solution as described in [This StackOverflow question](https://stackoverflow.com/questions/45680298/cleanest-way-to-glue-generated-flask-app-code-swagger-codegen-to-backend-imple/47554626#47554626) could be more desirable. 