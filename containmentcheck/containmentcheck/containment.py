"""Perform containment checks on data values in a collection."""

# TODO: Add any needed imports

# TODO: Add type annotations to all functions

# TODO: Add all of the needed documentation to the functions

# TODO: Make sure that you understand how each of these functions work

# TODO: For the containment_check_set function, make sure that you
# read the referenced web site and understand how the function works


def containment_check_list(thelist, number):
    # assume that the value is not inside of the list
    found = False
    return found


def containment_check_tuple(thetuple, number):
    # assume that the value is not inside of the tuple
    found = False
    return found


def containment_check_set(thelist, number):
    # Conventional wisdom often suggests it is faster to:
    # - Convert a list to a set
    # - Search for a number in the set
    # than it is to search through a list
    # Reference to support this assertion:
    # https://docs.quantifiedcode.com/python-anti-patterns/performance/using_key_in_list_to_check_if_key_is_contained_in_a_list.html
    found = False
    theset = set(thelist)
    if number in theset:
        found = True
    return found
