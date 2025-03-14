class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        # Step 1: Initialize difference array to track updates
        x = [0]*(len(nums)+1)
        
        # Step 2: Initialize counters for queries used and cumulative sum
        c = cs = 0
        
        # Step 3: Iterate through nums to process required decrements
        for i in range(len(nums)):
            cs += x[i]  # Step 3: Update cumulative sum with difference array
            
            # Step 4: Check if more decrements are needed
            while cs < nums[i]:
                # Step 5: If no more queries available and nums[i] is nonzero, return -1
                if c == len(queries): return -1
                
                # Step 6: Fetch the next query
                l, r, val = queries[c]
                c += 1  # Step 7: Mark query as used
                
                # Step 8: Apply the query updates
                if l <= i <= r: 
                    cs += val  # Step 8: Apply immediate effect if in range
                x[l] += val  # Step 9: Apply difference array range update
                x[r+1] -= val  # Step 9: Reverse update after range
        
        # Step 10: Return the minimum number of queries required
        return c

"""
Leetcode 3356: Zero Array Transformation II (https://leetcode.com/problems/zero-array-transformation-ii/)

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].
Each queries[i] represents the following action on nums:
Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.
Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

Example 1:
Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]
Output: 2
Explanation:
For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

Example 2:
Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]
Output: -1
Explanation:
For i = 0 (l = 1, r = 3, val = 2):
Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
The array will become [4, 1, 0, 0].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
The array will become [3, 0, 0, 0], which is not a Zero Array.

Constraints:
1 <= nums.length <= 105
0 <= nums[i] <= 5 * 105
1 <= queries.length <= 105
queries[i].length == 3
0 <= li <= ri < nums.length
1 <= vali <= 5

Approach (Step-by-Step)
1. Initialize a difference array x of size len(nums) + 1 to track updates efficiently.
2. Initialize c to track the number of queries used and cs to track the current cumulative sum.
3. Iterate through nums using index i and update cs with the current value of x[i].
4. If cs is less than nums[i], additional decrements are needed from queries.
5. If c reaches the total number of queries and nums[i] is not zero, return -1.
6. Extract the next query [l, r, val] from queries and increment c as it is used.
7. If i is within the query range [l, r], increment cs by val.
8. Apply the range update by adding val at index l and subtracting val at index r+1.
9. Continue until nums is fully processed and return c as the minimum required queries.
"""
