# Form field groups and variations
All form fields are statically bound. That means when a field needs an alternative storage and/or presentation, it's not possible. For example, the "Name" field is a textfield for a full name, it can't distinguish firstname, middlename, and lastname. We need form field variations to allow flexibility in form building.

## Two Unique Problems to Solve
* A radio or checkbox field needs to optionally have an "Other" input field which consists of a label and freeform text input. All existing radio/checkbox functionality must be preserved.
* Address can exist as a form group which can contain any combination of street address, city, state, zip, etc. It would be useful to have pre-made templates of form groups.

## Considered Alternatives
* Create additional versions of the form field, treat each version as a new form field type.
* Optional consideration: Create alternative(s) under each form field.

## Decision Outcome
* Create additional versions for each individual form field and treat them accordingly in the HTML helper. "version" will be a new attribute, "formtype" and the rest of the JSON will stay the same.
```
Example of field variation
	"data":
			[
				{
					// otherless radio, notice no version attribute (default)
					"label":"Icecream?",
					"placeholder":"placeholder",
					"help":"Supporting help text",
					"id":"radio_1",
					"formtype":"s08",
					"name":"icecream",
					"radios":"yes\nno",
					"type":"radio",
					"required":"true",
					"class":"custom-class"
				},
				{
					// radio with other
					"label":"Icecream flavor?",
					"placeholder":"placeholder",
					"help":"Supporting help text",
					"id":"radio_2",
					"formtype":"s08",
					"name":"icecream_flavor",
					"radios":"vanilla\nchocolate",
					"type":"radio",
					"version": "other", // Variation version
					"required":"true",
					"class":"custom-class"
				},
			]
```
* Add a new "groupid" attribute to the saved JSON form data object.
* The new "groupid" will act as a dynamic id which will group all fields with the same groupid together.
* The "groupid" value will be generated once it is dragged/added to the editing form and be a concatenation of the form group template name (see below) and an incremental number, ie: g_address_streetonly_1
* Versions of form groups do not depend on each other.
* Added form groups to the form will be non-editable but will otherwise appear as regular fields within the JSON form data object.
```
Example of form data with a group
	"data":
			[
				{
					// pizza is not in the group
					"label":"Pizza",
					"placeholder":"placeholder",
					"help":"Supporting help text",
					"id":"pizza_1",
					"formtype":"s08",
					"name":"pizza",
					"radios":"unpopular\nreally unpopular",
					"type":"radio",
					"required":"true",
					"class":"custom-class"
				},
				{
					"label":"Icecream?",
					"placeholder":"placeholder",
					"help":"Supporting help text",
					"id":"radio_1",
					"formtype":"s08",
					"name":"icecream",
					"radios":"yes\nno",
					"type":"radio",
					"required":"true",
					"class":"custom-class",
					"groupid":"g_icecream_all_1"
				},
				{
					"label":"Icecream flavor?",
					"placeholder":"placeholder",
					"help":"Supporting help text",
					"id":"radio_2",
					"formtype":"s08",
					"name":"icecream_flavor",
					"radios":"vanilla\nchocolate",
					"type":"radio",
					"version": "other", // Variation version
					"required":"true",
					"class":"custom-class",
					"groupid":"g_icecream_all_1"
				},
			]
```
* HTML Generation: Create a helper listing of form group templates which will describe which form fields belong to which predefined group.
* Format would be a JSON with an array of formtypes: each formtype would adopt the same attributes as the existing form field JSON.
* Undefined attributes would be filled in by the default value and defined attributes would override the default.
* Naming groups will start with g_groupname_templatename
```
Example of form group templates
	"address" : {
		"full" : [
			{
				"formtype":"c08",
				"label":"Address 1",
			},
			{
				"formtype":"c08",
				"label":"Address 2",
			},
			{
				"formtype":"c10", //city
			},
			{
				"formtype":"s14", //state
			},
			{
				"formtype":"c14", //zip
			}
		],
		"streetzip" : [
			{
				"formtype":"c08",
			},
			{
				"formtype":"c14", //zip
			}
		]
	}
```

## Pros
* Flat JSON object, easier to deal with.
* Reusing existing form fields will be more flexible in the future, allowing for dynamically grouping form fields in the future.
* Hardcoding labels and not allowing the user to edit groups will enforce best practices and allow for easy pre-translated forms.
* No changes to the database, that's a good thing.

## Cons
* By not hard-coding a full HTML template, it will be harder syntax to read/edit for those used to just editing HTML.
* Also, not hard-coding a full HTML template will be more work and development time initially.
* By making a flat JSON object, we are not able to make an infinite amount of nested form groups.

## Tasks and things to consider
* Update the HTML helper class for variations.
* Make sure the new JSON data structure supports easy UI development, possibly simplify it to YAML or create a function to convert from JSON to YAML and vice versa.

## See sample JSON object (deprecated, updated samples are inline)
* [json-form-variations.md] (json-form-variations.md)