class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dep = []
        dest = []
        for i, j in paths:
            dep.append(i)
            dest.append(j)
        return [result for result in dest if result not in dep][0]
