class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num

        while left<=right:
            mid = (left+right)//2
            sqr = mid *mid

            if sqr == num:
                return True

            if sqr < num:
                left = mid+1

            else:
                right = mid-1

        return False
         