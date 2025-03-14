class Solution:
    def numOfWays(self, n: int) -> int:
        # Step 1: Initialize the number of valid colorings for 1-row grid
        a, b = 6, 6
        
        # Step 2: Compute the number of valid colorings for each row
        for i in range(n-1):
            a, b = (3*a + 2*b), (2*a + 2*b)  # Step 3 & 4: Update a and b using recurrence relations
        
        # Step 6: Return the total number of valid ways, mod 10^9 + 7
        return (a+b)%(10**9 + 7)
      
"""
Leetcode 1141: Number of Ways to Paint N × 3 Grid (https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid/description/)

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: 
Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).
Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.
 
Example 1:
Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.

Example 2:
Input: n = 5000
Output: 30228214
 
Constraints:
n == grid.length
1 <= n <= 5000

Approach (Step-by-Step)
1. Define two states: a for color patterns with two colors in the first row, and b for color patterns with three colors in the first row.
2. Initialize a = 6 and b = 6, representing the number of valid ways to color a 1-row grid.
3. Iterate from 1 to n-1 to compute valid colorings for the next rows.
4. Update a as 3 * a + 2 * b to extend two-color patterns while maintaining valid coloring rules.
5. Update b as 2 * a + 2 * b to extend three-color patterns while maintaining valid coloring rules.
6. Repeat this process until the nth row is reached.
7. Return (a + b) % (10**9 + 7) as the total number of ways to color the grid while keeping the result within modulo constraints.
"""
