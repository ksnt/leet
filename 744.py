class Solution:
    def nextGreatestLetter(self,letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters = sorted(list(set(letters)))
        if len(letters) == 1: return letters[0]
        for i,s in enumerate(letters):
            if s == target and i < len(letters)-1:
                return letters[i+1]
            if s == target and i == len(letters)-1:
                return letters[0]
            if s > target:
                return letters[i]
        return letters[0]