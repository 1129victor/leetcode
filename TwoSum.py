from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n =len(nums)
        dic={}
        for i in range(0,n):
            if dic.get(target-nums[i])!=None:
                return [i,dic[target-nums[i]]];
            dic[nums[i]]=i
            #print('%d %d' % (nums[i], i))
        return []
                

nums = [9, 5, 7, 3,2,4]
target = 6

test=Solution()
result=test.twoSum(nums, target)

print(result)
