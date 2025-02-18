class Solution:
    def smallestNumber(self, pattern: str) -> str:
        # Step 1: Initialize counters for 'I' and 'D' in the pattern
        ic, dc = 0, 0  # ic for 'I' and dc for 'D'
        res = ""  # Initialize the result string
        n = len(pattern)  # Length of the pattern
        
        # Step 2: Count how many 'I' and 'D' are in the pattern
        for c in pattern:
            if c == "I":  # If the character is 'I', increase the 'I' counter
                ic += 1
            else:  # If the character is 'D', increase the 'D' counter
                dc += 1

        # Step 3: If all characters are 'I', return the numbers in increasing order
        if ic == n:  # If all characters in the pattern are 'I'
            return ''.join(str(i) for i in range(1, n + 2))  # Return increasing sequence
        
        # Step 4: If all characters are 'D', return the numbers in decreasing order
        elif dc == n:  # If all characters in the pattern are 'D'
            return ''.join(str(i) for i in range(n + 1, 0, -1))  # Return decreasing sequence
        
        else:
            # Step 5: Initialize pointers for filling the result and the stack
            i, j, x = 1, n + 1, ic + 1  # i is the starting number, j is the highest number we need
            
            stack = []  # Initialize the stack to store numbers for 'D' sequences
            
            # Step 6: Traverse through the pattern to build the result
            for idx, c in enumerate(pattern):  # Loop through each character in the pattern
                stack.append(i)  # Add the current number to the stack
                i += 1  # Increment the current number for the next index
                
                # Step 7: If we encounter an 'I', pop the stack and add numbers to the result
                if c == "I":
                    while stack:  # While there are numbers in the stack
                        res += str(stack.pop())  # Pop from the stack and add to the result
            
            # Step 8: After the loop, append the last number to the stack and flush it
            stack.append(i)  # Append the last number to the stack (even if it's the last 'D' section)
            
            # Step 9: Pop all remaining numbers from the stack and add to the result
            while stack:  # If the stack is not empty
                res += str(stack.pop())  # Pop all elements from the stack and append to the result
            
            # Step 10: Return the final result
            return res

"""
Leetcode 2375. Construct Smallest Number From DI String

You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.
A 0-indexed string num of length n + 1 is created using the following conditions:
num consists of the digits '1' to '9', where each digit is used at most once.
If pattern[i] == 'I', then num[i] < num[i + 1].
If pattern[i] == 'D', then num[i] > num[i + 1].
Return the lexicographically smallest possible string num that meets the conditions.

Example 1:
Input: pattern = "IIIDIDDD"
Output: "123549876"
Explanation:
At indices 0, 1, 2, and 4 we must have that num[i] < num[i+1].
At indices 3, 5, 6, and 7 we must have that num[i] > num[i+1].
Some possible values of num are "245639871", "135749862", and "123849765".
It can be proven that "123549876" is the smallest possible num that meets the conditions.
Note that "123414321" is not possible because the digit '1' is used more than once.

Example 2:
Input: pattern = "DDD"
Output: "4321"
Explanation:
Some possible values of num are "9876", "7321", and "8742".
It can be proven that "4321" is the smallest possible num that meets the conditions.
 
Constraints:
1 <= pattern.length <= 8
pattern consists of only the letters 'I' and 'D'.

Approach:
1. Initial Setup: You need to find a way to handle the 'I' and 'D' transitions in the pattern. We can use a stack to store numbers and only release them when we encounter an "I".
2. Count the 'I' and 'D': We need to check if the entire string is 'I' or 'D'. If so, we can directly return the result in increasing or decreasing order.
3. Stack for Processing: For mixed patterns (containing both 'I' and 'D'), we will push numbers to a stack for the 'D' segments and pop them when we encounter 'I' to ensure the lexicographical order.
"""
