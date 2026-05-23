## 4. Align technology, practice and process across the Libero Suite where appropriate

Date: 2019-10-10

### Status

Accepted

### Context

The Libero suite of products currently contains four products: Reviewer, Producer, Publisher and Data Hub. All have different problems to solve where different technologies, frameworks, libraries, concepts and practices help in different ways. For example, Publisher takes a large amount of traffic from a globally diverse population who generally drop in quickly to read content and then disappear. In contrast, Reviewer serves users that are committed to filling forms and uploading content, and has a fraction of the traffic compared to Publisher. Striking the right balance between addressing these different needs while promoting a good experience for developers and service providers is the key to our alignment strategy.

There are a number of personas that we need to balance:

- Web site / app end users (readers, authors, editors and peer reviewers)
- Publishing staff (staff at organisations using the software)
- Community developers who wish to extend and configure the products
- Core developers (all at eLife currently) who may want to work across products and share services but also retain autonomy for a given product by reducing coupling
- Service providers who want to configure and deploy instances of the products

### Decision

The approach is to align in a number of well-defined areas and record this in ADRs. However, strong alignment is not a requirement where it is detrimental to the way the product solves the problems for its given use cases or where it creates undesirable coupling between teams (resulting in synchronisation overheads and reduced autonomy/empowerment). For example, using the same framework for Publisher and Reviewer on the front-end would mean that either single-page performance or interactivity, respectively, would have to suffer, so a better choice would be weaker alignment in that area, as Publisher requires the first and Reviewer depends on the latter.

The process is to explore every reasonable opportunity for a strong alignment, and to pursue it in practice when it becomes apparent that its implementation will not be detrimental to the web apps’ end user experience. Therefore we are not seeking alignment for alignment’s sake, nor are we ignoring it for the sake of the web apps’ end users.

There will always be a balance between user experience, developer experience and publishing staff experience. With software-as-a-service or proprietary software products, the end user experience can always be prioritised over the others, but the community-driven, open source nature of the Libero suite means we have to consider all three. Below is the order in which we should ask ourselves the questions during discovery of an area that could be aligned:

1. Why should we align in this area? Why should we do something different? What is the value?
2. Can we strongly align in this area across products?
3. What are the consequences for the web site / app end users or publishing staff experience?
4. What are the consequences of weaker alignment on the developer experience?
5. Are the product and technology stakeholders happy with the balance and aware of the consequences of the alignment choice for the end user experience, developer experience and publishing staff experience?

A time-boxed discovery session should aim to answer all these questions. In some situations it may be apparent at step 3 or 4 that strong alignment has no consequences.

### Consequences

There is a better defined process for assessing the level of alignment we can achieve across Libero products that considers the consequences for the people working with the software.

Decision making around alignment should be better informed and therefore quicker. Following appropriate discovery, alignment opportunities will be decided upon on a case-by-case basis by consensus between the eLife team - taking input from the community via RFCs where appropriate.

Discovery will consider alignment (or alignment might prompt discovery) so we have more data to justify and record our decisions.

Future inspection of the decisions on alignment will have an evidence-based decision as a starting point for further discussion.
