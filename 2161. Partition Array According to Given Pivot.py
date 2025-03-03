class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Step 1: Initialize lists for elements less than and greater than pivot, and count occurrences of pivot
        n1, n2, c = [], [], 0  
        
        # Step 2: Iterate through nums and classify elements
        for x in nums:
            if x == pivot:
                c += 1  # Step 2a: Count occurrences of pivot
            elif x < pivot:
                n1.append(x)  # Step 2b: Append elements less than pivot
            else:
                n2.append(x)  # Step 2c: Append elements greater than pivot
        
        # Step 3: Construct the final array
        return n1 + [pivot]*c + n2  # Step 4: Return the rearranged array

"""
Leetcode 2161: Partition Array According to Given Pivot (https://leetcode.com/problems/partition-array-according-to-given-pivot/description/)

You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:
Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.

Example 1:
Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.

Example 2:
Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.

Constraints:
1 <= nums.length <= 105
-106 <= nums[i] <= 106
pivot equals to an element of nums.

Approach:
1. Initialize three lists: n1 for elements less than pivot, n2 for elements greater than pivot, and c to count occurrences of pivot.
2. Iterate through the nums array and classify each element:
    a. If the element is equal to pivot, increment c.
    b. If the element is less than pivot, append it to n1.
    c. If the element is greater than pivot, append it to n2.
3. Construct the final array by concatenating n1, c occurrences of pivot, and n2.
4. Return the rearranged array.
"""
