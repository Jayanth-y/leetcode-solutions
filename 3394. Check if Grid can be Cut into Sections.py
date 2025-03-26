class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:

        # Step 1: Helper to simulate sweeping line for cut detection
        def canMakeCuts(events):
            cs = 0  # Current sum of active intervals
            lines = 0  # Count of zero-points (cut lines)
            for pos, val in events:
                cs += val
                if cs == 0:  # No active rectangles -> valid cut location
                    lines += 1
                    if lines >= 2:  # Need at least 2 cuts to create 3 parts
                        return True
            return False

        xCheck = []
        yCheck = []

        # Step 2: Create events for horizontal and vertical edges
        for x1, y1, x2, y2 in rectangles:
            xCheck.append((x1, 1))   # Entering rectangle at x1
            xCheck.append((x2, -1))  # Exiting rectangle at x2
            yCheck.append((y1, 1))   # Entering rectangle at y1
            yCheck.append((y2, -1))  # Exiting rectangle at y2

        # Step 3: Sort the events by coordinate
        xCheck.sort()
        yCheck.sort()

        # Step 4: Check if we can cut either horizontally or vertically
        return canMakeCuts(xCheck) or canMakeCuts(yCheck)

"""
Leetcode 3394: Check if Grid can be Cut into Sections (https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/)

You are given an integer n representing the dimensions of an n x n grid, with the origin at the bottom-left corner of the grid. 
You are also given a 2D array of coordinates rectangles, where rectangles[i] is in the form [startx, starty, endx, endy], representing a rectangle on the grid. 
Each rectangle is defined as follows:
(startx, starty): The bottom-left corner of the rectangle.
(endx, endy): The top-right corner of the rectangle.
Note that the rectangles do not overlap. Your task is to determine if it is possible to make either two horizontal or two vertical cuts on the grid such that:

Each of the three resulting sections formed by the cuts contains at least one rectangle.
Every rectangle belongs to exactly one section.
Return true if such cuts can be made; otherwise, return false.

Example 1:
Input: n = 5, rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
Output: true
Explanation:
The grid is shown in the diagram. We can make horizontal cuts at y = 2 and y = 4. Hence, output is true.

Example 2:
Input: n = 4, rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
Output: true
Explanation:
We can make vertical cuts at x = 2 and x = 3. Hence, output is true.

Example 3:
Input: n = 4, rectangles = [[0,2,2,4],[1,0,3,2],[2,2,3,4],[3,0,4,2],[3,2,4,4]]
Output: false
Explanation:
We cannot make two horizontal or two vertical cuts that satisfy the conditions. Hence, output is false.

Constraints:
3 <= n <= 109
3 <= rectangles.length <= 105
0 <= rectangles[i][0] < rectangles[i][2] <= n
0 <= rectangles[i][1] < rectangles[i][3] <= n
No two rectangles overlap.

Approach (Step-by-Step)
1. Define a helper function canMakeCuts(events) to simulate a line sweep over sorted interval events.
2. Initialize two lists xCheck and yCheck to store entry and exit events along x-axis and y-axis.
3. For each rectangle, insert (x1, +1) and (x2, -1) into xCheck to represent start and end of rectangle on x-axis.
4. Similarly insert (y1, +1) and (y2, -1) into yCheck for y-axis events.
5. Sort both xCheck and yCheck by coordinate.
6. In canMakeCuts, sweep through the sorted events while maintaining a counter cs for how many rectangles are active.
7. Each time the counter cs becomes 0, it means a potential cut can be made between disjoint groups of rectangles.
8. If at least two such zero points (lines) are found, return True indicating 2 cuts are possible.
9. Return True if canMakeCuts(xCheck) or canMakeCuts(yCheck) is True.
"""
