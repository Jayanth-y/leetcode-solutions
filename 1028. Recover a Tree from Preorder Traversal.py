# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, s: str) -> TreeNode:
        # Step 1: Extract node values and their depth levels
        def separate_traversal(s: str):
            nodes, levels, i = [], [], 0

            while i < len(s):
                # Extract number (node value)
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = (num * 10) + int(s[i])  # Build number digit by digit
                    i += 1
                nodes.append(num)  # Store node value
            
                # Count dashes (-) to determine depth level
                depth = 0
                while i < len(s) and s[i] == '-':
                    depth += 1
                    i += 1
                
                if depth > 0:
                    levels.append(depth)  # Store depth level

            return nodes, levels

        # Step 2: Rebuild the tree using extracted values and depths
        def build_tree(nodes, depth):
            if not nodes: 
                return None

            # First value is always the root node
            root = TreeNode(nodes[0])
            stack = [root]  # Stack to track nodes
            level, i = 1, 1  # Start from the second node

            for d in depth:
                node = TreeNode(nodes[i])  # Create new node
                
                # Find the correct parent by popping from stack
                while level != d:
                    stack.pop()  # Remove nodes that are too deep
                    level -= 1
                
                parent = stack[-1]  # Get the last node from the stack

                # Attach node as left child if empty, otherwise right child
                if parent.left is None:
                    parent.left = node
                else:
                    parent.right = node

                # Add new node to stack and update depth level
                stack.append(node)
                level += 1
                i += 1

            return root

        nodes, levels = separate_traversal(s)  # Step 1: Extract data
        return build_tree(nodes, levels)  # Step 2: Build the tree
      
"""
Leetcode 1028. Recover a Tree from Preorder Traversal (https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/)

We run a preorder depth-first search (DFS) on the root of a binary tree.
At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  If the depth of a node is D, the depth of its immediate child is D + 1.  The depth of the root node is 0.
If a node has only one child, that child is guaranteed to be the left child.
Given the output traversal of this traversal, recover the tree and return its root.

Example 1:
Input: traversal = "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: traversal = "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]

Example 3:
Input: traversal = "1-401--349---90--88"
Output: [1,401,null,349,88,90]
 
Constraints:
The number of nodes in the original tree is in the range [1, 1000].
1 <= Node.val <= 109

Approach:
Step 1: Extract Node Values & Their Depths  
     a. Read the string character by character.
     b. If we find a number, it is a node value.
     c. If we find dashes (-), count how many there are. This tells us the depth of the node.
     d. Store the values in nodes[] and their depths in levels[].
     
Step 2: Rebuild the Tree
     a. The first value in nodes[] is always the root node.
     b. Use a stack to keep track of parent-child relationships.
     c. For each new node:
     d. If its depth is greater, it becomes the left child of the last node in the stack.
     e. Otherwise, go up in the stack until we find the correct parent, then make it the right child.
     f. Keep updating the stack to maintain the correct structure.


"""
