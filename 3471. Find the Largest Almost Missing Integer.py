class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # Step 1: Initialize counter to track occurrences of numbers in different subarrays
        c = Counter()
        
        # Step 2: Iterate through all subarrays of size k
        for i in range(len(nums) - k + 1):
            c.update(set(nums[i:i+k]))  # Step 3: Add unique elements in subarray to counter
            
        # Step 4: Find numbers that appear in exactly one subarray
        res = [x for x, y in c.items() if y == 1]
        
        # Step 5: Return the largest number among them, or -1 if no such number exists
        return max(res) if res else -1
"""
Leetcode 3471: Find the Largest Almost Missing Integer (https://leetcode.com/problems/find-the-largest-almost-missing-integer/description/)

You are given an integer array nums and an integer k.
An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
Return the largest almost missing integer from nums. If no such integer exists, return -1.
A subarray is a contiguous sequence of elements within an array.
 
Example 1:
Input: nums = [3,9,2,1,7], k = 3
Output: 7
Explanation:
1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:
Input: nums = [3,9,7,2,1,7], k = 4
Output: 3
Explanation:
1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:
Input: nums = [0,0], k = 1
Output: -1
Explanation:
There is no integer that appears in only one subarray of size 1.

Constraints:
1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length

Approach:
1. Initialize a counter c to keep track of how many times each number appears in different subarrays of size k.
2. Iterate through nums using a sliding window of size k.
3. For each subarray of size k, extract its unique elements using set() and update their count in c.
4. Create a list res containing numbers that appear in exactly one subarray.
5. Return the maximum number from res if it exists; otherwise, return -1.
"""
