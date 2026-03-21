class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if num <= 1:
            return False

        sum1 = 1  
        i = 2

        while i * i <= num:
            if num % i == 0:
                sum1 += i
                if i != num // i:  
                    sum1 += num // i
            i += 1

        return sum1 == num
