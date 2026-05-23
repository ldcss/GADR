# Static file server

This project is a coding challenge which aims to server static files in java via HTTP without framework support.

## Usage

Command line overwrites set environment variables.

Command line options: 

```
-a,--address <arg>       listen address - default: 0.0.0.0
-dir,--directory <arg>   directory to server files - default: /var/www/html
-h,--help                print help
-p,--port <arg>          listen port - default: 8080
```

Environment Variables:
```
PORT                listen port
ADDRESS             listen address
DIRECTORY           directory to server files
```

## Docker

I would recommend using [buildpacks](https://buildpacks.io/) to create a running image like so:

`pack build file-server --path . --builder gcr.io/buildpacks/builder:v1 --env GOOGLE_RUNTIME_VERSION=14`

This creates a docker image names "file-server". 

## Notes

This is just a proof of concept and does not implement the full HTTP Standard. For example the socket connection gets
always closed no matter what. For that reason this project uses a more functional approach over object orientation.

I decided not to use a template engine for my single html page and relied on java strings to do so.
Sadly text blocks are still in preview and disabled by default.

Some functionality is not tested since it requires a connected Socket, and I did not implement Integration testing here for now.  
