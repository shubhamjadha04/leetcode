class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        

        for key in nums:
            if key in freq:
                freq[key]+=1

            else:
                freq[key] = 1

        for key in freq:
            if freq[key] == 1:
                return key


         
        