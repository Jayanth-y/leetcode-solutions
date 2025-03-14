class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        l = res = 0  # Step 1: Initialize variables

        while l+k <= len(s):  # Step 2: Ensure there are at least k characters left
            # Step 3: Check if substring of length k is a palindrome
            if s[l:l+k] == s[l:l+k][::-1]:  
                res += 1
                l += k  # Move forward by k
            
            # Step 4: Check if substring of length k+1 is a palindrome
            elif l+k+1 <= len(s) and s[l:l+k+1] == s[l:l+k+1][::-1]:  
                res += 1
                l += k+1  # Move forward by k+1
            
            # Step 5: If no valid palindrome, move forward by 1
            else:
                l += 1  

        return res  # Step 6: Return maximum count of valid substrings

"""
Leetcode 2472: Maximum Number of Non-overlapping Palindrome Substrings (https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/description/)

You are given a string s and a positive integer k.
Select a set of non-overlapping substrings from the string s that satisfy the following conditions:
The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.

Example 2:
Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.

Constraints:
1 <= k <= s.length <= 2000
s consists of lowercase English letters.

Approach (Step-by-Step):
1. Initialize variables: l = 0 (starting index for checking substrings) and res = 0 (count of valid palindromic substrings).
2. Iterate while l + k <= len(s), ensuring that we have at least k characters left to check for a palindrome.
3. Check if s[l:l+k] (substring of length k) is a palindrome. If true, increment res and move l forward by k.
4. If s[l:l+k+1] (substring of length k+1) is a palindrome, increment res and move l forward by k+1.
5. If neither condition is met, increment l by 1 and continue searching.
6. Return res, the maximum number of valid palindromic substrings found.
"""
