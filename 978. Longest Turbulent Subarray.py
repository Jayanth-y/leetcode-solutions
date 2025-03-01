class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Step 1: Initialize variables
        m, c, p = 1, 1, None  # m = max length, c = current turbulent length, p = previous comparison
        
        # Step 2: Iterate through the array from index 1
        for i in range(1, len(arr)):
            # Step 3: Check if the sequence alternates turbulence
            if (arr[i] < arr[i-1] and p) or (arr[i] > arr[i-1] and p is False):
                c += 1  # Step 3: Increase current turbulent count if alternating pattern continues
            else:
                if arr[i] != arr[i-1]:  
                    c = 2  # Step 4: Reset to 2 if the current pair is different
                else:
                    c = 1  # Step 5: Reset to 1 if consecutive elements are equal
            
            # Step 6: Update `p` to track the last comparison direction
            p = None if arr[i] == arr[i-1] else arr[i] > arr[i-1]
            
            # Step 7: Update max turbulent subarray length
            m = max(m, c)
        
        # Step 8: Return the maximum turbulence size found
        return m
"""
Leetcode 978: Longest Turbulent Subarray (https://leetcode.com/problems/longest-turbulent-subarray/description/)

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.

Example 1:
Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

Example 2:
Input: arr = [4,8,12,16]
Output: 2

Example 3:
Input: arr = [100]
Output: 1

Constraints:
1 <= arr.length <= 4 * 104
0 <= arr[i] <= 109

Approach:
1. Initialize m to track the maximum turbulent subarray length, c for the current turbulent length, and p to store the previous comparison result.
2. Iterate through the array starting from index 1 to check adjacent element relationships.
3. If the current comparison alternates with the previous one, increase c by 1 to extend the turbulent sequence.
4. If the comparison does not alternate but the elements are different, reset c to 2 to start a new turbulent sequence.
5. If two consecutive elements are equal, reset c to 1 since turbulence is broken.
6. Update p with the new comparison state (None for equal elements, True for increasing, False for decreasing).
7. Update m to keep track of the maximum turbulent subarray length encountered.
8. Return m as the final result.
"""
