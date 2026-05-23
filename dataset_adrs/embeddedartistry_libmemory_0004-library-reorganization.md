# 4. Library Reorganization

Date: 2024-10-14

## Status

Accepted

## Context

In order to support the implementation of `aligned_alloc`, C11's `free` (able to free both aligned_alloc and normal malloc memory), and the [improved freelist implementation](https://github.com/embeddedartistry/libmemory/pull/91) from michaeljclark, the fundamental design of the library needs to changed.

In particular, `aligned_malloc` was presumed to be a standalone addition under C99, added onto an existing `malloc` implementation. The implementation necessitated that the memory be freed with `aligned_free`.

However, this requirement cannot hold anymore, and we need a more "intrusive" solution that covers both specific-aligned and standard allocations.

## Decision

- The existing aligned allocator strategy, which is tacked onto an existing `malloc`/`free`, will be kept as an independent solution
- The new aligned allocation strategy will be more tightly coupled to the implementation of `malloc`, to support the necessary C11 requirements.
- Allocators are now expected to have an implementation of `malloc` and `aligned_alloc` that is suitable for

## Consequences

The approach above adds complexity to the build design and to implementation requirements.

- We still want to provide the standalone aligned allocator for users to select, as there are still several C99 systems using this library. However, the ideal build approach would be changing dependency names, which necessitates a build change. Ideally, this will be done in a breaking way, so that updates become clearer. Or, maybe we could trigger an error and add an update note on what needs to change, making the migration clearer.
- Existing RTOS allocators need to be adjusted to handle aligned allocation as well in an integrated way.
- Documentation requirements need to be clear that the implementation must support `aligned_alloc` and `malloc`, as they will `free` memory the same way.
