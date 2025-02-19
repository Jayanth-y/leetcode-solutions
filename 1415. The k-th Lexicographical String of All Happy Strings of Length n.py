class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        validStrings = []  # List to store valid "happy strings"

        # Function to generate all valid strings of length 'n' from the characters 'a', 'b', 'c'
        def generateAllValidStrings(chars: list, n: int) -> list:
            # Using itertools.product to generate all possible combinations of length 'n'
            # itertools.product(chars, repeat=n) generates all combinations of 'n' characters
            # chosen from the input list 'chars'. For example, if chars = ['a', 'b'] and repeat=2,
            # it generates all combinations of length 2, such as ('a', 'a'), ('a', 'b'), ('b', 'a'), ('b', 'b').
            result = itertools.product(chars, repeat = n)
            
            # Check each generated combination if it is a valid "happy string"
            for combination in result:
                isValid = True
                # Check each character and compare with the previous one to ensure no two consecutive characters are the same
                for i in range(1, len(combination)):
                    if combination[i] == combination[i-1]:  # Invalid if two consecutive characters are the same
                        isValid = False
                        break
                if isValid:
                    # Join the tuple of characters into a string and add to the validStrings list
                    validStrings.append(''.join(combination))

        # Generate all valid strings of length 'n' using characters 'a', 'b', and 'c' and storing them in validStrings List
        generateAllValidStrings(['a', 'b', 'c'], n)
        
        # If 'k' is greater than the number of valid strings, return an empty string
        # Otherwise, return the k-th lexicographically smallest string
        return "" if k > len(validStrings) else sorted(validStrings)[k-1]
      
"""
Leetcode 1415: The k-th Lexicographical String of All Happy Strings of Length n

A happy string is a string that:
a. consists only of letters of the set ['a', 'b', 'c'].
b. s[i] != s[i + 1] for all values of i from 1 to s.length - 1 (string is 1-indexed).
For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings and strings "aa", "baa" and "ababbc" are not happy strings.
Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order.
Return the kth string of this list or return an empty string if there are less than k happy strings of length n.

Example 1:
Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".

Example 2:
Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.

Example 3:
Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy string of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab"
 
Constraints:
1 <= n <= 10
1 <= k <= 100

Approach:
1. Initially, we are generating all valid strings (generateAllValidStrings)
   a. This function generates all combinations of length n using the characters 'a', 'b', and 'c'.
   b. It uses itertools.product(chars, repeat=n) to create all possible combinations of length n from ['a', 'b', 'c'].
   c. It then checks if each combination is a "happy string" (i.e., no two consecutive characters are the same).
   d. Only valid strings are added to the list validStrings.

2. Main Function (getHappyString):
   a. Input: n (length of the string), k (position of the desired lexicographically smallest string).
   b. It calls generateAllValidStrings to generate all valid strings.
   c. Sorts the valid strings lexicographically.
   d. If k is larger than the number of valid strings, it returns an empty string.
   e. Otherwise, it returns the k-th smallest valid string.
"""
