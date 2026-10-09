class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res =[]

        for i in range(len(nums)):
            res.append(sum(nums[:i+1]))


        return res
        