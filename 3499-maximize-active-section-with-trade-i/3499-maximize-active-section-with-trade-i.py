class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = 0
        runs = []

        i = 0

        while i < len(s):
            j = i

            while j < len(s) and s[j] == s[i]:
                j += 1

            runs.append((s[i], j - i))

            if s[i] == '1':
                ones += j - i

            i = j

        ans = ones

        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1':
                left = runs[i - 1]
                right = runs[i + 1]

                if left[0] == '0' and right[0] == '0':
                    ans = max(ans, ones + left[1] + right[1])

        return ans