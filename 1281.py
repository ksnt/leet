class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n_str = str(n)
        product = 1
        summension = 0
        for s in n_str:
            product = product * int(s)
            summension = summension + int(s)
        return product - summension