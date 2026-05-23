# 1. Use PostgreSQL as Database
Date: 6/18/2018

## Status
Accepted

## Context
The API for CHIP needs some sort of persistence for storing its data. Although the data needs for the app are pretty lightweight, it's likely that they will grow in the future as new features are desired or more data is acquired. To this end, sticking with a simple, powerful, reliable, and flexible technology that is widely understood makes sense.

## Decision
A RDBMS fits this bill and PostgreSQL does so even more snugly. It's a top contender, it's free, it's currently the best supported traditional database for the Elixir/Erlang ecosystem and it's unparalleled at its geospatial capabilities.

## Consequences
There's more infrastructure to integrate with, stand up, and maintain with this approach as compared to using something like Mnesia, the built in database for Erlang/Elixir, but there's also less to learn and greater flexibility. 

