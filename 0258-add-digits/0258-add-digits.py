class Solution:
    def addDigits(self, num: int) -> int:

        def add_digit(num):
            if len(str(num)) == 1:
                return num

            sum = 0
            while num > 0:
                digit = num%10
                sum+=digit
                num = num//10

            return add_digit(sum)

        return add_digit(num)
        