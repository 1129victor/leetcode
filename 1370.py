class Solution:
    def sortString(self, s: str) -> str:
        data = dict(collections.Counter(s))
        print(data)
        seq = sorted(data.keys())
        print(seq)
        result = ''
        for i in seq[::-1]:
            print(i)

        while sum(data.values()) > 0:
            for i in seq:
                if data[i] > 0:
                    result += i
                    data[i] -= 1
            for i in seq[::-1]:
                if data[i] > 0:
                    result += i
                    data[i] -= 1
        return result
