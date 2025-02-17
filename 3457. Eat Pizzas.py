class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # Step 1: Sorting the pizzas by weight in ascending order.
        pizzas = sorted(pizzas)
        
        # Step 2: Calculate how many days we need, based on the number of pizzas.
        n = len(pizzas)
        days = n//4
        
        # Step 3: Initialize result variable to store the total weight.
        res = 0
        
        # Step 4: Set 'i' as the last index in the sorted pizza list (the heaviest pizza).
        i = n-1

        # Step 5: Loop through odd days (1st, 3rd, 5th, etc.) and pick the heaviest pizzas.
        for day in range(1, days+1, 2):
            res += pizzas[i]  # Add the heaviest pizza for the current odd day.
            i -= 1  # Move to the next pizza (next heaviest).
        
        # Step 6: Move to the next pizza, skipping one.
        i -= 1
        
        # Step 7: Loop through even days (2nd, 4th, 6th, etc.) and pick the next heaviest pizzas.
        for day in range(2, days+1, 2):
            res += pizzas[i]  # Add the next heaviest pizza for the current even day.
            i -= 2  # Skip one pizza and move to the next one.

        # Step 8: Return the total weight of the selected pizzas.
        return res

"""
Leetcode 3457. Eat Pizzas

You are given an integer array pizzas of size n, where pizzas[i] represents the weight of the ith pizza. Every day, you eat exactly 4 pizzas. 
Due to your incredible metabolism, when you eat pizzas of weights W, X, Y, and Z, where W <= X <= Y <= Z, you gain the weight of only 1 pizza!
On odd-numbered days (1-indexed), you gain a weight of Z.
On even-numbered days, you gain a weight of Y.
Find the maximum total weight you can gain by eating all pizzas optimally.

Note: It is guaranteed that n is a multiple of 4, and each pizza can be eaten only once.

Example 1:
Input: pizzas = [1,2,3,4,5,6,7,8]
Output: 14
Explanation:
On day 1, you eat pizzas at indices [1, 2, 4, 7] = [2, 3, 5, 8]. You gain a weight of 8.
On day 2, you eat pizzas at indices [0, 3, 5, 6] = [1, 4, 6, 7]. You gain a weight of 6.
The total weight gained after eating all the pizzas is 8 + 6 = 14.

Example 2:
Input: pizzas = [2,1,1,1,1,1,1,1]
Output: 3
Explanation:
On day 1, you eat pizzas at indices [4, 5, 6, 0] = [1, 1, 1, 2]. You gain a weight of 2.
On day 2, you eat pizzas at indices [1, 2, 3, 7] = [1, 1, 1, 1]. You gain a weight of 1.
The total weight gained after eating all the pizzas is 2 + 1 = 3.

Constraints:
4 <= n == pizzas.length <= 2 * 105
1 <= pizzas[i] <= 105
n is a multiple of 4.

Approach:
1. First, the pizzas are sorted in ascending order of their weight, allowing us to easily access the heaviest and second heaviest pizzas when needed.
2. Next, we calculate how many days we need to eat all the pizzas by dividing the total number of pizzas by 4, as we consume exactly 4 pizzas per day.
3. A variable res is initialized to 0 to keep track of the total weight gained from eating the pizzas.
4. We set i to be the last index of the sorted pizzas list, which represents the heaviest pizza, and start picking pizzas from the heaviest available.
5. For each odd day (1st, 3rd, 5th, etc.), we add the weight of the heaviest pizza available (the pizza at the current index i) to res, and then decrease i by 1 to move to the next pizza.
6. After completing the selection for odd days, we skip one pizza by decreasing i by 1 again, ensuring that we skip the pizza already selected for the odd days.
7. For each even day (2nd, 4th, 6th, etc.), we add the weight of the next heaviest pizza available (the pizza at index i) to res, and move to the next pizza, skipping one by decreasing i by 2.
8. Once all the pizzas have been processed, we return the accumulated total weight res, which represents the maximum total weight gained from eating the pizzas optimally.
"""
