class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Step 1: Compute the total sum of candies
        t = sum(candies)

        # Step 2: If total candies are less than children, return 0
        if t < k: return 0

        # Step 3: Initialize binary search range
        l, r = 1, t//k

        # Step 4: Perform binary search
        while l < r:
            # Step 5: Compute the middle pile size
            m = ((l+r)//2) + 1

            # Step 6: Count how many children can receive at least m candies
            x = 0
            for pile in candies:
                x += pile//m
            
            # Step 7: If x >= k, search in the higher range (increase l)
            if x >= k: l = m
            # Step 8: Otherwise, search in the lower range (decrease r)
            else: r = m - 1
        
        # Step 10: Return the maximum pile size found
        return l
      
"""
Leetcode 2226: Maximum Candies Allocated to K Children (https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description)

You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. 
You can divide each pile into any number of sub piles, but you cannot merge two piles together.
You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. 
Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.
Return the maximum number of candies each child can get.

Example 1:
Input: candies = [5,8,6], k = 3
Output: 5
Explanation: We can divide candies[1] into 2 piles of size 5 and 3, and candies[2] into 2 piles of size 5 and 1. We now have five piles of candies of sizes 5, 5, 3, 5, and 1. We can allocate the 3 piles of size 5 to 3 children. It can be proven that each child cannot receive more than 5 candies.

Example 2:
Input: candies = [2,5], k = 11
Output: 0
Explanation: There are 11 children but only 7 candies in total, so it is impossible to ensure each child receives at least one candy. Thus, each child gets no candy and the answer is 0.

Constraints:
1 <= candies.length <= 105
1 <= candies[i] <= 107
1 <= k <= 1012

Approach:
1. Compute the total sum t of all candies.
2. If t is less than k, return 0 because it is impossible to distribute at least one candy per child.
3. Set the binary search range with l = 1 (minimum pile size) and r = t // k (maximum possible pile size).
4. Perform binary search while l < r.
5. Compute the middle value m = ((l + r) // 2) + 1 as the possible pile size.
6. Count how many children can receive at least m candies.
7. If the count is at least k, update l = m to try a larger pile size.
8. If the count is less than k, update r = m - 1 to reduce the pile size.
9. Continue searching until l == r.
10. Return l as the maximum possible pile size.
"""
