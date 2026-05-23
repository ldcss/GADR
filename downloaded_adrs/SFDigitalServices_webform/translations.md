# Translations
The Form Builder must be able to present itself in different languages. There must be a way to serve custom human translated content but it would be prudent to also include pre-translated content for common fields like name, phone number, address, etc. Lastly, there should be a fallback to use an API-based machine translated service.

## Internal Considerations
* Spoke with Nicole and Anthony about SF.gov translation services and various online translation services.
* Discussed with the team and came to the conclusion that we do not want to require code access just to add/update translations.
* This leaves two primary approaches: file uploads w/ repository or database entries.
* Talked with Henry about different data structures to store translation including scenarios for additional tables and columns.

## Considered Alternatives
* The easiest solution would leverage Lumen/Laravel localization features out of the box: https://laravel.com/docs/5.8/localization
* However, because form authors will need a way to input translations through the app, additional work must be done to accomodate more than the template files in laravel
* Using the Lumen/Laravel default file system with a file uploader might be the easiest solution but instantly becomes more complicated when editing files which also must be formatted in PHP syntax:
```php
<?php

return [
    'welcome' => 'Welcome to our application'
];
```
* A package exists to load and override file translations from the database: https://github.com/spatie/laravel-translation-loader

## Preliminary Decision Outcome
* Use the translation loader to store language lines in the database.
* Use the file system to store localized strings of hard-coded version templates.
* The order to fetch will be human translated (database) -> pre-translated (file template) -> machine translated (cached, database) -> machine translated (API)
* MVP will only require human translated and pre-translated layers.

## File Structure
```
/resources
    /lang
        /en
            template-name.php
        /es
            template-name.php
```
* Template-name would be determined by formType-version, ie: s14-fullName

## Database
* Generate a new table named language_lines
```php
        Schema::create('language_lines', function (Blueprint $table) {
            $table->increments('id');
            $table->string('group');
            $table->index('group');
            $table->string('key');
            $table->text('text');
            $table->timestamps();
       });
```
* Group column will be used as form_id.
* Key should be field_id and attribute, ie: phone.label.
```php
LanguageLine::create([
   'group' => '351',
   'key' => 'name.label',
   'text' => ['en' => 'Name', 'es' => 'Nombre'],
]); 
```

* To retrieve name for form 351: trans('351.name.label');

## Additional Considerations
* Anytime a new field is added or removed from a form, or an id is changed, the language_lines should be synced.
* We will also need to create a full form string export and add a localization toggle for preview.
* Lumen has a translator package to generate and translate data: https://github.com/jcarrizalez/translator
* Google translate looks feasible initially but other translation API services may fit better.
