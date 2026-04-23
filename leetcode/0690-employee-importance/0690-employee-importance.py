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
        employee = {e.id:e for e in employees}
        visited = set()
        total = 0
        def dfs(empId):
            nonlocal total
            visited.add(empId)
            emp = employee[empId]
            total+=emp.importance
            for i in emp.subordinates:
                if i not in visited:
                    dfs(i)
                    
        dfs(id)
        return total