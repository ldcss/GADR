# 1. GET_CURRENT_MONTH_COURSE_2018-05-14

Date: 2018-05-14

## Status

Accepted

## Context

We need a way of getting all courses for the current month, and year.

## Decision

For May(2018) E.g: 
```
[{ 
    date:"2018-05-01", course_dates:{...}
},{
    date:"2018-05-02", course_dates:{...}
},{
    date:"2018-05-03", course_dates:{...}
}, ...]
```

## Consequences

### TODO:

- [ ] Parse year structure (https://econ.ubbcluj.ro/documente2018/Structura%20anului%20universitar%202018-2019,%20RO,EN,FR,%20nivel%20Licenta%20si%20Master,%20IF.pdf)
- [x] Create models for year structure
- [x] Create endpoint to get all date to a specific year
- [ ] Create endpoint to get all date to a specific month
