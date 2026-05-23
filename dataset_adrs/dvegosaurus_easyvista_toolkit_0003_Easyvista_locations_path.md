# Easyvista's location_path
date : 2019/10/03

## Status
accepted

## Context
We need to be able to assign a location when creating an employee and to have autocompletion that list all availables location on cmdlet.

But there are issues related to the location_path attributes on users in easyvista's API.
According to the documentation ([employees creation](https://wiki.easyvista.com/xwiki/bin/view/Documentation/REST+API+-+Create+an+employee)) the field can't be
used in a request to create an employee.

Also filtering on location_path when querying /locations does not work : queries ignore the field an simply returns the 100 first results.

## Decision
Instead of using the [search option](https://wiki.easyvista.com/xwiki/bin/view/Documentation/REST+API+-+See+a+list+of+locations) from the API we will rely instead on powershell
Where-Object cmdlet with the max_rows parameter from the API.

## Consequences
### Pros
- easier for powershell user's to read the code
### Cons
- API requests will be slower
- we will need to implement a way to allow users to adjust the max_rows value.
