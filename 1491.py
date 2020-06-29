class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(-1)
        salary.pop(0)
        
        return sum(salary) / len(salary)
