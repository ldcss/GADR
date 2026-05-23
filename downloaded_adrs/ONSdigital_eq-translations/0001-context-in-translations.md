# 1. Context in Translations

## Context

For some translatable strings, we create a message context (`msgctxt`) that contains the question text. This means strings can be translated in the context of the question being asked. There are two issues with this approach:

- For some elements the context is incorrect. For example, the context for an answer guidance title is `"Answer for: {question_text}"`.
- Most translatable strings at the question level and below don't have context. This causes problems when the English text doesn't vary between question variants, but the translated text needs to - https://trello.com/c/JEdbgtlT/3538-e-translations-add-context-to-all-child-elements-of-a-question-m

## Decision

- Remove the current message context `Answer for: {question_text}`.
- Use a new `Question: {question_text}` message context for all translatable properties within a question other than title. This allows any text within a question to vary based on the question.
- Add a new `Type: {property_type}` comment for every string extracted based on the values in the table below e.g. `Type: Question definition list item`. This helps a translator understand what they are being asked to translate.

  | JSON Path | Type | Notes |
  |-----------|------|-------|
  | `$.title` | Questionnaire title | |
  | `$.legal_basis` | Questionnaire legal basis | |
  | `$.messages` | Global answer error message | `message` rather than `messages` as each message is an individual translation |
  | `$.sections[*].title` | Section title | Used for section summaries, final summary and the hub |
  | `$.sections[*].repeat.title` | Section title (repeating section) | |
  | `$.sections[*].summary.items[*].title` | Custom section summary item title | |
  | `$.sections[*].summary.items[*].add_link_text` | Custom section summary list add link | |
  | `$.sections[*].summary.items[*].empty_list_text` | Custom section summary empty list text | |
  | `$..groups[*].title` | Group title | Used as heading in summaries |
  | `$..blocks[*].title` | Block title | Deprecated? |
  | `$..blocks[*].summary.title` | List collector summary heading | Deprecated when section summary blocks are removed from section definitions. |
  | `$..blocks[*].summary.item_title` | List collector summary item | Defines how to form the string to summarise each item in the list. Strictly speaking this doesn't need to be translated for all current usages |
  | `$..add_block.cancel_text` | List collector add block cancel link | |
  | `$..content.title` | Content page heading | The main heading on a Content page |
  | `$..content.contents[*].title` | Content page contents title | |
  | `$..content.contents[*].description` | Content page contents description | |
  | `$..content.contents[*].list` | Content page contents list | |
  | `$..question.title` | Question text | |
  | `$..question.description` | Question description | |
  | `$..question.instruction` | Question instruction | Instructions for field interviewers |
  | `$..question.definitions[*].title` | Question definition link | |
  | `$..question.definitions[*].contents[*].title` | Question definition title | |
  | `$..question.definitions[*].contents[*].description` | Question definition description | |
  | `$..question.definitions[*].contents[*].list` | Question definition list  | |
  | `$..question.guidance.contents[*].title` | Question guidance title | |
  | `$..question.guidance.contents[*].description` | Question guidance description | |
  | `$..question.guidance.contents[*].list` | Question guidance list | |
  | `$..answers[*].validation.messages` | Answer error message | |
  | `$..answers[*].label` | Answer label | |
  | `$..answers[*].description` | Answer description | |
  | `$..answers[*].playback` | Relationships playback template | Used for playback before a relationship is chosen e.g. "{person2} is {person1}'s ..." |
  | `$..answers[*].options[*].label` | Answer option | |
  | `$..answers[*].options[*].description` | Answer option description | |
  | `$..answers[*].options[*].detail_answer.label` | Detail answer label | |
  | `$..answers[*].options[*].detail_answer.description` | Detail answer description | |
  | `$..answers[*].options[*].title` | Relationships answer option question text | Question text to set when this answer option is selected e.g. "Thinking about {person1}, {person2} is their husband or wife"|
  | `$..answers[*].options[*].playback` | Relationships answer option playback text | Used for playback when a relationship is chosen e.g. "{person2} is {person1}'s husband or wife" |
  | `$..answers[*].guidance.show_guidance` | Answer guidance show link | |
  | `$..answers[*].guidance.hide_guidance` | Answer guidance hide link | |
  | `$..answers[*].guidance.contents[*].title` | Answer guidance title | |
  | `$..answers[*].guidance.contents[*].description` | Answer guidance description |
  | `$..answers[*].guidance.contents[*].list` | Answer guidance list | |

- Where it is helpful to reference another property value, an additonal comment should be added. Initially this will be:

  | JSON Path | Comment |
  |-----------|---------|
  | `$..answers[*].description`                           | For answer label: {answer label} |
  | `$..answers[*].options[*].description`               | For answer option: {answer option label} |
  | `$..answers[*].options[*].detail_answer.label`       | For answer option: {answer option label} |
  | `$..answers[*].options[*].detail_answer.description` | For answer option: {answer option label} |
  | `$..answers[*].options[*].title`                     | For answer option: {answer option label} |
  | `$..answers[*].options[*].playback`                  | For answer option: {answer option label} |

### Example

For a detail answer "Enter main language":

```
#. Type: Detail answer label
#. For answer option: Other, including British Sign Language
msgctxt "Question: What is <strong>{person_name_possessive}</strong> main language?"
msgid "Enter main language"
msgstr ""
```
