class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_n = -1
        for i in range(len(arr)-1, -1, -1):
            arr[i], max_n = max_n, max(arr[i], max_n)
        return arr