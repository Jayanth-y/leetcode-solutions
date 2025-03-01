class Solution:
    def shortestCommonSupersequence(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)

        # Step 1: Create DP table to store LCS length
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Step 2: Fill DP table using bottom-up approach
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:  # Step 3: If characters match, increase LCS length
                    dp[i][j] = dp[i-1][j-1] + 1
                else:  # Step 4: If characters don't match, take max LCS from left or top
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        # Step 5: Trace back to construct the shortest common supersequence
        res = []
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i-1] == s2[j-1]:  # Step 6: If characters match, add to result
                res.append(s1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:  # Step 7: Move in the direction of LCS
                res.append(s1[i-1])
                i -= 1
            else:
                res.append(s2[j-1])
                j -= 1

        # Step 8: Append remaining characters of s1 or s2 if any
        while i > 0:
            res.append(s1[i-1])
            i -= 1
        while j > 0:
            res.append(s2[j-1])
            j -= 1

        # Step 9: Reverse the result and return the SCS
        return ''.join(res[::-1])

"""
Leetcode 1092: Shortest Common Supersequence (https://leetcode.com/problems/shortest-common-supersequence/description/)

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.
A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

Example 1:
Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:
Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"
 
Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of lowercase English letters.

Approach:
1. Create a DP table dp[m+1][n+1] to store the length of the Longest Common Subsequence (LCS) of s1 and s2.
2. Fill the DP table using bottom-up approach, where dp[i][j] represents the LCS length of s1[0:i] and s2[0:j].
3. If s1[i-1] == s2[j-1], update dp[i][j] = dp[i-1][j-1] + 1 since this character is part of the LCS.
4. If s1[i-1] != s2[j-1], update dp[i][j] = max(dp[i-1][j], dp[i][j-1]) to store the maximum LCS length by either excluding s1[i-1] or s2[j-1].
5. Trace back the DP table from dp[m][n] to construct the shortest common supersequence (SCS).
6. If characters from s1 and s2 match, add them to the result and move diagonally up-left in DP table.
7. If characters do not match, add the character from s1 or s2 that contributed to the LCS and move left or up in the table accordingly.
8. If one string is exhausted, append the remaining characters of the other string to the result.
9. Reverse the collected characters to obtain the final SCS and return it.
"""
