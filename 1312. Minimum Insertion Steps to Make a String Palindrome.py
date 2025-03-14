class Solution:
    def minInsertions(self, s: str) -> int:
        # Step 1: Reverse the string to find LCS
        t = s[::-1]
        n = len(s)
        
        # Step 2: Initialize DP table to store LCS values
        dp = [[0]*(n+1) for _ in range(n+1)]

        # Step 3: Fill the DP table using LCS approach
        for i in range(n):
            for j in range(n):
                # Step 4: If characters match, extend LCS
                if s[i] == t[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                # Step 5: Otherwise, take the max LCS length found so far
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        
        # Step 6: Compute minimum insertions required
        return n - dp[n][n]
"""
Leetcode 1312: Minimum Insertion Steps to Make a String Palindrome (https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/)

Given a string s. In one step you can insert any character at any index of the string.
Return the minimum number of steps to make s palindrome.
A Palindrome String is one that reads the same backward as well as forward.

Example 1:
Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:
Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:
Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

Constraints:
1 <= s.length <= 500
s consists of lowercase English letters.

Approach (Step-by-Step)
1. Reverse the string s to get t, since making s a palindrome is equivalent to finding the longest common subsequence (LCS) between s and t.
2. Initialize a 2D DP table dp of size (n+1) x (n+1) where dp[i][j] stores the LCS length between s[:i] and t[:j].
3. Iterate through both s and t using indices i and j to fill the DP table.
4. If s[i] == t[j], update dp[i+1][j+1] = 1 + dp[i][j] to extend the LCS.
5. Otherwise, update dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1]) to retain the longest subsequence found so far.
6. Compute the minimum insertions required as n - dp[n][n], since the longest palindromic subsequence (LPS) is of length dp[n][n].
7. Return the computed value as the answer.
"""
