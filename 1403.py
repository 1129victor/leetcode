class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse = True)
        result = []
        nowSum = 0
        total = sum(nums)
        for i in nums:
            nowSum += i
            result.append(i)
            if nowSum > total - nowSum:
                break
            
        return result
