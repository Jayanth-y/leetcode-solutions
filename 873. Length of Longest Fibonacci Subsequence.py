class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        s = set(arr)  # Step 1: Convert array to a set for quick lookups
        maxlen = 0  # Step 2: Track the longest Fibonacci-like sequence

        # Step 3: Iterate through all pairs as potential first two numbers of a sequence
        for i in range(n):
            for j in range(i+1, n):
                count = 1  # Step 4: Initialize sequence length
                a, b = arr[i], arr[j]  # Step 4: Start sequence with arr[i] and arr[j]

                # Step 5: Continue while the next Fibonacci number exists in the set
                while b in s:
                    count += 1
                    a, b = b, a+b  # Step 5: Update `a` and `b` to next values in the sequence
                
                # Step 6: Update maxlen if a valid Fibonacci-like sequence is found
                if count >= 3: maxlen = max(maxlen, count)

        # Step 7: Return the longest valid sequence length found
        return maxlen
"""
Leetcode 873: Length of Longest Fibonacci Subsequence (https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/)

A sequence x1, x2, ..., xn is Fibonacci-like if:
n >= 3
xi + xi+1 == xi+2 for all i + 2 <= n
Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

Example 1:
Input: arr = [1,2,3,4,5,6,7,8]
Output: 5
Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].

Example 2:
Input: arr = [1,3,7,11,12,14,18]
Output: 3
Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
 
Constraints:
3 <= arr.length <= 1000
1 <= arr[i] < arr[i + 1] <= 109

Approach:
1. Convert the array into a set for quick lookups to check Fibonacci-like extensions efficiently.
2. Initialize maxlen to track the longest Fibonacci-like subsequence found.
3. Iterate over all pairs (i, j) to consider them as the first two numbers of a possible Fibonacci-like sequence.
4. Set initial values a = arr[i] and b = arr[j], and initialize count to track the subsequence length.
5. Continue checking if the next Fibonacci number (a + b) exists in the set and update a and b accordingly.
6. If a valid Fibonacci-like sequence of length at least 3 is found, update maxlen with the maximum length encountered.
7. Return maxlen as the length of the longest Fibonacci-like subsequence found.
"""
