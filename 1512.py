class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
        
        result = 0
        for count in counter.values():
            result += count * (count - 1) / 2
        return int(result)
