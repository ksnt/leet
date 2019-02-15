import math
from operator import itemgetter
class Solution:  
    def distance(self,i,l):
        return (i,math.sqrt(l[0] ** 2 + l[1] ** 2))
    
    def kClosest(self, points: 'List[List[int]]', K: 'int') -> 'List[List[int]]':
        res = []
        tmp = []
        for i,p in enumerate(points):
            tmp.append(self.distance(i,p))
        tmp = sorted(tmp,key=itemgetter(1))
        for j in range(K):
            res.append(points[tmp[j][0]])
        return res

        