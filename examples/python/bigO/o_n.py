"""
O(n) == Linear Time Complexity
"""

from bigO.data import moms

# Example 1:
items = list(range(1, 10))  # O(N)


# If we increase the range to 10x more than the previous range,
# the time it takes to create the list will also increase by 10x.


# Example 2:
def find_mom(child):
    """
    On average, we're going to go through half
    of the list (N/2) to find the mom.

    Each loop has 3 steps:
        1. Get the mom and child names tuple
        2. Assign the mom to mom_name
        3. Assign the child to child_name

    `if` statement inside the loop has 1 step - happens
    once per iteration.

    And finally, the return statement will happen once.

    So, the time complexity of this function is:
    3 * N/2 + N/2 + 1 = 2N + 1 = O(N)
    If we get rid of the lower order components (1) and
    we get rid the coefficient (2), we get O(N).

    Conclusion:
        find_mom() has a linear time complexity.
        find_mom() is O(N).
    """

    for mom_name, child_name in moms:  # 3 * N/2
        if child == child_name:  # 1 * N/2
            return mom_name  # 1
    return None
