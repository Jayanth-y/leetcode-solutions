# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        if root is None: 
            return
        
        # Step 2: Initialize a set to store recovered values
        self.seen = set()

        def helper(node: Optional[TreeNode], dir: int, rv: int):
            # Step 3: Recover the node value based on parent value
            node.val = ((2*rv) + dir)
            self.seen.add(node.val)  # Store the value in the set
            
            # Step 3a: Recur for the left child if it exists
            if node.left is not None: 
                helper(node.left, 1, node.val)            
            
            # Step 3b: Recur for the right child if it exists
            if node.right is not None: 
                helper(node.right, 2, node.val)
            
        # Step 3: Start recursion from the root with value 0
        helper(root, 0, 0)

    # Step 4: Check if target exists in the recovered values set
    def find(self, target: int) -> bool:
        return (target in self.seen)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
"""
Leetcode 1261: Find Elements in a Contaminated Binary Tree

Given a binary tree with the following rules:
root.val == 0
For any treeNode:
If treeNode.val has a value x and treeNode.left != null, then treeNode.left.val == 2 * x + 1
If treeNode.val has a value x and treeNode.right != null, then treeNode.right.val == 2 * x + 2
Now the binary tree is contaminated, which means all treeNode.val have been changed to -1.

Implement the FindElements class:
FindElements(TreeNode* root) Initializes the object with a contaminated binary tree and recovers it.
bool find(int target) Returns true if the target value exists in the recovered binary tree.
 

Example 1:
Input
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
Output
[null,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 

Example 2:
Input
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
Output
[null,true,true,false]
Explanation
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False

Example 3:
Input
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
Output
[null,true,false,false,true]
Explanation
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True
 

Constraints:
TreeNode.val == -1
The height of the binary tree is less than or equal to 20
The total number of nodes is between [1, 104]
Total calls of find() is between [1, 104]
0 <= target <= 106

Approach:
1. If root is None, return immediately.
2. Initialize a set self.iota to store valid values after recovery.
3. Define a recursive helper function to recover values:
   a. Set node.val = (2 * parent_val) + dir (where dir is 0 for root, 1 for left child, 2 for right child).
   b. Store node.val in self.iota.
   c. Recursively call helper on node.left (if exists) with dir=1 and node.val as new parent value.
   d. Recursively call helper on node.right (if exists) with dir=2 and node.val as new parent value.
4. find(target) simply checks if target exists in self.iota.
"""
