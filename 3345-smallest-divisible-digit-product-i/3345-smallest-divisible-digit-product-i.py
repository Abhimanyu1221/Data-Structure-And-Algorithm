class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        while True:
            product = 1
            num = n

            while num > 0:
                product *= num % 10
                num //= 10

            if product % t == 0:
                return n

            n += 1