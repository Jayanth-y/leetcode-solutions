class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(node, ch):
            if node:
                # Step 2: Update the max value seen so far on the path
                ch = max(ch, node.val)
                
                # Step 3: Check if current node is a good node
                if ch <= node.val:
                    # Step 4: Count the node if it's good
                    self.goodNodeCount += 1
                
                # Step 5: Recurse into left child
                if node.left:
                    helper(node.left, ch)
                
                # Step 5: Recurse into right child
                if node.right:
                    helper(node.right, ch)

        # Step 1: Start from root and initialize good node counter
        self.goodNodeCount = 0
        helper(root, -maxsize)  # Use negative infinity to ensure root is counted
        return self.goodNodeCount

"""
1448. Count Good Nodes in Binary Tree (https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
 
Constraints:
The number of nodes in the binary tree is in the range [1, 10^5].
Each node's value is between [-10^4, 10^4].

Approach (Step-by-Step):
1. Use a recursive helper function to traverse the tree starting from the root.
2. Pass the maximum value (ch) seen on the path from the root to the current node.
3. If the current node's value is greater than or equal to all previous values (ch), it's a good node.
4. Increment the good node counter if the node is good.
5. Recur for left and right subtrees with the updated maximum value.
"""
