class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}

        for key in nums:
            if key in d:
                d[key]+=1

            else:
                d[key] = 1

        
        for k in d:
            if d[k] >= len(nums)/2:
                return k
        