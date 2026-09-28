class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = []
        i = 0
        j = 1

        while j <len(nums):
            res.append(min(nums[i],nums[j]))

            i +=2
            j +=2

        
        return sum(res)

        