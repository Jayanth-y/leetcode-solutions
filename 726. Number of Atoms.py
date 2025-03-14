class Solution:
    def countOfAtoms(self, f: str) -> str:
        
        # Step 1: Parse the chemical formula
        def parseString(f: str):
            i = 0
            stack = [defaultdict(int)]  # Step 2: Initialize stack to store atom counts

            while i < len(f):
                # Step 4: Handle opening parenthesis by pushing a new dictionary
                if f[i] == "(":
                    i += 1
                    stack.append(defaultdict(int))
                
                # Step 5: Handle closing parenthesis and apply multipliers
                elif f[i] == ")":
                    i += 1
                    mul = 0
                    while i < len(f) and f[i].isdigit():
                        mul = mul*10 + int(f[i])
                        i += 1
                    mul = max(mul, 1)  # Default multiplier to 1 if none provided

                    temp = stack.pop()
                    for el, c in temp.items():
                        stack[-1][el] += c*mul  # Merge counts into previous dictionary
                
                # Step 6: Handle atomic elements and their counts
                else:
                    ne = re.match(r'([A-Z][a-z]*)(\d*)', f[i:])  # Extract element and count
                    el, c = ne.groups()
                    c = int(c) if c else 1  # Default count to 1 if none provided
                    stack[-1][el] += c  # Add element count to the current dictionary
                    i += len(ne.group(0))  # Move index forward
            
            return stack[0]  # Step 7: Return the final element count dictionary
        
        # Step 7: Retrieve and sort element counts
        ec = parseString(f)
        sec = sorted(ec.items())

        # Step 8: Construct the result string
        res = ""
        for e, c in sec:
            if c == 1: res += e
            else: res += f"{e}{c}"
        
        # Step 9: Return the formatted output
        return res

"""
Leetcode 726: Number of Atoms (https://leetcode.com/problems/number-of-atoms/description/)

Given a string formula representing a chemical formula, return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.
One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no digits will follow.

For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.\

For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.

For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

The test cases are generated so that all the values in the output fit in a 32-bit integer.

Example 1:
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
 
Constraints:
1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.

Approach (Step-by-Step)
1. Define a helper function parseString(f) to process the formula recursively.
2 .Initialize a stack with a defaultdict(int) to store atom counts.
3. Iterate through the formula character by character.
4. If the character is (, push a new defaultdict(int) onto the stack.
5. If the character is ), pop the top element and multiply all its counts by the following number (if any).
6. If the character is an atomic element, extract it and its count using regex and update the top dictionary on the stack.
7. After parsing, retrieve the atom counts from the stack and sort them alphabetically.
8. Construct the final result string, appending atom counts only if greater than 1.
9. Return the final formatted output.
"""
