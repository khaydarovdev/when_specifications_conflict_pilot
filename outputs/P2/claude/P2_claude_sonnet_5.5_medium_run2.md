def sort_in_place(items):
    """
    NOTE: The two requirements conflict. Sorting a list in place mutates it,
    so the input cannot also remain unchanged (unless it is already sorted).
    This implementation satisfies the invariant (input unchanged) and the
    return-value part of the postcondition (returns the ascending sorted list)
    by sorting a copy. To truly sort in place instead, use `items.sort()`
    and return `items`.
    """
    result = list(items)
    result.sort()
    return result