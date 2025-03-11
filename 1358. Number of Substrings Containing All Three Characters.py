class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = [0, 0, 0]  # Step 1: Track occurrences of 'a', 'b', 'c'
        
        l = 0  # Left pointer for sliding window
        res = 0  # Store the count of valid substrings
        
        # Step 2: Expand the right pointer
        for r in range(n):
            if s[r] == 'a': count[0] += 1
            elif s[r] == 'b': count[1] += 1
            else: count[2] += 1
            
            # Step 3: Shrink the window while all characters are present
            while count[0] > 0 and count[1] > 0 and count[2] > 0:
                res += (n - r)  # Step 4: Add valid substrings
                
                # Step 5: Move the left pointer and reduce count
                if s[l] == 'a': count[0] -= 1
                elif s[l] == 'b': count[1] -= 1
                else: count[2] -= 1
                l += 1  # Move the left pointer
        
        return res  # Step 6: Return the total count of substrings
"""
Leetcode 1358: Number of Substrings Containing All Three Characters (https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/)

Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:
Input: s = "abc"
Output: 1
 
Constraints:
3 <= s.length <= 5 x 10^4
s only consists of a, b or c characters.

Approach:
1. Initialize count = [0, 0, 0] to track occurrences of 'a', 'b', and 'c'.
2. Initialize l = 0 as the left pointer of the sliding window.
3. Initialize res = 0 to store the count of valid substrings.
4. Iterate through the string using r as the right pointer.
5. Update count by incrementing the corresponding index for s[r].
6. Check if all three characters are present in the current window.
7. If all characters exist, add (n - r) to res.
8. Move l to the right while reducing the count of s[l].
9. Continue until r reaches the end of the string.
10. Return res as the final result.
"""
