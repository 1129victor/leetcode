class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        NonCount = 0
        for i in zip(*A):
            if list(i) != sorted(i):
                NonCount += 1
        return NonCount
