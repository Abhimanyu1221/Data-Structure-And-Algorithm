class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []

        for length in range(2, 10):          # Number of digits
            for start in range(10 - length): # Starting index
                num = int(s[start:start + length])

                if low <= num <= high:
                    ans.append(num)

        return ans