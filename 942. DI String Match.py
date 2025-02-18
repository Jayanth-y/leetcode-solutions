class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # Step 1: Initialize an empty result list to store the result
        res = []
        
        # Step 2: Initialize two pointers: i for the smallest number and j for the largest
        i, j = 0, len(s)  # We need to assign values from the range [0, n]
        
        # Step 3: Iterate through the string s
        for c in s:
            if c == "I":  # If the character is 'I', we need an increasing order
                res.append(i)  # Assign the smallest available value to the current position
                i += 1  # Move the 'i' pointer to the next smallest value
            else:  # If the character is 'D', we need a decreasing order
                res.append(j)  # Assign the largest available value to the current position
                j -= 1  # Move the 'j' pointer to the next largest value
        
        # Step 4: Append the last remaining number to the result list (i == j at this point)
        res.append(i)  # At the end, only one value is left which will be the last position
        
        # Step 5: Return the resulting list
        return res
"""
Leetcode 942: DI String Match

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]
 
Constraints:
1 <= s.length <= 105
s[i] is either 'I' or 'D'.

Approach:
We can use two pointers approach:
1. Start with two pointers: 
   a. One pointer i to keep track of the smallest value available for placement.
   b. Another pointer j to keep track of the largest value available for placement.
2. Traverse the string s:
   a. When we encounter an 'I' (increasing), we assign the smallest available number (i) to the current position.
   b. When we encounter a 'D' (decreasing), we assign the largest available number (j) to the current position.
3. Final step:
   a. After filling positions based on the string s, we append the last remaining value (which will be the only value left) to the result.
"""
