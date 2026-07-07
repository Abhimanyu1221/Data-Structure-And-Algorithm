class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''.join(ch for ch in str(n) if ch != '0')

        if not x:
            return 0

        return int(x) * sum(int(ch) for ch in x)