# 0002. Object identifiers

Date: 2019-06-11

## Status

Agreed

## Context

To uniquely identify an entity in Ensembl (e.g. gene, transcript, region/slice/location) we need three pieces of information:

-   The **dataset** to which the object belongs, e.g. homo_sapiens_GCA_000001405_14 [^1]
-   The **object type**, e.g. gene, transcript, region  
-   The **object ID**, e.g. ENSG00000139618, AT3G52430, 13:32315474-32400266 [^2]  
  
Ensembl entities (called objects) are used extensively in the web client and passing around three separate pieces of information for each one can be cumbersome, error prone, and adds additional work when serialisation is required (e.g. for use in URLs or hash keys). Therefore creating a single string which can be decomposed to the 3 data tuple is useful.

[^1]: For our purposes dataset can be considered synonymous to `genome_id`. Also note issues in the current `genome_id` structure
[^2]: Region strings are not IDs (they do not point to an entity) but we can consider them as such for convenience 

## Decision

To allow more convenient manipulation of Ensembl objects we will use a string to uniquely identify each "object". These “object IDs” will be generated and parsed by the back-end APIs, and should not be generated or parsed by the client (i.e. the client should not assume anything about the ID format). When the client needs information about an object it will request it through the relevant API calls.

### Object ID format

`<dataset>:<object type>:<object id>`

Examples:

```
homo_sapiens_GCA_000001405_14:gene:ENSG00000139618
arabidopsis_thaliana_GCA_000001735_1:gene:AT3G52430
arabidopsis_thaliana_GCA_000001735_1:transcript:AT3G52430
homo_sapiens_GCA_000001405_14:location:13:32315474-32400266
```

Semantically the dataset identifier used (we have chosen `genome_id` here) might differ and so the consuming API should be capable of knowing how to decode said dataset identifier (e.g. it could be a track identiifer).

**Currently `location` is known as `region` in the 2020 codebase**

## Consequences

While it is convenient to have a human readable object ID format, a potential risk is that external users will make assumptions about how these IDs are composed. This may lead to attempted use of invalid IDs, or to external dependencies on a specific format.

At present, we feel the convenience of a human-readable format outweighs the potential risks.

However, as the web client does not parse the object IDs it should be possible to use alternative serialisation formats by changing the way IDs are generated and parsed in the back-end APIs.

An example of an alternative serialisation format is Base64 encoding, e.g.

Format

`Base64_urlencode( <dataset>:<object type>:<object id> )`

Example
```
Base64_urlencode( homo_sapiens_GCA_000001405_14:gene:ENSG00000139618 )
=>
aG9tb19zYXBpZW5zX0dDQV8wMDAwMDE0MDVfMTQ6Z2VuZTpFTlNHMDAwMDAxMzk2MTg=
```

In this case the object IDs cannot be easily decomposed by external users. Base64 url encode should be used to avoid using unsafe URL characters in an ID to be pushed into a URL.
