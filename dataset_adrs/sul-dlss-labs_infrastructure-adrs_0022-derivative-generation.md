---
layout: default
title: ADR-0022
nav_order: 25
permalink: records/0022
---
# Text Derivative File Generation in SDR (OCR/Transcription)

* Status: [proposed]
* Decider(s): <!-- required -->
  * Peter Mangiafico
  * Ed Summers
  * Justin Coyne
  * Justin Littman
  * Alan Lundgard
  * Niqui O'Neill
  * Mike Giarlo
  * Andrew Berger
  * Dinah Handel
* Date(s):
  * Proposed: 2024-03-27
  * Recommended: 2024-04-01

## Context and Problem Statement <!-- required -->

Automated OCR (from images/PDFs) and transcription (from video/audio) are desired for a subset of content deposited in SDR in order to improve accessibility and discoverability.  Current processes for generating these derivative files are manual and require operator intervention.  This proposal is to automate the generation of these derivative files via various mechanisms (either on-demand or by other requests made by operators).

This proposal addresses so called "non-image" derivatives (though they may be referred to simply as "derivatives" throughout this ADR).  For the purpose of this ADR, "non-image" derivatives are defined as derivative files which add value to the delivery of content, but are not strictly required for delivery itself.  For example, JP2s must be created for the image viewer to work, and so these derivatives must be generated during accessioning prior to shelving.  OCR and transcription derivative files are used to make content accessible and searchable, but the viewers themselves will still work without them. Note that while the viewer will work, it may not meet accessibly requirements until the derivatives become available.

This distinction is useful because some derivatives must be generated during accessioning, while others may be generated after accessioning.

For additional context and planning, see Links section below.

## Decision Drivers <!-- optional -->

* Derivatives should be able to be created by an automated process.
* Users should be able to supply pre-created derivatives; the automated generation should be skipped when a pre-created derivative is present.
* Users should be able to re-accession items by providing only changed files.
* Users should be able to review generated derivatives before proceeding.
* Users should be able to replace / edit / update generated derivatives as part of the review process.
* Users should be able to regenerate existing derivatives.
* Generation of non-image derivatives should not delay accessioning.
* Derivative generation failure should be handled.
* Derivatives should be versioned and there should be a single system from which all files can be retrieved.

## Considered Options <!-- required -->

Three original options were considered, as summarized in [this document](https://docs.google.com/document/d/10MzjOjwmuijHD5rgO5QxxuLKFwv94Lq29vDy0Y_xDUg)

* Option 1 had derivatives generated prior to accessioning (similar to the current manual process)
* Option 2 had derivatives generated during accessioning (similar to JP2 derivative creation)
* Option 3 had derivatives generated after accessioning
* Option 4 also had derivatives generated after accessioning, but not via a workflow and [instead using tools in the Access stack](https://docs.google.com/document/d/1EDcj-lb2jpjzMxm2MDsvVvpYOopvsgtRUrY97arzcu4/edit#heading=h.j58qbs1p9lqa)

After considering the pros and cons of each approach, option 3 was selected, and is described here.  The pros and cons of the various options are summarized in the above documents, and the reason option 3 was selected was the requirement that generation of these derivatives should not delay accessioning, which would not be possible with options 1 and 2.

The proposed solution uses a combination of a messaging and workflow driven solutions as described in more detail in [this document](https://docs.google.com/document/d/1JLJwio7xVDDh75KY3dZJIFPDep-92hoQJ5p9EgFKabY) and summarized below.

## Decision Outcome <!-- required -->

After [several discussions](https://docs.google.com/document/d/1H1zy-yCDErMTf2IWK1PdN9r_6IjqRqiREc0yYnaiYvo) as part of an Architecture Forum, we propose to use a combination of messaging and new workflow(s) to produce non-image derivatives, a form of Option 3 as described in documents listed above.

The basic flow and architecture is:

* The user initiates accessioning via current systems, e.g. pre-assembly, Goobi, H2.  New user interface elements will need to be added to indicate if OCR or transcription is needed for the material or batch of materials.  This will set new fields in cocina and/or add new workflow variables.
* Accessioning will proceed as normal.
* At the last step of `accessionWF`, currently `end-accession`, we will [use logic](https://docs.google.com/document/d/1JLJwio7xVDDh75KY3dZJIFPDep-92hoQJ5p9EgFKabY/edit#heading=h.n930qglopzgc) to create the new OCR/captioning workflow for that object if needed.  This new workflow is created immediately if needed, but `accessionWF` will be allowed to complete (i.e. the creation of the new workflow is not blocking).
* The new workflow will have consist of several steps, which will include any required versioning, OCR and transcription, and possible pause of review.  If review is required, it will be indicated by the operator ahead of time via a UI element (most likely in pre-assembly or Goobi), and this will be passed through to the workflow.
* Note: Since the new workflow will need to version the object, and since a new version cannot be opened until the previous one is closed, there may be a race condition if the new version is opened before the previous one is closed.  If this happens occasionally, a restart of the workflow will fix the problems.  if this happens often, we may need to implement automatic retries or look to the alternate messaging based solution described below.
* The OCR will be performed by ABBYY, and the transcription will be performed by Whisper. These services are likely to be run separately from the server(s) monitoring for `end-accession.completed` and running the new robots, and will triggered by API calls from the robots.
* As part of the workflow, the object will be opened, and then closed when OCR and transcription is complete to ensure files are preserved.
* Closing the object will trigger accessionWF, which will ensure the files are properly shelved and preserved.
* Changes being made to versioning in a separate workcycle will ensure that no other user or process can close the object while this new workflow is in process, preventing two processes from altering the object at the same time.

### Alternative Mechanism to start OCR/Transcription

When accessioning is complete, an `end-accession.completed` message is currently sent.  An alternative to having the new OCR/transcription workflow triggered by the last step of `accessionWF` is to listen for this message and trigger the new workflow(s) when the message is received.  This new service would thus look for these messages and [use logic](https://docs.google.com/document/d/1JLJwio7xVDDh75KY3dZJIFPDep-92hoQJ5p9EgFKabY/edit#heading=h.n930qglopzgc) to create the new OCR/captioning workflow for that object if needed.  Logic will consider the content type, the new fields set and the existence of derivatives to determine if the new OCR/captioning workflow is needed.

### TBD

Some issues are known to be outstanding and will be decided later:

* Which exact variables need to be passed from the accessioneer through the system.
* Where these variables will be stored (e.g. in cocina or in the workflow model or a combination of the two).
* How reviews will be performed and which system will be used to do this.
* How edits will be performed and which system will be used to do this.
* If we will have a single new workflow to handle both OCR and transcription, or if two separate workflows will be used.
* How will the code be distributed between existing codebases and VMs and new codebases and VMs.
* [more]

## Links <!-- optional -->

* [Integrating Text Extraction into SDR Accessioning - Architecture Forum Overview](https://docs.google.com/document/d/1vzDFaD9BKmyDaJdXcVIp82Vd2BJ9hnuUH1KhXilEOWk)
* [Derivative Generation Proposal](https://docs.google.com/document/d/1JLJwio7xVDDh75KY3dZJIFPDep-92hoQJ5p9EgFKabY)
* [Meeting Running Notes](https://docs.google.com/document/d/1H1zy-yCDErMTf2IWK1PdN9r_6IjqRqiREc0yYnaiYvo)
* [High level overview of options by Andrew](https://docs.google.com/document/d/10MzjOjwmuijHD5rgO5QxxuLKFwv94Lq29vDy0Y_xDUg)
* [Derivative Generation Proposal (post processing)](https://docs.google.com/document/d/1EDcj-lb2jpjzMxm2MDsvVvpYOopvsgtRUrY97arzcu4/edit#heading=h.j58qbs1p9lqa)
