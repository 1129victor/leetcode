class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for i in range((-1 * int(n / 2)), int(n / 2) + 1):
            result.append(i)
        if n % 2 == 0:
            result.pop(int(n / 2))
        return result
