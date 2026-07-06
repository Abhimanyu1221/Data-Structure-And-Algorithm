class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        maxRight = 0

        for left, right in intervals:

            if right > maxRight:
                count += 1
                maxRight = right

        return count