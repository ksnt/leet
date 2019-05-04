from collections import Counter
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:                        
        common = Counter(A[0])                
        for str in A[1:]:
            common &= Counter(str)                                    
        return list(common.elements())