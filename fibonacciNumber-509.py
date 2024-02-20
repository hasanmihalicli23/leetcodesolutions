class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        x, y = 0, 1

        for i in range(n):
            x, y = y, x + y

        return x