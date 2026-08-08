class Solution:
    def validSequence(self, word1: str, word2: str) -> list[int]:
        n = len(word1)
        m = len(word2)

        # suffix[i] = maximum number of characters
        # of word2 that can be matched using word1[i:]
        suffix = [0] * (n + 1)

        j = m - 1

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1]

            if j >= 0 and word1[i] == word2[j]:
                suffix[i] += 1
                j -= 1

        ans = []
        j = 0
        used_mismatch = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not used_mismatch:
                remaining_word2 = m - j - 1
                remaining_word1 = n - i - 1

                if suffix[i + 1] >= remaining_word2:
                    ans.append(i)
                    j += 1
                    used_mismatch = True

        if j == m:
            return ans

        return []