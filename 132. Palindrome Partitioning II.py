class Solution:
    def minCut(self, s: str) -> int:
        # Step 1: Initialize DP array, -1 ensures the first palindrome cut remains 0
        dp = [-1] + [float('inf')]*len(s)
        
        # Step 3: Iterate over end index i
        for i in range(1, len(s)+1):
            # Step 4: Iterate over start index j
            for j in range(1, i+1):
                # Step 5: Check if s[j-1:i] is a palindrome
                if s[j-1:i] == s[j-1:i][::-1]:
                    dp[i] = min(dp[i], dp[j-1]+1)  # Step 5: Update dp[i]
        
        # Step 6: Return minimum cuts for the entire string
        return dp[-1]

"""
Leetcode 132: Palindrome Partitioning II (https://leetcode.com/problems/palindrome-partitioning-ii/description/)

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:
Input: s = "a"
Output: 0

Example 3:
Input: s = "ab"
Output: 1
 
Constraints:
1 <= s.length <= 2000
s consists of lowercase English letters only.

Approach (Step-by-Step)
1. Initialize a DP array dp, where dp[i] represents the minimum cuts needed for a palindrome partition of s[:i].
2. Set dp[-1] = -1 to ensure that the first valid palindrome substring (starting at index 0) does not require a cut.
3. Iterate i from 1 to len(s), representing the end of a substring.
4. Iterate j from 1 to i, representing the start of a substring.
5. If s[j-1:i] is a palindrome, update dp[i] = min(dp[i], dp[j-1] + 1), meaning we consider a partition ending at i by making a cut before j.
6. Return dp[len(s)], which gives the minimum number of cuts needed to partition s into palindromes.
"""
