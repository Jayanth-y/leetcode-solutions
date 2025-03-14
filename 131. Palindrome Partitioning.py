class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # Step 1: Stores the final palindrome partitions
        partition = []  # Step 1: Tracks current partitioning

        # Step 2: Helper function to check if substring is a palindrome
        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l+1, r-1
            return True

        # Step 3: Backtracking function to generate partitions
        def dfs(i):
            # Step 4: If we've reached the end, store partition copy in res
            if i >= len(s):
                res.append(partition.copy())
                return
            
            # Step 5: Iterate to create substrings from i to j
            for j in range(i, len(s)):
                # Step 6: If substring s[i:j+1] is palindrome, proceed
                if isPalindrome(s, i, j):
                    partition.append(s[i:j+1])  # Step 6: Add to partition
                    dfs(j+1)  # Step 7: Recur to find more partitions
                    partition.pop()  # Step 7: Backtrack to explore other options

        # Step 8: Start the recursion from index 0
        dfs(0)

        # Step 9: Return final partition list
        return res

"""
Leetcode 131: Palindrome Partitioning (https://leetcode.com/problems/palindrome-partitioning/description)

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s. 

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
 
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.

Approach (Step-by-Step)
1. Initialize res to store the final list of palindrome partitions.
2. Define a helper function isPalindrome(s, l, r) to check if s[l:r+1] is a palindrome.
3. Use a backtracking function dfs(i) to explore all possible partitions starting from index i.
4. If i reaches the end of s, store a copy of partition in res.
5. Iterate j from i to len(s) - 1 to generate substrings s[i:j+1].
6. If s[i:j+1] is a palindrome, add it to partition, call dfs(j+1), and then backtrack.
7. Continue exploring all possible partitions recursively.
8. Return res as the final result.
"""
