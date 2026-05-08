class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        def dfs(node,c):
            colors[node] = c
            for nei in graph[node]:
                if colors[nei] == -1:
                    if not dfs(nei,1-c):
                        return False
                elif colors[nei] == colors[node]:
                    return False
            return True
        
        for i in range(len(graph)):
            if colors[i] == -1 and not dfs(i,0):
                return False
        return True