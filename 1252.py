import numpy as np
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        origin = np.zeros((n, m))
        for i in indices:
            origin[i[0],:] += 1
            origin[:,i[1]] += 1
            
        return int(np.sum(origin[:] % 2))
