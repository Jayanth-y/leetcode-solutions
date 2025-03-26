class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Step 1: Flatten the 2D grid to a 1D list
        nums = [num for row in grid for num in row]

        # Step 2: Sort the list
        nums.sort()

        # Step 3: Use the median as the target value
        m = nums[len(nums)//2]
        res = 0

        # Step 4-9: Check divisibility and accumulate operations
        for num in nums:
            diff = abs(m - num)
            if diff % x != 0:
                return -1  # Not possible to reach target
            else:
                res += diff // x

        return res
"""
2033. Minimum Operations to Make a Uni-Value Grid (https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/description/)

You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
A uni-value grid is a grid where all the elements of it are equal.
Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:
Input: grid = [[1,5],[2,3]], x = 1
Output: 5
Explanation: We can make every element equal to 3.

Example 3:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10^5
1 <= m * n <= 10^5
1 <= x, grid[i][j] <= 10^4

Approach (Step-by-Step)
1. Flatten the 2D grid into a 1D list of all elements.
2. Sort the list to prepare for median-based comparison.
3. Choose the median element as the target value, since it minimizes the total absolute difference (for L1 norm).
4. Initialize a result counter res = 0.
5. For each number in the list:
6. Calculate the absolute difference from the median.
7. If the difference is not divisible by x, return -1 as equalization is impossible.
8. Otherwise, add (difference // x) to res to count the number of operations.
9. After processing all elements, return the total operations in res.
"""
