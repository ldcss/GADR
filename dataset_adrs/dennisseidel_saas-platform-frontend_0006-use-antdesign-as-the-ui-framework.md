# 6. Use AntDesign as the UI Framework

Date: 2019-02-07

## Status

Accepted

## Context

To speed up the UI development we need to select a UI Framework that has a good community as well as good functionality.

## Decision

We use Ant Design as the UI Framework.

## Consequences

because it allows me to use features like [AntDesign landing](https://landing.ant.design/docs/use/getting-started), AntDesign Mobile including support for react native. It is well suported by Ant/Alibaba. The risk is that not all documentation is english but chinise, therefore I need to ensure that I can work with google translate on it. Further it often integrates with the Ant specific stack like dva and umi, so I need to make sure not to couple myself deeply to those.

## Links

* Install: https://deploy-preview-14385--ant-design.netlify.com/docs/react/use-with-create-react-app
* Antd Landing Guide: https://landing.ant.design/docs/use/getting-started (use google translate)
