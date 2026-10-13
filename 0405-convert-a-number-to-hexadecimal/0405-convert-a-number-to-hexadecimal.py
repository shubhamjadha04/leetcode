class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hexa_char = "0123456789abcdef"
        res = ""

        num = num & 0xFFFFFFFF

        while num > 0:
            rem = num%16
            res = hexa_char[rem]+res
            num = num//16

        return res