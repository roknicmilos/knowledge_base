"""
O(1) == Constant Time Complexity
"""

# Example 1:
len(range(1, 10))  # O(1)
# Regardless of the size of the range, it will always take the
# same time to calculate the length of the range.

# Example 2:
numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
}
one = numbers["one"]  # O(1)
# Regardless of the size of the dictionary, it will always take
# the same time to get the value of "one" or any other key.
# Under the hood, Python uses hash tables to store the keys as
# unique numbers. This allows Python to access the values quickly.
