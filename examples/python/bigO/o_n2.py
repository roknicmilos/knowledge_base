"""
O(N2) == Quadratic Time Complexity
"""

from bigO.data import moms
from bigO.o_n import find_mom


# Example:
def grandmothers_count():
    """
    N2 + kN + 1 = O(N2)
    """
    grandmother_count = 0
    for child, mom in moms:  # N
        grandma = find_mom(mom)  # N * N
        if grandma:  # N
            grandmother_count += 1  # kN
    return grandmother_count  # 1
