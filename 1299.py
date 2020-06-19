lass Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_behind = arr[-1]
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > max_behind:
                temp = arr[i]
                arr[i] = max_behind
                max_behind = temp
            else:
                arr[i] = max_behind
        arr[-1] = -1
        return arr
