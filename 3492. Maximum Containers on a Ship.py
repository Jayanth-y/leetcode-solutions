class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        return min(n**2 , maxWeight // w)

"""
Leetcode 3492: Maximum Containers on a Ship (https://leetcode.com/problems/maximum-containers-on-a-ship/description/)

You are given a positive integer n representing an n x n cargo deck on a ship. Each cell on the deck can hold one container with a weight of exactly w.
However, the total weight of all containers, if loaded onto the deck, must not exceed the ship's maximum weight capacity, maxWeight.
Return the maximum number of containers that can be loaded onto the ship.
 
Example 1:
Input: n = 2, w = 3, maxWeight = 15
Output: 4
Explanation: The deck has 4 cells, and each container weighs 3. The total weight of loading all containers is 12, which does not exceed maxWeight.

Example 2:
Input: n = 3, w = 5, maxWeight = 20
Output: 4
Explanation: The deck has 9 cells, and each container weighs 5. The maximum number of containers that can be loaded without exceeding maxWeight is 4.

Constraints:
1 <= n <= 1000
1 <= w <= 1000
1 <= maxWeight <= 10^9

Approach (Step-by-Step)
1. Compute the total number of available cells on the cargo deck, which is n * n.
2. Determine how many containers can be loaded based on the ship's weight capacity: maxWeight // w.
3. The final result is the minimum of the two values above since we cannot exceed either the number of deck cells or the weight capacity.
4. Return the minimum value as the maximum number of containers that can be loaded.
"""
