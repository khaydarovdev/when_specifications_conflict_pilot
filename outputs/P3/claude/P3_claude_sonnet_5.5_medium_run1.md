def first_item(items):
    # Note: the spec is contradictory for an empty list (postcondition says "",
    # edge case says None). The more specific edge-case rule is followed here.
    # To return "" instead, change `return None` to `return ""`.
    if not items:
        return None
    return items[0]
