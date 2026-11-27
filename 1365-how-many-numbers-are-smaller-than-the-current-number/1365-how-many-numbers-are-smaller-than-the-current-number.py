class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        first = {}

        for i,x in enumerate(sorted(nums)):
            if x not in first:
                first[x] = i

        
        res = []

        for n in nums:
            res.append(first[n])

        return res
        