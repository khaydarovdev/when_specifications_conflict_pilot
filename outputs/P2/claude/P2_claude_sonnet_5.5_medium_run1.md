def sort_in_place(items):
    # NOTE: The spec is contradictory: sorting "in place" mutates the input,
    # but the invariant requires the input to remain unchanged.
    # This implementation honors the invariant and the return-value
    # postcondition by sorting a copy. For true in-place sorting,
    # replace the body with: items.sort(); return items
    result = list(items)
    result.sort()
    return result