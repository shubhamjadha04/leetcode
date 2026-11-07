class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-","").upper()
        res = ""

        i = len(s)-1
        j = 0
        while i >= 0:
            res+=s[i]
            j+=1
            i-=1

            if j == k and i >= 0:
                res += "-"
                j = 0

        return res[::-1]


        