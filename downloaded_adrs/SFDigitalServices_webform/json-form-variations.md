# Example JSON (variations)
Below is an example of a form saved as a JSON object in the database.

```
{
  "settings":
    {
      "action":"",
      "method":"POST",
      "name":"My Form with variations"
     },
  "data":
    [
      {
        "label":"First Name",
        "placeholder":"placeholder",
        "help":"Supporting help text",
        "id":"first_name",
        "formtype":"g02", // for group of Name field
        "name":"first_name",
        "type":"text",
        "version:: "2", // Variation version
        "required":"true",
        "value":"John",
        "class":"custom-class"
      },
      {
        "label":"Middle Name",
        "placeholder":"placeholder",
        "help":"Supporting help text",
        "id":"middle_name",
        "formtype":"g02",
        "name":"middle_name",
        "type":"text",
        "version:: "2",
        "required":"true",
        "value":"S",
        "class":"custom-class"
      },
      {
        "label":"Last Name",
        "placeholder":"placeholder",
        "help":"Supporting help text",
        "id":"last_name",
        "formtype":"g02",
        "name":"last_name",
        "type":"text",
        "version:: "2",
        "required":"true",
        "value":"Doe",
        "class":"custom-class"
       }
      ]
}
```
