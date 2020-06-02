from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False for _ in range(len(candies))]
        print(result)
        max_candies = max(candies)
        
        for idx, candycount in enumerate(candies):
            if candycount + extraCandies >= max_candies:
                result[idx] = True
        return result
        
candies = [12,1,12]
extraCandies = 10

        
ansclass = Solution()
result = ansclass.kidsWithCandies(candies, extraCandies)

print(result)
