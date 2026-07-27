class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest = 0
        second_largest = 0

        for num in nums:
            if num > largest:
                second_largest = largest
                largest = num
            elif num > second_largest:
                second_largest = num

        return (largest - 1) * (second_largest - 1)