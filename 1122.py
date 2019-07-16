class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        arr1 = sorted(arr1)
        #print(arr1)
        for a2 in arr2:
            n = arr1.count(a2)
            #print(n)
            while n > 0:
                res.append(a2)
                arr1.remove(a2)
                n = n -1
        #print(arr1)
        return(res + arr1)