class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        n = len(s)
        matched = 0

        # Match target as far as possible.
        for i in range(n):
            x = ord(target[i]) - ord('a')

            if freq[x] == 0:
                # target[i] is unavailable.
                # Try making the answer greater at this position.
                for c in range(x + 1, 26):
                    if freq[c] > 0:
                        freq[c] -= 1

                        ans = target[:i] + chr(c + ord('a'))

                        for j in range(26):
                            ans += chr(j + ord('a')) * freq[j]

                        return ans

                break

            freq[x] -= 1
            matched += 1

        # Backtrack only through characters that were actually matched.
        for i in range(matched - 1, -1, -1):
            x = ord(target[i]) - ord('a')

            # Restore the character matched at position i.
            freq[x] += 1

            # Try the smallest character greater than target[i].
            for c in range(x + 1, 26):
                if freq[c] > 0:
                    freq[c] -= 1

                    ans = target[:i] + chr(c + ord('a'))

                    for j in range(26):
                        ans += chr(j + ord('a')) * freq[j]

                    return ans

        return ""