class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            num= num**2
            res.append(num)

        
        return sorted(res)

        

        
        