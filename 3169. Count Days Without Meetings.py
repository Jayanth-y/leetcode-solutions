class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # Step 1: If no meetings, all days are free
        if not meetings:
            return days

        # Step 2: Sort meetings by start time
        meetings.sort()
        merged = []

        # Step 3-6: Merge overlapping or adjacent meetings
        for start, end in meetings:
            if not merged or merged[-1][1] < start - 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)

        # Step 7-8: Calculate total number of busy days
        busy_days = 0
        for s, e in merged:
            busy_days += e - s + 1

        # Step 9-10: Subtract busy from total days
        return days - busy_days

"""
Leetcode 3169: Count Days Without Meetings (https://leetcode.com/problems/count-days-without-meetings/description/)

You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). 
You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).
Return the count of days when the employee is available for work but no meetings are scheduled.
Note: The meetings may overlap.

Example 1:
Input: days = 10, meetings = [[5,7],[1,3],[9,10]]
Output: 2
Explanation: There is no meeting scheduled on the 4th and 8th days.

Example 2:
Input: days = 5, meetings = [[2,4],[1,3]]
Output: 1
Explanation: There is no meeting scheduled on the 5th day.

Example 3:
Input: days = 6, meetings = [[1,6]]
Output: 0
Explanation: Meetings are scheduled for all working days.

Constraints:
1 <= days <= 109
1 <= meetings.length <= 105
meetings[i].length == 2
1 <= meetings[i][0] <= meetings[i][1] <= days

Approach (Step-by-Step)
1. If there are no meetings, return days as all days are free.
2. Sort the meetings list based on start day to prepare for merging overlapping intervals.
3. Initialize an empty list merged to store merged meeting intervals.
4. For each [start, end] in meetings, do the following:
5. If merged is empty or the last merged interval ends before start - 1, append the interval as new.
6. Else, merge the current interval with the last one by updating the end time to max(end, last_end).
7. Initialize a counter busy_days = 0 to accumulate all busy days.
8. For each [s, e] in merged, add e - s + 1 to busy_days.
9. Subtract busy_days from days to get the number of available and free days.
10. Return the result.
"""
