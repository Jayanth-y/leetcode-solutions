# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def makeTree():
            # Step 1: Create root node from the last element of postorder
            node = TreeNode(postorder.pop())

            # Step 2: Base case - If preorder is empty, return node
            if not preorder:
                return node  

            # Check if the next element in preorder exists in postorder
            if node.val != preorder[-1]:  
                node.right = makeTree()  # Recursively construct right subtree
            
            if node.val != preorder[-1]:  
                node.left = makeTree()   # Recursively construct left subtree

            # Step 3: Remove the processed node from preorder list
            preorder.pop()

            return node  # Return the constructed node

        return makeTree()
"""
Leetcode 889: Construct Binary Tree from Preorder and Postorder Traversal (https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/)

Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct values.
And postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.
If there exist multiple answers, you can return any of them.

Example 1:
Input: preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
Output: [1,2,3,4,5,6,7]

Example 2:
Input: preorder = [1], postorder = [1]
Output: [1]
 
Constraints:
1 <= preorder.length <= 30
1 <= preorder[i] <= preorder.length
All the values of preorder are unique.
postorder.length == preorder.length
1 <= postorder[i] <= postorder.length
All the values of postorder are unique.
It is guaranteed that preorder and postorder are the preorder traversal and postorder traversal of the same binary tree.

Ideaology:
1. Preorder Traversal (Root → Left → Right)
    a. First element is always the root.
    b. Second element is the left child (if it exists).

2. Postorder Traversal (Left → Right → Root)
    a. Last element is always the root.
    b. The second last element is the right child (if it exists).

Using this information, we can recursively reconstruct the tree.

Approach:
1. Base Case: If preorder or postorder is empty, return None.
2. Create the root node using the first element of preorder.
3. Find the left subtree:
    a. The left child (if exists) is the second element of preorder.
    b. Find its position in postorder to determine the subtree boundaries.
4. Recursively construct left and right subtrees.
5. Return the root node.
"""
