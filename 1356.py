class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr),key=lambda arr:bin(arr).count("1"))
