class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        result=[]
        for i in range(len(prices)):
            done = False
            now = prices[i]
            for j in range(i + 1, len(prices)):
                if now >= prices[j] :
                    now = prices[j]
                    done = True
                    break
            if done == False :
                result.append(prices[i])
            else:
                result.append(prices[i] - now)
        return result
