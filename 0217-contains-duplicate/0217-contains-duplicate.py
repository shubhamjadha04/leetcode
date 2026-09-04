class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}

        for key in nums:
            if key in d:
                return True
            else:
                d[key] = 1

        return False
        