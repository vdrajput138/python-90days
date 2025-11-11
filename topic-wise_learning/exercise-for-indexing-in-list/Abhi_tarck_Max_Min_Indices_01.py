"""
1. Find Indices with Maximum and Minimum numbers in list.

Problem: Given a list of integers nums, find the indices of the maximum and minimum elements.
Example:
nums = [10, 3, 7, 2, 9]
Output:
max_index = 0, min_index = 3
"""

nums = [10, 3, 45, 7, 2, 93]

max_index = 0
min_index = 0

for i in range(1, len(nums)):
    if nums[i] > nums[max_index]:
        max_index = i
    if nums[i] < nums[min_index]:
        min_index = i

print("MAX# index: ", max_index, "\nMIN# index: ", min_index)
