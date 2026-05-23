---
title: Accepted log
---

## Currently accepted records

{% assign subpage = site.pages | where: 'status', 'accepted' %}

{% for item in subpage %}* [ADR-{{ item.adr }}]({{ item.url}}) - {{ item.title }}
{% endfor %}

## Currently proposed records

{% assign subpage = site.pages | where: 'status', 'proposed' %}

{% for item in subpage %}* [ADR-{{ item.adr }}]({{ item.url}}) - {{ item.title }}
{% endfor %}

<!-- ## Superseded records -->

<!-- ## Rejected records -->

<!-- ## Deprecated records -->
