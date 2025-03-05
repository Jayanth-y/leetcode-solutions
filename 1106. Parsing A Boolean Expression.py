class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        t, f = True, False  # Step 1: Define boolean literals for true and false
        
        # Step 2: Replace logical operators with equivalent Python expressions
        expression = expression.replace("|(", 'any([') \
                               .replace("&(", 'all([') \
                               .replace(")", '])')     \
                               .replace("!(", 'any(not i for i in [')  # Replace NOT operator
        
        # Step 3: Evaluate the transformed Python expression
        return eval(expression) 
"""
Leetcode 1106: Parsing A Boolean Expression (https://leetcode.com/problems/parsing-a-boolean-expression/description/)

A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
->  't' that evaluates to true.
->  'f' that evaluates to false.
->  '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
->  '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
->  '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.

Given a string expression that represents a boolean expression, return the evaluation of that expression.
It is guaranteed that the given expression is valid and follows the given rules.

Example 1:
Input: expression = "&(|(f))"
Output: false
Explanation: 
First, evaluate |(f) --> f. The expression is now "&(f)".
Then, evaluate &(f) --> f. The expression is now "f".
Finally, return false.

Example 2:
Input: expression = "|(f,f,f,t)"
Output: true
Explanation: The evaluation of (false OR false OR false OR true) is true.

Example 3:
Input: expression = "!(&(f,t))"
Output: true
Explanation: 
First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
Then, evaluate !(f) --> NOT false --> true. We return true.
 
Constraints:
1 <= expression.length <= 2 * 104
expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.

Approach:
1. Replace logical OR "|(" with any([ to convert it into Python’s any() function.
2. Replace logical AND "&(" with all([ to convert it into Python’s all() function.
3. Replace logical NOT "!(" with "any(not i for i in [" to handle negation correctly.
4. Replace closing parentheses ")" with "])" to ensure correct list formatting.
5. Replace boolean literals 't' with True and 'f' with False for Python evaluation.
6. Use eval() to compute the final result of the transformed boolean expression.
"""
