class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Get unique values and sort them
        sorted_unique = sorted(set(arr))

        # Assign ranks starting from 1
        rank = {}
        for i, val in enumerate(sorted_unique):
            rank[val] = i + 1

        # Replace each element with its rank
        return [rank[val] for val in arr]