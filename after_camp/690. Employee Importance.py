
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.total_imp = 0
      
        def sumimportance(emp,employees):
            
            self.total_imp += emp.importance
            if not emp.subordinates:
                return self.total_imp
            for sub in emp.subordinates:
                for employee in employees:
                    if sub == employee.id:
                        sumimportance(employee, employees)
            return self.total_imp
        
        for employee in employees:
              
            if id == employee.id:
                return sumimportance(employee, employees)
         
            



