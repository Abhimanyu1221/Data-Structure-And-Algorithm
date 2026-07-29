import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)

        if not self._isPalindromePossible(count):
            return ""

        halfCount, midLetter = self._getHalfCountAndMidLetter(count)

        totalPerm = self._countArrangements(halfCount)
        if k > totalPerm:
            return ""

        leftHalf = self._generateLeftHalf(halfCount, k)

        return "".join(leftHalf) + midLetter + "".join(reversed(leftHalf))

    def _isPalindromePossible(self, count):
        oddCount = sum(1 for x in count.values() if x & 1)
        return oddCount <= 1

    def _getHalfCountAndMidLetter(self, count):
        half = [0] * 26
        mid = ""

        for ch, freq in count.items():
            half[ord(ch) - ord("a")] = freq // 2
            if freq & 1:
                mid = ch

        return half, mid

    def _generateLeftHalf(self, halfCount, k):
        length = sum(halfCount)
        ans = []

        for _ in range(length):
            for i in range(26):
                if halfCount[i] == 0:
                    continue

                halfCount[i] -= 1

                ways = self._countArrangements(halfCount)

                if ways >= k:
                    ans.append(chr(i + ord("a")))
                    break

                k -= ways
                halfCount[i] += 1

        return ans

    def _countArrangements(self, cnt):
        total = sum(cnt)
        res = 1

        for f in cnt:
            res *= self._nCk(total, f)

            if res >= self.MAX:
                return self.MAX

            total -= f

        return res

    def _nCk(self, n, k):
        k = min(k, n - k)

        res = 1
        for i in range(1, k + 1):
            res = res * (n - i + 1) // i

            if res >= self.MAX:
                return self.MAX

        return res