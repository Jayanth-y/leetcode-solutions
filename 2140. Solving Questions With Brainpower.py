class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        questionsLength = len(questions)
        memo = {}  # Dictionary to store best path at every index

        def processFurther(currIndex, currPoints):
            # Step 1: If we've reached past the end, return accumulated points
            if currIndex >= questionsLength: 
                return currPoints

            # Step 4: Return cached result if already computed
            if currIndex in memo:
                return memo[currIndex] + currPoints

            # Step 2: Choose to solve the current question
            nextIndexIfChoosing = currIndex + questions[currIndex][1] + 1
            pointsIfChoosing = currPoints + questions[currIndex][0]
            resultIfChoosing = processFurther(nextIndexIfChoosing , pointsIfChoosing)

            # Step 3: Choose to skip the current question
            nextIndexIfSkipping = currIndex + 1
            pointsIfSkipping = currPoints
            resultIfSkipping = processFurther(nextIndexIfSkipping , pointsIfSkipping)

            # Step 5: Take the better of the two choices
            bestResultBetweenChoosingOrSkipping = max(resultIfChoosing, resultIfSkipping)

            # Store result in memo (without currPoints to keep it index-relative)
            memo[currIndex] = bestResultBetweenChoosingOrSkipping - currPoints
            
            return bestResultBetweenChoosingOrSkipping

        return processFurther(0, 0)
"""
2140. Solving Questions With Brainpower (https://leetcode.com/problems/solving-questions-with-brainpower/)

You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. 
Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
Return the maximum points you can earn for the exam.

Example 1:
Input: questions = [[3,2],[4,3],[4,4],[2,5]]
Output: 5
Explanation: The maximum points can be earned by solving questions 0 and 3.
- Solve question 0: Earn 3 points, will be unable to solve the next 2 questions
- Unable to solve questions 1 and 2
- Solve question 3: Earn 2 points
Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.

Example 2:
Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
Output: 7
Explanation: The maximum points can be earned by solving questions 1 and 4.
- Skip question 0
- Solve question 1: Earn 2 points, will be unable to solve the next 2 questions
- Unable to solve questions 2 and 3
- Solve question 4: Earn 5 points
Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.
 
Constraints:
1 <= questions.length <= 10^5
questions[i].length == 2
1 <= pointsi, brainpoweri <= 10^5

Approach (Step-by-Step):
1. Initialize a recursive function that tries both solving and skipping each question.
2. If we solve the current question, we earn its points but skip the next brainpower[i] questions.
3. If we skip the current question, we move to the next one with no points gained.
4. Use memoization to avoid reprocessing the same state repeatedly.
5. Track the best result at each index and return the maximum of both choices.
"""
