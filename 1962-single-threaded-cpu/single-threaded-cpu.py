class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(x,y,i) for i,[x,y] in enumerate(tasks)]
        tasks.sort()
        i, n = 0, len(tasks)
        currtime = tasks[0][0]
        heap = []
        res = []
        while i < n or heap:
            if not heap and i < n and currtime < tasks[i][0]:
                currtime = tasks[i][0]
            
            while i < n and currtime >= tasks[i][0]:
                s,p,index = tasks[i]
                heapq.heappush(heap,(p,index))
                i += 1
            
            p,idx = heapq.heappop(heap)
            currtime += p
            res.append(idx)

        return res