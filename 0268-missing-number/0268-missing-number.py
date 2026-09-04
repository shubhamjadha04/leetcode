class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        if nums[-1]!=n:
            return n
        
        if n == 1:
            return 0

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                return nums[i]-1

        return 0

        

        