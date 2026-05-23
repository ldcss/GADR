# 7. Starting a Flask App

Date: 2021-03-11

## Status

Accepted

## Context

We feel the need to set a standard for starting a Flask App.

## Decision

There should be only one entrypoint to start a Flask App. When using [openapi-generator](https://github.com/OpenAPITools/openapi-generator) this entrypoint defaults to `__main__.py`, which should look similar to:

```
#!/usr/bin/env python3

import connexion

from openapi_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Petstore API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()
```



A Flask app can be started locally by executing running `python __main__.py`.

When running a Flask app in Google App Engine (GAE), the `app.yaml` should use `gunicorn` to start Flask:

```
---
runtime: python37
entrypoint: gunicorn --pythonpath __main__.py -b :$PORT __main__:app --workers 4
instance_class: F4
```

Note: `gunicorn` is automatically available in the GAE Python runtime environment.
