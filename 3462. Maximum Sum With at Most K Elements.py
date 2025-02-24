class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
        n, m = len(grid), len(grid[0])
        
        # Step 1: Insert all elements into a max heap (negated for max-heap simulation)
        for i in range(n):
            for j in range(m):
                heapq.heappush(max_heap, (-grid[i][j], i))  # Store (-value, row_index)
        
        total_sum = 0
        
        # Step 2: Extract the largest k elements while respecting limits
        while k > 0 and max_heap:
            val, row = heapq.heappop(max_heap)  # Extract max element (smallest negative)
            
            if limits[row] > 0:  # Check if row has available limit
                limits[row] -= 1
                total_sum += -val  # Convert back to positive value
                k -= 1
        
        return total_sum
"""
Leetcode 3462: Maximum Sum With at Most K Elements (https://leetcode.com/problems/maximum-sum-with-at-most-k-elements)

You are given a 2D integer matrix grid of size n x m, an integer array limits of length n, and an integer k. 
The task is to find the maximum sum of at most k elements from the matrix grid such that:
The number of elements taken from the ith row of grid does not exceed limits[i].
Return the maximum sum.

Example 1:
Input: grid = [[1,2],[3,4]], limits = [1,2], k = 2
Output: 7
Explanation:
From the second row, we can take at most 2 elements. The elements taken are 4 and 3.
The maximum possible sum of at most 2 selected elements is 4 + 3 = 7.

Example 2:
Input: grid = [[5,3,7],[8,2,6]], limits = [2,2], k = 3
Output: 21
Explanation:
From the first row, we can take at most 2 elements. The element taken is 7.
From the second row, we can take at most 2 elements. The elements taken are 8 and 6.
The maximum possible sum of at most 3 selected elements is 7 + 8 + 6 = 21.
 
Constraints:
n == grid.length == limits.length
m == grid[i].length
1 <= n, m <= 500
0 <= grid[i][j] <= 105
0 <= limits[i] <= m
0 <= k <= min(n * m, sum(limits))

Approach:
1. Use a Max Heap (Priority Queue) to extract the largest elements quickly.
2. Push all elements from the matrix into the heap, storing them as negative values (since Python’s heapq is a min-heap by default).
3. Extract elements from the heap while respecting limits:
   a. Check if the row's limit allows selection before adding to the sum.
   b. Decrement k after each valid selection.
4. Return the total sum.
"""
