# 6. Field Formats And Naming Conventions

Date: 2020-01-27

## Status

Proposed

## Context

We desire consistency across the API, so should provide a set of sensible naming conventions which we will adhere to and require our clients to do likewise

## Decision

### Naming conventions

Our field naming standard is closely follows the [JSON API](https://jsonapi.org/format/#document-member-names) v1.0 definition, and this spec should be consulted for a full list of allowed, disallowed, and reserved characters.

In brief, field names:

* Are case sensitive
* Must contain at least one character, and begin with an a character
* Use only [non-reserved](https://jsonapi.org/format/#document-member-names-reserved-characters), URL-safe characters

The following additional standards are also in force in `application/vnd.opg-data.v1`:

* Field names are all lower case
* Must begin with an an alpha chatacter [a-z]
* We use an underscore to separate compound field names
* U+0020 SPACE, “ “ is not permissible in a field name

### Field data formats

* integers are integers
* boolean are represented by `true` and `false`
* null values are represented by `null`
* empty arrays are always shown, represented by `[]`
* To represent time and date. The government mandates using the [ISO 8601](https://www.gov.uk/government/publications/open-standards-for-government/date-times-and-time-stamps-standard) standard to represent date and time in your payload response. This helps people read the time correctly.

Use a consistent date format. For dates, this looks like 2017-08-09. For dates and times, use the form 2017-08-09T13:58:07Z.

### Use Unicode for encoding

The Unicode Transformation Format (UTF-8) standard is mandatory for use in government when encoding text or other textual representations of data.

```json
{
    "data": {
        "id": "123XYZalways_a_string",
        "integer": 1,
        "string": "Like so",
        "boolean": true,
        "boolean": false,
        "date": "1977-03-08",
        "datetime": "1977-03-08T02:03:52Z",
        "explicit_empty_arrays_are_shown": [],
        "explicit_null_for_everything_else": null,
        "use_underscores_in_naming": true,
        "fields_all_lower_case": true,
        "fields_Are_Case_Sensitive": true
    }
}
```

## Consequences

Consistency is greatly improved
