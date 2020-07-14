class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        charsDict = Counter(chars)
        result = 0
        for i in words:
            for j in i:
                if j not in charsDict:
                    break
                if i.count(j) > charsDict[j]:
                    break
            else:
                result += len(i)
        return result
        
