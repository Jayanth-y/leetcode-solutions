class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        # Step 1: Initialize range variables
        s, e = float('-inf'), float('inf')

        # Step 2: Iterate through original and update valid range
        for i in range(len(original)):
            # Step 3: Update lower bound based on constraints
            s = max(s, bounds[i][0] - original[i])
            
            # Step 4: Update upper bound based on constraints
            e = min(e, bounds[i][1] - original[i])
        
            # Step 5: If lower bound exceeds upper bound, return 0 (no valid arrays)
            if s > e:
                return 0
        
        # Step 6: Return the number of valid sequences
        return e-s+1

"""
Leetcode 3468: Find the Number of Copy Arrays (https://leetcode.com/problems/find-the-number-of-copy-arrays/description/)

You are given an array original of length n and a 2D array bounds of length n x 2, where bounds[i] = [ui, vi].
You need to find the number of possible arrays copy of length n such that:
(copy[i] - copy[i - 1]) == (original[i] - original[i - 1]) for 1 <= i <= n - 1.
ui <= copy[i] <= vi for 0 <= i <= n - 1.
Return the number of such arrays.

Example 1:
Input: original = [1,2,3,4], bounds = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation:
The possible arrays are:
[1, 2, 3, 4]
[2, 3, 4, 5]

Example 2:
Input: original = [1,2,3,4], bounds = [[1,10],[2,9],[3,8],[4,7]]
Output: 4
Explanation:
The possible arrays are:
[1, 2, 3, 4]
[2, 3, 4, 5]
[3, 4, 5, 6]
[4, 5, 6, 7]

Example 3:
Input: original = [1,2,1,2], bounds = [[1,1],[2,3],[3,3],[2,3]]
Output: 0
Explanation:
No array is possible.

Constraints:
2 <= n == original.length <= 105
1 <= original[i] <= 109
bounds.length == n
bounds[i].length == 2
1 <= bounds[i][0] <= bounds[i][1] <= 109

Approach:
1. Initialize s as negative infinity and e as positive infinity to track the valid range of the first element in copy.
2. Iterate through the original array while updating s and e based on the bounds.
3. For each i, update s as the maximum of s and bounds[i][0] - original[i] to ensure copy[i] respects the lower bound.
4. Update as the minimum of e and bounds[i][1] - original[i] to ensure copy[i] respects the upper bound.
5. If at any point s > e, return 0 since no valid sequence can be formed.
6. Return e - s + 1, which represents the number of possible valid sequences that satisfy the given constraints.
"""
