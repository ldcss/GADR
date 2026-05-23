# ADR 008: Join count

## TL;DR

## Context
For data such as variants, there can be a very large number of joined objects, so we need to provide a count rather than showing the objects. This could then be used as a link to retrieve the list of objects separately.

## Decision
This has been implemented as part of JoinMergeSort, triggered by a special `count` field e.g.
`http://localhost:8080/api/genes/query?query={"name":"BRCA2","genome":"homo_sapiens"}&fields=["name","description",{"variants":["count"]}]`
yields:
```
{
	"name": "BRCA2",
	"description": "breast cancer 2 [Source:HGNC Symbol;Acc:HGNC:1101]",
	"id": "ENSG00000139618",
	"variants": {
		"count": 9337
	}
}
```

## Status
Under development

## Consequences
Will be tricky for homologues but then might not be needed.

`count` might be an actual field used in future so there would be a clash.

## Tags
Search, JoinMergeSearch

