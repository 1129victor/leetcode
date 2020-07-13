class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        '''
        count = 0
        for i in arr1:
            for j in arr2:
                if abs(i - j) <= d:
                    count -= 1
                    break
            count += 1
        return count   
        '''
        Y = sorted(arr2)
        
        def okay(x: int) -> bool:
            i = bisect.bisect_left(Y, x)
            print(Y)
            print(x)
            print(i)
            for j in (i-1, i):
                print(j)
                if j < 0 or j >= len(Y):
                    continue
                if abs(x - Y[j]) <= d:
                    return False
            return True
        
        return sum(okay(x) for x in arr1)
