import sys
input = sys.stdin.readline
import heapq

def solve():
    n = int(input().strip())
    heap = []
    logs = n
    operations = []
    for _ in range(n):
        op = input().split()

        if op[0] == "removeMin":
            if not heap:
                logs += 1
                operations.append("insert 1")
            else:
                heapq.heappop(heap)

        elif op[0] == "getMin":
            _min = int(op[1])

            while heap and heap[0] < _min:
                heapq.heappop(heap)
                logs += 1
                operations.append("removeMin")

            if not heap or heap[0] != _min:
                logs += 1
                heapq.heappush(heap,_min)
                operations.append("insert "+str(_min))
            
        else:
            heapq.heappush(heap,int(op[1]))
        
        operations.append(" ".join(op))
    print(logs)
    for operation in operations:
        print(operation)

solve()