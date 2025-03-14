class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # Step 1: Initialize an array to store seat changes
        res = [0] * (n + 1)
        
        # Step 2: Apply difference array technique
        for l, r, x in bookings:
            res[l-1] += x   # Step 2a: Add seats at the start index
            res[r] -= x       # Step 2b: Remove seats after the end index
        
        # Step 3: Compute prefix sum to get actual seat reservations
        for i in range(1, n):
            res[i] += res[i-1]
        
        # Step 4: Return the result excluding the extra space
        return res[:n]

"""
Leetcode 1109: Corporate Flight Bookings (https://leetcode.com/problems/corporate-flight-bookings/description/)

There are n flights that are labeled from 1 to n.
You are given an array of flight bookings bookings, where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights firsti through lasti (inclusive) with seatsi seats reserved for each flight in the range.
Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

Example 1:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]
Explanation:
Flight labels:        1   2   3   4   5
Booking 1 reserved:  10  10
Booking 2 reserved:      20  20
Booking 3 reserved:      25  25  25  25
Total seats:         10  55  45  25  25
Hence, answer = [10,55,45,25,25]

Example 2:
Input: bookings = [[1,2,10],[2,2,15]], n = 2
Output: [10,25]
Explanation:
Flight labels:        1   2
Booking 1 reserved:  10  10
Booking 2 reserved:      15
Total seats:         10  25
Hence, answer = [10,25]

Constraints:
1 <= n <= 2 * 104
1 <= bookings.length <= 2 * 104
bookings[i].length == 3
1 <= firsti <= lasti <= n
1 <= seatsi <= 104

Approach (Step-by-Step)
1. Initialize an array res of size n+1 with zeros to store seat changes.
2. Iterate through the bookings list and update res:
  --> Increase res[l-1] by x to mark seat reservation at l.
  --> Decrease res[r] by x to remove seats after r.
3. Compute the prefix sum of res to get the total number of reserved seats for each flight.
4. Return the first n elements of res as the final answer.
"""
