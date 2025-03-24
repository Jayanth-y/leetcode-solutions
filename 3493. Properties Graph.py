class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)

        # Step 1: Convert each property list to a set
        ps = [set(prop) for prop in properties]
        graph = defaultdict(list)

        # Step 2-4: Build the graph based on set intersection
        for i in range(n):
            for j in range(i + 1, n):
                if len(ps[i] & ps[j]) >= k:
                    graph[i].append(j)
                    graph[j].append(i)

        # Step 6: DFS to explore all nodes in a connected component
        def dfs(node, seen):
            seen[node] = True
            for neighbor in graph[node]:
                if not seen[neighbor]:
                    dfs(neighbor, seen)

        seen = [False] * n
        count = 0

        # Step 7: Count connected components
        for node in range(n):
            if not seen[node]:
                count += 1
                dfs(node, seen)

        return count

"""
Leetcode 3493: Properties Graph (https://leetcode.com/problems/properties-graph/description/)

You are given a 2D integer array properties having dimensions n x m and an integer k.
Define a function intersect(a, b) that returns the number of distinct integers common to both arrays a and b.
Construct an undirected graph where each index i corresponds to properties[i]. 
There is an edge between node i and node j if and only if intersect(properties[i], properties[j]) >= k, where i and j are in the range [0, n - 1] and i != j.
Return the number of connected components in the resulting graph.

Example 1:
Input: properties = [[1,2],[1,1],[3,4],[4,5],[5,6],[7,7]], k = 1
Output: 3
Explanation: The graph formed has 3 connected components:

Example 2:
Input: properties = [[1,2,3],[2,3,4],[4,3,5]], k = 2
Output: 1
Explanation: The graph formed has 1 connected component:

Example 3:
Input: properties = [[1,1],[1,1]], k = 2
Output: 2
Explanation: intersect(properties[0], properties[1]) = 1, which is less than k. This means there is no edge between properties[0] and properties[1] in the graph.

Constraints:
1 <= n == properties.length <= 100
1 <= m == properties[i].length <= 100
1 <= properties[i][j] <= 100
1 <= k <= m

Approach (Step-by-Step)
1. Convert each properties[i] list to a set to allow fast intersection checks.
2. Initialize an undirected graph using adjacency lists.
3. For every pair of indices (i, j) such that i < j, compute the set intersection of properties[i] and properties[j].
4. If the number of distinct common elements is greater than or equal to k, add an undirected edge between i and j in the graph.
5. Initialize a visited list (seen) to track visited nodes.
6. Define a DFS traversal function to mark all nodes in a connected component as visited.
7. For each unvisited node, start a DFS and increment the component counter.
8. After all nodes are visited, return the total number of connected components.
"""
