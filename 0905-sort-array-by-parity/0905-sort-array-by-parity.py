class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        s = 0

        for i in range(n):
            if (nums[i]%2 == 0):
                nums[s],nums[i] =nums[i],nums[s]
                s+=1

        return  nums
        