from collections import defaultdict

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u,v in edges:
            graph[v].append(u)
        
        res = [set() for _ in range(n)]
        visited = set()

        def dfs(idx):

            if idx in visited:
                return res[idx]
            
            for parent in graph[idx]:
                res[idx].add(parent)
                res[idx].update(dfs(parent))
            
            visited.add(idx)
            return res[idx]

        
        for i in range(n):
            dfs(i)
        
        return [sorted(list(r)) for r in res]
                