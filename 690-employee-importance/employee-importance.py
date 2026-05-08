"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp_sub = dict()
        for employee in employees:
            imp_sub[employee.id] = [employee.importance,employee.subordinates]

        def dfs(id):
            if not imp_sub[id]:
                return 0
            importance = imp_sub[id][0]
            for sub in imp_sub[id][1]:
                importance += dfs(sub)
            return importance
        return dfs(id)
