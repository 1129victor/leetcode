class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dic={}
        for i in range(len(mat)):
            dic[i] = sum(mat[i])
            
        
        SortDic = sorted(dic.items(), key=lambda d: d[1])
        result = []
        for i in range(k):
            result.append(SortDic[i][0])
        return result
