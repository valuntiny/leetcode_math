'''
Count the number of prime numbers less than a non-negative number, n.
'''


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n <= 2:
            return 0

        result = [True] * n
        result[0] = result[1] = False # < 0 and < 1 doesn't have any prime

        for i in range(2, int(n ** 0.5) + 1):
            if result[i]:
                result[i * i:n:i] = [False] * len(result[i * i:n:i])

        return sum(result)