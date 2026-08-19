class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reserved = {}

        # Store reserved seats row-wise
        for row, seat in reservedSeats:
            if row not in reserved:
                reserved[row] = set()
            reserved[row].add(seat)

        # Every completely empty row can fit 2 families
        ans = (n - len(reserved)) * 2

        # Check rows having reserved seats
        for seats in reserved.values():

            left = all(seat not in seats for seat in [2, 3, 4, 5])
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            if left:
                ans += 1

            if right:
                ans += 1

            elif not left and not right:
                middle = all(seat not in seats for seat in [4, 5, 6, 7])

                if middle:
                    ans += 1

        return ans