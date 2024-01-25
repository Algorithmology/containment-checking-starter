"""Perform containment checks on data values in a collection."""

from typing import List, Tuple

# TODO: Make sure that you understand how each of these functions work

# TODO: For the containment_check_set function, make sure that you
# read the referenced web site and understand how the function works


def containment_check_list(thelist: List[int], number: int) -> bool:
    """Determine if a value is contained in the list."""
    # assume that the value is not inside of the list
    found = False
    # the value is, in fact, inside of the list
    if number in thelist:
        found = True
    # return bool to indicate whether or not value is found
    return found


def containment_check_tuple(thetuple: Tuple[int], number: int) -> bool:
    """Determine if a value is contained in the list."""
    # assume that the value is not inside of the tuple
    found = False
    # the value is, in fact, inside of the tuple
    if number in thetuple:
        found = True
    # return the bool to indicate whether or not value is found
    return found


def containment_check_set(thelist: List[int], number: int) -> bool:
    """Determine if a value is contained in the list."""
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
