class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0,len(numbers)-1
        while numbers[l] + numbers[r] != target:
            if numbers[l] + numbers[r] == target:
                break
            elif numbers[l] + numbers[r] > target:
                r = r - 1
            else:
                l = l + 1
        return [l+1,r+1]
