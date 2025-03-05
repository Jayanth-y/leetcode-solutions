class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        # Step 1: Initialize variables
        n = len(heights)
        ans = [0]*n  # Step 1: Store count of visible people
        
        stack = [heights[-1]]  # Step 2: Start with the last person's height in stack
        
        # Step 3: Iterate from right to left
        for i in range(n-2, -1, -1):
            # Step 4: Pop from stack while the current height is taller
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1  # Step 4: Count people that are visible
            
            # Step 5: If the stack is not empty, they can see one more person
            if stack: ans[i] += 1  
            
            # Step 6: Push the current height onto the stack
            stack.append(heights[i])
        
        # Step 7: Return the answer array
        return ans
"""
Leetcode 1944: Number of Visible People in a Queue (https://leetcode.com/problems/number-of-visible-people-in-a-queue/description/)

There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. You are given an array heights of distinct integers where heights[i] represents the height of the ith person.
A person can see another person to their right in the queue if everybody in between is shorter than both of them. More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).
Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

Example 1:
Input: heights = [10,6,8,5,11,9]
Output: [3,1,2,1,1,0]
Explanation:
Person 0 can see person 1, 2, and 4.
Person 1 can see person 2.
Person 2 can see person 3 and 4.
Person 3 can see person 4.
Person 4 can see person 5.
Person 5 can see no one since nobody is to the right of them.

Example 2:
Input: heights = [5,1,2,3,10]
Output: [4,1,1,1,0]
 
Constraints:
n == heights.length
1 <= n <= 105
1 <= heights[i] <= 105
All the values of heights are unique.

Approach:
1. Initialize an array ans of size n with all zeros to store the number of visible people for each person.
2. Use a monotonic decreasing stack to track heights of people who are yet to be counted for visibility.
3. Iterate from right to left (reverse order) to efficiently determine the number of people each person can see.
4. While the current person's height is greater than the height at the top of the stack, pop from the stack and increment the count for the current person since they can see this person.
5. If the stack is not empty after popping, increment the count by one because the next taller person in the stack is still visible.
6. Push the current person's height onto the stack to maintain a decreasing order of heights.
7. Return the ans array as the result.
"""
