class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        arr = []

        for row in grid:
            for value in row:
                arr.append(value)

        total = m * n
        k = k % total

        arr = arr[total - k:] + arr[:total - k]

        result = []

        for i in range(0, total, n):
            result.append(arr[i:i + n])

        return result