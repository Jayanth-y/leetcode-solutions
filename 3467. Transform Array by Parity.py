class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        # Step 1: Initialize variables
        n, oc = len(nums), 0  # n = total elements, oc = count of odd numbers
        
        # Step 2: Count the number of odd numbers
        for x in nums:
            if x % 2 == 1:
                oc += 1  # Step 2: Increment count if number is odd
        
        # Step 3: Construct the transformed array
        return ([0]*(n-oc) + [1]*oc)  # Step 4: Create array with zeros followed by ones


"""
Leetcode 3467: Transform Array by Parity (https://leetcode.com/problems/transform-array-by-parity/description/)

You are given an integer array nums. Transform nums by performing the following operations in the exact order specified:
Replace each even number with 0.
Replace each odd numbers with 1.
Sort the modified array in non-decreasing order.
Return the resulting array after performing these operations.

Example 1:
Input: nums = [4,3,2,1]
Output: [0,0,1,1]
Explanation:
Replace the even numbers (4 and 2) with 0 and the odd numbers (3 and 1) with 1. Now, nums = [0, 1, 0, 1].
After sorting nums in non-descending order, nums = [0, 0, 1, 1].

Example 2:
Input: nums = [1,5,1,4,2]
Output: [0,0,1,1,1]
Explanation:
Replace the even numbers (4 and 2) with 0 and the odd numbers (1, 5 and 1) with 1. Now, nums = [1, 1, 1, 0, 0].
After sorting nums in non-descending order, nums = [0, 0, 1, 1, 1].
 
Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 1000

Approach:
1. Initialize n to store the length of nums and oc to count the number of odd elements in nums.
2. Iterate through the array and check if each number is odd. If it is odd, increment oc.
3. The total number of even numbers in nums is n - oc.
4. Construct the transformed array using [0] * (n - oc) + [1] * oc, ensuring that even numbers (0s) appear before odd numbers (1s).
5. Return the final transformed array.
"""
