class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        Arr = sorted(arr)
        n = len(Arr)
        minVal = Arr[1] - Arr[0]
        result = [[Arr[1], Arr[0]]]
        for i in range(2, n):
            temp = Arr[i] - Arr[i - 1]
            if temp < minVal:
                minVal = temp
                result = [[Arr[i - 1], Arr[i]]]
            elif temp == minVal:
                result.append([Arr[i - 1], Arr[i]])
        return result
        
