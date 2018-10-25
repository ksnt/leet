class Solution:
    def isLongPressedName(self,name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0
        while j < len(typed):
            #print(i)
            if i < len(name) and name[i] == typed[j] :
                    i = i + 1
            j = j + 1
        return i == len(name) and j == len(typed)