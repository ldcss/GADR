# React Hook Forms

Formik isn't getting enough updates.
It is easy to run into bugs during form UI development.
Certain kinds of form fields are difficult to handle.

## Considered Alternatives

* [React Hook Form](https://react-hook-form.com/)
* [Formik](https://formik.org/)

## Decision Outcome

* Chosen Alternative: RHF
* It is comforting that the RHF API has some aspects similar to Formik.
It also has more features for performance and flexibility.
As a bonus this seems to be a popular switch for former Formik users.
* Unfortunately this will cause a significant cleanup effort.
Forms are a major part of this app.

## Pros and Cons of the Alternatives

### *React Hook Form*

* `+` Similar API when marking up form fields
* `+` Provides good code samples
* `+` Features that go along with newer React
* `+` Option for "uncontrolled" form fields to avoid re-renders
* `-` Causes library overhaul

### *Formik*

* `+` Avoid a form library overhaul
* `-` Run into bugs often
* `-` Typescript support sometimes isn't there
* `-` Formik project support uncertain (at this time)
