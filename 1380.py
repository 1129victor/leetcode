import numpy as np

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minRow = {min(row) for row in matrix}
        maxCol = {max(col) for col in zip(*matrix)}
        return list(minRow & maxCol)
