class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # Step 1: Convert n to binary string representation
        bf = format(n, "b")  
        ans = 0  # Step 2: Initialize answer variable
        
        # Step 3: Iterate over bits from right to left
        for i in range(1, len(bf) + 1):
            if bf[-i] == "1":  # Step 4: If current bit is 1, apply the formula
                ans = (2**i - 1) - ans  
        
        # Step 5: Return the minimum operations required
        return ans

"""
Leetcode 1161: Minimum One Bit Operations to Make Integers Zero (https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/description/)

Given an integer n, you must transform it into 0 using the following operations any number of times:
Change the rightmost (0th) bit in the binary representation of n.
Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.
Return the minimum number of operations to transform n into 0.

Example 1:
Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.

Example 2:
Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.
 
Constraints:
0 <= n <= 109

Approach: 
1. Convert n into its binary representation (bf) to analyze the bit positions.
2. Initialize ans to 0, which will store the minimum operations required to transform n into 0.
3. Iterate through the bits of bf from right to left (least significant bit to most significant).
4. If the current bit is "1", update ans using the formula: 𝑎𝑛𝑠 = (2**𝑖 − 1) − 𝑎𝑛𝑠
5. This follows the Gray code transformation rule, ensuring the minimum number of operations is applied.
6. Continue this process until all bits are processed.
7. Return the final value of ans as the minimum number of operations required.

About Gray Code Operation:
The problem constraints define two types of bit operations:
  -> You can flip the rightmost (0th) bit at any time.
  -> You can flip the i-th bit only if the (i-1)-th bit is 1 and all bits before that are 0.

The operations on bits follow a structured pattern similar to Gray Code counting:
  -> Flipping the rightmost bit (0th bit) is always 1 operation.
  -> Flipping the next bit (1st bit) requires 2 additional operations.
  -> Flipping the next bit (2nd bit) requires 4 additional operations, and so on.
  -> More generally, flipping the i-th bit requires (2^i - 1) operations.

Recursive Gray Code Formula
If the i-th bit in n is 1, the minimum number of operations required to reach 0 is: 𝑓(𝑛) = (2**𝑖 − 1) − 𝑓(𝑛 without the 𝑖-th bit)
This follows Gray code reversal rules.
"""
