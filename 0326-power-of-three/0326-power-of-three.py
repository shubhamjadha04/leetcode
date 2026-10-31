class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <=0:
            return False

        if n == 1:
            return True

        

        for i in range(1,n):
            if n == 3**i:
                return True

            if n < 3**i:
                return False
        