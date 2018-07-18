class Solution:
    def findRestaurant(self,list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        res = []
        for i,v in enumerate(list1):
            for j, w in enumerate(list2):
                if v==w:
                    res.append((i+j,v))
        res = sorted(res)
        standard_value = res[0][0]
        return [x[1] for x in res if x[0]==standard_value]