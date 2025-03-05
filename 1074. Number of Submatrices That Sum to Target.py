class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], t: int) -> int:
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Compute prefix sum matrix
        mm = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                mm[i][j] = mm[i][j-1] + matrix[i-1][j-1]  # Row-wise prefix sum
        
        res = 0  # Step 2: Initialize count of valid submatrices
        
        # Step 3: Iterate over all column pairs
        for i in range(1, n+1):
            for j in range(i, n+1):
                d = {0: 1}  # Step 4: Dictionary to track cumulative sums
                cs = 0  # Step 5: Running cumulative sum for rows
                
                for k in range(1, m+1):
                    # Step 6: Compute sum of submatrix between columns i and j
                    cs += mm[k][j] - mm[k][i-1]
                    
                    # Step 7: Check if (cs - target) exists in dictionary
                    res += d.get(cs-t, 0)
                    
                    # Step 8: Update count of cumulative sum in dictionary
                    d[cs] = d.get(cs, 0)+1
        
        return res  # Step 9: Return total count of valid submatrices
"""
Leetcode 1074: Number of Submatrices That Sum to Target (https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/)

Given a matrix and a target, return the number of non-empty submatrices that sum to target.
A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Example 3:
Input: matrix = [[904]], target = 0
Output: 0
 
Constraints:
1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i][j] <= 1000
-10^8 <= target <= 10^8

Approach:
1. Precompute the Prefix Sum Matrix (mm)
  -> Construct a 2D prefix sum array (mm) where mm[i][j] stores the sum of all elements in the submatrix from (0,0) to (i-1, j-1).
  -> This allows us to efficiently compute the sum of any submatrix in constant time.
2. Iterate Over All Possible Column Pairs (i, j)
  -> Fix two column indices (i, j) to define the left and right boundaries of a submatrix.
  -> We then collapse the matrix into a 1D problem where each row is a sum over the selected column range.
3. Use a Dictionary (d) for Efficient Subarray Sum Counting
  -> Initialize d = {0: 1} to count subarrays that sum to target.
  -> Maintain a running cumulative sum (cs) for each row, representing the sum of elements between columns i and j.
  -> If cs - target exists in the dictionary, we found a valid submatrix.
4. Count Valid Submatrices
  -> Update the count of cumulative sum occurrences in d.
  -> Accumulate the number of valid submatrices found in res.
5. Return the Final Count (res)
"""
