class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = collections.Counter(arr)
        result = []
        for i in dic:
            if dic.get(i) not in result:
                result.append(dic.get(i))
            else:
                return False
        return True
