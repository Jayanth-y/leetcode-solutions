class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        d = len(graph) - 1

        def findPaths(node, path):
            # Step 4: Reached destination
            if node == d:
                res.append(path)
                return
            
            # Step 5-6: Explore neighbors recursively
            for neighbor in graph[node]:
                findPaths(neighbor, path + [neighbor])

        # Step 7: Start from node 0
        findPaths(0, [0])
        return res

"""
Leetcode 797: All Paths From Source to Target (https://leetcode.com/problems/all-paths-from-source-to-target/description/)

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
 
Constraints:
n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.

Approach (Step-by-Step)
1. Initialize an empty list res to store all valid paths.
2. Define the destination node d as len(graph) - 1.
3. Define a recursive function findPaths(node, path) that explores paths from the current node.
4. If the current node is the destination d, append a copy of the path to res.
5. Otherwise, iterate over all neighbors of the current node.
6. For each neighbor, recursively call findPaths(neighbor, path + [neighbor]).
7. Start DFS from node 0 with the path [0].
8. Return the result list res.
"""
