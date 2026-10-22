class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expect = (n*(n+1))//2
        total = sum(nums)

        return expect - total
        
    

        

        