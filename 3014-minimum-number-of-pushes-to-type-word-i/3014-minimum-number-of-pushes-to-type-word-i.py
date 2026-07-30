class Solution:
    def minimumPushes(self, word: str) -> int:
        ans = 0
        chars = len(word)
        if chars<=8:
            return chars
        elif chars<=16:
            return (8+ (2*(chars - 8)))
        elif chars <=24:
            return 24 + (3*(chars - 16))
        return 48+ (4*(chars - 24))
            