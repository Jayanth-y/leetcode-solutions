class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Step 1: Use a set for quick lookup of available supplies
        supplies_set = set(supplies)

        # Step 2: Use a set to identify valid recipe names
        recipe_set = set(recipes)

        # Step 3: Result list to collect all buildable recipes
        can_make = []

        # Step 4: Keep track of recipes to check
        to_check = list(range(len(recipes)))

        # Step 5-9: Repeat until no new recipe can be made
        while to_check:
            did_make_something = False
            next_round = []

            for i in to_check:
                can_cook = True
                for ingredient in ingredients[i]:
                    if ingredient not in supplies_set:
                        can_cook = False
                        # Step 8: Retry later if ingredient might be another recipe
                        if ingredient in recipe_set:
                            next_round.append(i)
                        break

                if can_cook:
                    # Step 7: Make the recipe and mark progress
                    can_make.append(recipes[i])
                    supplies_set.add(recipes[i])
                    did_make_something = True

            # Step 9: Stop if no progress was made in this round
            if not did_make_something and next_round:
                break

            to_check = next_round

        # Step 10: Return the list of makeable recipes
        return can_make

"""
Leetcode 2115: Find All Possible Recipes from Given Supplies (https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/)

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. 
The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. 
A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.
You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
Return a list of all the recipes that you can create. You may return the answer in any order.
Note that two recipes may contain each other in their ingredients.

Example 1:
Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".

Example 2:
Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".

Example 3:
Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

Constraints:
n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.

Approach (Step-by-Step)
1. Convert the supplies list into a set for fast lookup.
2. Convert the recipes list into a set for quick identification of dependencies that are also recipes.
3. Create a result list can_make to store all recipes that can be made.
4. Maintain a list to_check containing indices of all recipes that need evaluation.
5. Iterate while there are recipes to check:
6. For each recipe in to_check, check if all its ingredients are in supplies_set.
7. If yes, the recipe can be made:
   --> Add it to can_make
   --> Add it to supplies_set (since it can now act as an ingredient for other recipes)
   --> Set a flag did_make_something to True
8. If the recipe cannot be made but contains a dependency that is also a recipe, push it to next_round to try again later.
9. If no new recipe was made and next_round is not empty, break the loop to avoid infinite processing.
10. After the loop ends, return the can_make list.
"""
