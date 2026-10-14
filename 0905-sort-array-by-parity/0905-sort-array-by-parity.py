class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        res = []
        odd =[]

        for num in nums:
            if num%2==0:
                res.append(num)
            else:
                odd.append(num)

        for num in  odd:
            res.append(num)

        return res
        