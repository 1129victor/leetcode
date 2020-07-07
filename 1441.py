class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        i, j = 1, 0
        while j < len(target):
            if i == target[j]:
                result.append("Push")
                i+=1
                j+=1
            else:
                result.append("Push")
                result.append("Pop")
                i+=1
        
        return result
