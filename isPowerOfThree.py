'''
Given an integer, write a function to determine if it is a power of three.

Could you do it without using any loop / recursion?
'''
import math

class Solution:

    # recursion solution
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # recursion have time exceed

        # return n > 0 and (n == 1 or self.isPowerOfThree(n/3))

        # iteration, also time exceed

        # if n < 0:
        #     return False
        # while (n % 3) == 0:
        #     n /= 3
        #
        # return n == 1

        # math solution

        if n <= 0:
            return False
        return ((math.log10(n) / math.log10(3)) % 1) == 0