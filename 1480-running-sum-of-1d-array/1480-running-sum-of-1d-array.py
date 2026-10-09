class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        res =[]
        max_sum = 0

        for i in range(len(nums)):
            max_sum += nums[i]

            res.append(max_sum)

        return res
            


        
        