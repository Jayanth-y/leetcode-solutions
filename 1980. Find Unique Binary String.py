class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Step 1: Convert list to set for faster lookup
        n = len(nums[0])
        nums = set(nums)

        # Step 2: Define a function to generate all binary strings of length n
        def findAllUniquePermutations(chars: List[str], n: int):
            result = itertools.product(chars, repeat=n)  # Generate all combinations

            # Step 3: Iterate through each generated binary string
            for combi in result:
                string = ''.join(combi)  # Convert tuple to string
                
                # Step 4: Return the first missing binary string
                if string not in nums:
                    return string
            
            # Step 5: Edge case (not expected in given constraints)
            return ""
        
        return findAllUniquePermutations(['0','1'], n)
      
"""
Leetcode 1980: Find Unique Binary String (https://leetcode.com/problems/find-unique-binary-string/description/)

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 
If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
 
Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.

Approach:
1. Convert the list nums into a set for faster lookup.
2. Define a helper function to generate all possible binary strings of length n using itertools.product.
3. Iterate over each generated binary string and check if it is not in the nums set.
4. Return the first missing binary string found.
5. If all strings are present (edge case), return an empty string (though this case won’t occur given the problem constraints).
"""
