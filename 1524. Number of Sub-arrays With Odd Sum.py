class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        odd_count, even_count = 0, 1  # Include the empty prefix sum (0, even)
        curr_sum = 0
        result = 0

        for num in arr:
            curr_sum += num  # Compute the prefix sum
            
            if curr_sum % 2 == 1:  # If prefix sum is odd
                odd_count += 1
                result += even_count  # Odd subarrays can be formed from even prefix sums
            else:  # If prefix sum is even
                even_count += 1
                result += odd_count  # Odd subarrays can be formed from odd prefix sums

            result %= MOD  # Take modulo to avoid overflow
        
        return result
"""
Leetcode 1524: Number of Sub-arrays With Odd Sum (https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/)

Given an array of integers arr, return the number of subarrays with an odd sum.
Since the answer can be very large, return it modulo 109 + 7.

Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.

Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.

Example 3:
Input: arr = [1,2,3,4,5,6,7]
Output: 16

Constraints:
1 <= arr.length <= 105
1 <= arr[i] <= 100

Ideaology:
1. Prefix Sum Determines Subarray Parity
  a. If a prefix sum (sum of elements from the start to index i) is odd, it means we have found an odd sum subarray ending at i.
  b. If a prefix sum is even, we need to subtract an earlier odd prefix sum to get an odd subarray.
2. Tracking Even and Odd Prefix Sums
  a. If the prefix sum is odd, it can form an odd subarray in two ways:
  b. The entire subarray from index 0 to i is odd.
  c. The subarray starts at some earlier index where the prefix sum was even.
  d. If the prefix sum is even, it can form an odd sum subarray only when subtracted from an earlier odd prefix sum.
3. Efficient Counting
  a. Maintain: odd_count → Count of prefix sums that are odd and even_count → Count of prefix sums that are even.
  b. Update the total count based on these values.

Approach:
1. Initialize odd_count to track how many prefix sums are odd, even_count to track how many prefix sums are even, 
   curr_sum as the running prefix sum, and result to store the total number of valid subarrays.
2. Iterate over the array and update curr_sum by adding the current element.
3. If curr_sum is odd, increase odd_count, and add even_count to result since subarrays ending at the current index with an even prefix sum will result in an odd subarray.
4. If curr_sum is even, increase even_count, and add odd_count to result since subarrays ending at the current index with an odd prefix sum will result in an odd subarray.
5. Apply modulo to result to prevent overflow and continue processing until all elements have been traversed.
6. Return result as the count of valid subarrays with an odd sum.
"""
