class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step 1: Build the graph as adjacency list
        graph = defaultdict(list)
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        # Step 2: Initialize shortest time to each node
        time = [math.inf] * n
        time[0] = 0

        # Step 3: Initialize number of shortest paths to each node
        pc = [0] * n
        pc[0] = 1

        # Step 4: Min-heap to simulate Dijkstra's algorithm
        pq = [(0, 0)]  # (current_time, node)

        # Step 5-9: Standard Dijkstra with path count tracking
        while pq:
            ct, node = heapq.heappop(pq)

            for neighbor, tt in graph[node]:
                nt = ct + tt

                if nt < time[neighbor]:
                    time[neighbor] = nt
                    pc[neighbor] = pc[node]
                    heapq.heappush(pq, (nt, neighbor))

                elif nt == time[neighbor]:
                    pc[neighbor] += pc[node]

        # Step 10: Return count of shortest paths to node n-1
        return pc[n-1] % (10**9 + 7)

"""
Leetcode 1976: Number of Ways to Arrive at Destination (https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/)

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. 
The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. 
You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.
Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

Example 1:
Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

Example 2:
Input: n = 2, roads = [[1,0,10]]
Output: 1
Explanation: There is only one way to go from intersection 0 to intersection 1, and it takes 10 minutes.
 
Constraints:
1 <= n <= 200
n - 1 <= roads.length <= n * (n - 1) / 2
roads[i].length == 3
0 <= ui, vi <= n - 1
1 <= timei <= 109
ui != vi
There is at most one road connecting any two intersections.
You can reach any intersection from any other intersection.

Approach (Step-by-Step)
1. Build an adjacency list graph from the given list of roads.
2. Initialize a time array where time[i] stores the shortest time to reach node i. Set time[0] = 0 and all others to infinity.
3. Initialize a pc array (path_count) to track the number of shortest paths to each node. Set pc[0] = 1 since there's exactly one way to start at node 0.
4. Use a priority queue (min-heap) to perform Dijkstra's algorithm, starting from node 0.
5. For each node popped from the queue:
6. Iterate over all its neighbors and compute the new potential time nt = current_time + edge_weight.
7. If this nt is less than the recorded time[neighbor], update time[neighbor] and set pc[neighbor] = pc[current_node].
8. If nt is equal to the recorded shortest time to the neighbor, add the current node's path count to the neighbor’s path count.
9. Continue until all nodes have been visited.
10. Return pc[n-1] % (10^9 + 7) — the number of ways to reach the destination in minimum time.
"""
