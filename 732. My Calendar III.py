class MyCalendarThree:
    def __init__(self):
        # Step 1: Dictionary to store event start and end changes
        self.b = defaultdict(int)
        self.overlap = 0  # Step 2: Track max concurrent events

    def book(self, s: int, e: int) -> int:
        # Step 3: Mark event start and end in the dictionary
        self.b[s] += 1
        self.b[e] -= 1

        # Step 4: Compute the maximum overlapping events
        c = 0  # Step 4a: Running count of active events
        for time in sorted(self.b.keys()):
            c += self.b[time]  # Step 4b: Update active events
            self.overlap = max(self.overlap, c)  # Step 5: Track max k-booking

        return self.overlap  # Step 6: Return max concurrent booking

"""
Leetcode 732: My Calendar III (https://leetcode.com/problems/my-calendar-iii/description/)

A k-booking happens when k events have some non-empty intersection (i.e., there is some time that is common to all k events.)
You are given some events [startTime, endTime), after each given event, return an integer k representing the maximum k-booking between all the previous events.
Implement the MyCalendarThree class:

MyCalendarThree() Initializes the object.
int book(int startTime, int endTime) Returns an integer k representing the largest integer such that there exists a k-booking in the calendar.

Example 1:
Input:
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output: [null, 1, 1, 2, 3, 3, 3]

Explanation
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // return 1
myCalendarThree.book(50, 60); // return 1
myCalendarThree.book(10, 40); // return 2
myCalendarThree.book(5, 15); // return 3
myCalendarThree.book(5, 10); // return 3
myCalendarThree.book(25, 55); // return 3

Constraints:
0 <= startTime < endTime <= 109
At most 400 calls will be made to book.

Approach (Step-by-Step)
1. Initialize a defaultdict(int) b to store time points and their event counts.
2. Initialize overlap to track the maximum k-booking observed so far.
3. In the book() function, increment b[start] to mark the event start and decrement b[end] to mark the event end.
4. Iterate through the sorted keys of b to maintain a running sum c of active events.
5. Update overlap to track the highest concurrent booking (k).
6. Return overlap as the result.
"""
