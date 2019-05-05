class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("0b"+"".join(["0" if int(b)%2 == 1 else "1" for b in (bin(N)[2:])]),2)