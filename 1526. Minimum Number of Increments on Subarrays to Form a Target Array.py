class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        # Step 1: Initialize operations count with the first element
        c = target[0]

        # Step 2: Iterate through the target array
        for i in range(0, len(target)-1):
            # Step 3: Calculate additional operations required
            c += max(target[i+1] - target[i], 0)  # Step 4: Add positive increments

        # Step 6: Return total operations required
        return c

"""
Leetcode 1526: Minimum Number of Increments on Subarrays to Form a Target Array (https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/description/)

You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.
In one operation you can choose any subarray from initial and increment each value by one.
Return the minimum number of operations to form a target array from initial.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: target = [1,2,3,2,1]
Output: 3
Explanation: We need at least 3 operations to form the target array from the initial array.
[0,0,0,0,0] increment 1 from index 0 to 4 (inclusive).
[1,1,1,1,1] increment 1 from index 1 to 3 (inclusive).
[1,2,2,2,1] increment 1 at index 2.
[1,2,3,2,1] target array is formed.

Example 2:
Input: target = [3,1,1,2]
Output: 4
Explanation: [0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2]

Example 3:
Input: target = [3,1,5,4,2]
Output: 7
Explanation: [0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2].

Constraints:
1 <= target.length <= 10^5
1 <= target[i] <= 10^5

Approach (Step-by-Step)
1. Initialize c as target[0] since we need at least target[0] operations to set the first element.
2. Iterate through target from index 1 to n-1.
3. Compute the difference target[i+1] - target[i] to determine how much more needs to be incremented at i+1.
4. If the difference is positive, add it to c since it represents an additional required operation.
5. Continue processing until the end of the array.
6. Return c as the minimum number of operations.
"""
