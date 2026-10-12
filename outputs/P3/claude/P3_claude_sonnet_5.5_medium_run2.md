def first_item(items):
    # NOTE: The spec conflicts: the postcondition says to return "" for an
    # empty list, while the edge case says to return None. The more specific
    # edge-case rule is followed here. To return "" instead, change the
    # empty-list return value below.
    if not items:
        return None
    return items[0]
