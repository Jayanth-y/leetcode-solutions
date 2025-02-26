# Solution 1:
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Handle the edge case when there's only one element
        if n == 1: return abs(nums[0])

        # Step 2: Initialize cumulative sums and tracking variables
        csum1, maxsum = 0, 0  # Track max subarray sum
        csum2, minsum = 0, 0  # Track min subarray sum

        # Step 3: Iterate through the array while maintaining max and min cumulative sums
        for i in range(n):
            # Step 4: Update max cumulative sum (Kadane’s for max subarray)
            csum1 = max(0, csum1 + nums[i])
            maxsum = max(maxsum, csum1)

            # Step 5: Update min cumulative sum (Kadane’s for min subarray)
            csum2 = min(0, csum2 + nums[i])
            minsum = min(minsum, csum2)

        # Step 6: Return the max absolute sum by comparing maxsum and abs(minsum)
        return max(maxsum, abs(minsum))



# Solution 2:
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # Step 1: Compute the prefix sum array using accumulate() with initial value 0
        s = list(accumulate(nums, initial=0))  
        
        # Step 2: The prefix sum at any index represents the sum of the subarray from the start to that index
        # Step 3: The difference between any two prefix sums gives the sum of a subarray
        # Step 4: To find the maximum absolute difference, compute max and min values in prefix sum array
        max_val = max(s)  
        min_val = min(s)  
        
        # Step 5: The maximum absolute sum of any subarray is given by max(prefix_sum) - min(prefix_sum)
        return max_val - min_val  
"""
Leetcode 1749: Maximum Absolute Sum of Any Subarray (https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/description/)

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).
Return the maximum absolute sum of any (possibly empty) subarray of nums.
Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.

Example 1:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.

Example 2:
Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104

Approach:
1. Compute the prefix sum array using accumulate() with an initial value of 0 to track cumulative sums efficiently.
2. The prefix sum at any index represents the sum of the subarray from the start to that index.
3. The difference between any two prefix sums gives the sum of a subarray, and the absolute maximum subarray sum is obtained by maximizing this difference.
4. To find the maximum absolute difference, compute the maximum and minimum values in the prefix sum array.
5. The maximum absolute sum of any subarray is given by max(prefix_sum) - min(prefix_sum).
6. Return this computed value as the result.
"""
