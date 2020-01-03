class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n % 2 == 1: # odd
            return [i for i in range(-n//2 + 1, n//2 + 1)]
        else: # even
            return [i for i in range(-n//2, 0)] + [j for j in range(1, n//2 + 1)]