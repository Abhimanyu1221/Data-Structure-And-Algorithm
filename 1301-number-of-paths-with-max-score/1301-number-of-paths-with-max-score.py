from typing import List

class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)

        score = [[-1] * n for _ in range(n)]
        ways = [[0] * n for _ in range(n)]

        score[0][0] = 0
        ways[0][0] = 1

        for i in range(n):
            for j in range(n):
                if board[i][j] == 'X':
                    continue

                if i == 0 and j == 0:
                    continue

                best = -1
                cnt = 0

                for x, y in [(i - 1, j), (i, j - 1), (i - 1, j - 1)]:
                    if x < 0 or y < 0:
                        continue

                    if score[x][y] > best:
                        best = score[x][y]
                        cnt = ways[x][y]

                    elif score[x][y] == best:
                        cnt = (cnt + ways[x][y]) % MOD

                if best == -1:
                    continue

                val = 0
                if board[i][j].isdigit():
                    val = int(board[i][j])

                score[i][j] = best + val
                ways[i][j] = cnt

        if ways[n - 1][n - 1] == 0:
            return [0, 0]

        return [score[n - 1][n - 1], ways[n - 1][n - 1]]