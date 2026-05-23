# Generate PDFs with Prince

## Background

EASi needs to be able to export information in PDF format. We are looking
specifically at exporting System Intake and Business Cases, but in the
future we expect the range of reports to grow as the overall scope of
EASi does.

## Decision Drivers

- The PDFs need to be accessible, which requires using the PDF-UA profile
  and having appropriate tagging.
- Most PDF tooling doesn’t have good support for accessibility features,
  so our choices are somewhat limited.
- The project requires hosting everything privately, which rules out any
  SaaS options for generating PDFs (e.g. [DocRaptor](https://docraptor.com)).
- We’d like to generate the PDF from HTML and CSS code. This allows us to
  develop the PDFs using the same workflows, tools, and CSS code that we
  currently use for the existing UI.

**User Story:** EASI-983

## Chosen Solution

- We will deploy a commercial software product,
  [Prince](https://www.princexml.com), to do the HTML-to-PDF conversion. This
  is a command-line program that we will deploy via AWS Lambda.
- The lambda will only be accessible from our Go backend and not via the
  public internet. It will only have permissions to access services needed
  for metrics and logging.
- Our React frontend will send HTML to Go backend, which will then invoke
  the lambda and return the resulting PDF to the user’s browser.

We think this is the best solution in terms of providing highly-accessible
PDFs, saving developer time, and building on a supported and actively
developed tool. Hosting Prince within a private lambda function minimizes
any potential attack surface.

## Pros and Cons of the Options

### [Prince](https://www.princexml.com)

Mature commercial software product that converts HTML and CSS to PDF.

- `+` Best HTML-to-PDF option in terms of creating accessible PDFs using
  PDF-UA profile
- `+` Offers [control over how PDF files are tagged](https://medium.com/@bruce_39084/making-accessible-tagged-pdfs-with-prince-ad7fd7a48711)
- `+` Allowing us to reuse our existing code and workflow will save lots of
  development time
- `+` Commercially supported product with long history
- `+` [Ready-to-go Lambda distribution](https://medium.com/@bruce_39084/setting-up-prince-on-aws-lambda-and-api-gateway-4d524dcb035b)
- `-` Requires some infra work to setup lambda function
- `-` Closed-source
- `-` Annual license required (~ \$4k/year)
- `+` Already in use by DHS and other government organizations

### [Puppeteer](https://pptr.dev)

Remote controlled headless Chrome allows use of Chrome’s built-in PDF
generator via a Node module.

- `+` Provides some level of PDF tagging
- `-` Chrome’s new `--tagged-pdf` option creates a messy and cluttered
  tag hierarchy that can't be customized
- `-` Requires some infra work to setup lambda function
- `+` Open Source
- `+` Free

### [UniDoc](https://www.unidoc.io) - DOCX

- `-` DOCX isn’t as desirable as PDF
- `-` It isn’t clear if DOCX fulfills our accessibility requirements
- `-` Can't reuse any of our existing application UI for presentation
- `+` Runs in the Go process (doesn’t require additional infra)
- `+` Open Source
- `-` Costs \$3k

### [React-PDF](https://react-pdf.org) (and [PDFKit](http://pdfkit.org))

JavaScript library, all code runs within frontend application

- `-` [Does not support generating accessible PDFs](https://github.com/foliojs/pdfkit/issues/1062)
  (no support for tagging)
- `+` Doesn’t require additional infrastructure
- `+` Open source
- `+` Free

### [Gotenberg](https://thecodingmachine.github.io/gotenberg/)

Docker-based service that created PDFs from various document formats

- `-` Doesn’t support generating tagged PDFs
- `-` Docker image isn’t immediately compatible with running on Lambda
- `+` Open source
- `+` Free

### [Microsoft Print-To-PDF](https://www.onmsft.com/how-to/how-to-print-to-pdf-in-windows-10)

Component of Windows 10 that allows any Windows application to create PDFs

- `-` Creates inaccessible PDFs by embedding images of the webpage
- `-` Not intuitive for users (using “print” to download a file)
- `-` May not be installed by default
- `+` Free
- `+` Works with any Windows application

### [UniDoc](https://www.unidoc.io) - PDF

Go library for generating PDFs

- `-` Doesn’t support creating tagged PDFs
- `-` Can't reuse any of our existing application UI for presentation
- `+` Runs in the Go process (doesn’t require additional infra)
- `+` Open source
- `-` Costs \$3k a year
