class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0 or n<0:
            return False
        for i in range(n):
            x = 2**i
            if x == n:
                return True

            if x>n:
                return False
        