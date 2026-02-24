from collections.abc import Callable
from typing import Any


def execute_on_endpoints(
    tree: dict,
    element: list[str],
    function: Callable[[Any], Any],
    _parents: list[str] = [],
) -> dict:
    """Replaces tree elements using a given function.

    Searches through tree to find keys matching element, such that
    the key's name matches element's first entry, and its parent
    matches the second key (if given), its grandparent matches the third
    key (if given), and so on.

    All found keys are then processed with function, and replaced by
    function's output in tree. (which is modified in-place)

    The modified tree is returned, though it is modified in place as
    well.

    :param tree: The tree to search in, and modify.
    :type tree: dict
    :param element: The list of hierarchy names to match, e.g.
        ['child', 'parent']
    :type element: list[str]
    :param function: The function that is used to process instances
        matching element.
    :type function: Callable[[Any], Any]
    :param _parents: Used internally when traversing the data-structure
        to keep track of parents outside tree.
        (default is [])
    :type _parents: list[str]
    :rtype: dict
    """

    # Calculate element length at start for performance
    elem_len: int = len(element)

    # Search through all top-level keys
    for e in tree.keys():
        # Hierarchy definition is used for comparing against element.
        hierarchy_definition: list[str] = _parents + e
        hierarchy_def_len: int = len(hierarchy_definition)
        # Reduce hierarchy definition to length of element if needed.
        if hierarchy_def_len > elem_len:
            hierarchy_definition = hierarchy_definition[
                elem_len - hierarchy_def_len :
            ]

        # Check if we found an instance of element
        if hierarchy_definition == element:
            # Run function and replace
            tree[e] = function(tree[e])

        # If it isn't a match, can it be traversed?
        elif tree[e] is dict:
            # Traverse
            execute_on_endpoints(
                tree[e], element, function, hierarchy_definition
            )

    return tree
