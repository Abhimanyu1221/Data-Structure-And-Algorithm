class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)

        if k == 1:
            candidates = [x for x in freq if freq[x] == 1]
            return max(candidates) if candidates else -1

        if k == n:
            return max(nums)

        candidates = []
        if freq[nums[0]] == 1:
            candidates.append(nums[0])
        if freq[nums[-1]] == 1:
            candidates.append(nums[-1])

        return max(candidates) if candidates else -1