class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # method for graph traversal in both directions
        graph = defaultdict(dict)
        count = 0

        for u, v in connections:
            graph[u][v] = 1 # original direction (away from current city)
            graph[v][u] = 0 # reverse direction (toward current city)

        # finds all nodes directing away from 0 and adds them to the count
        def dfs(root):
            nonlocal count
            visited.add(root)
            for node, val in graph[root].items():
                if node not in visited:
                    if val == 1:
                        count += 1
                    dfs(node)

        
        visited = set()

        dfs(0)

        return count
