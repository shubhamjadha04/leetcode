class Solution:
    def findLHS(self, nums: list[int]) -> int:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] +=1
            else:
                dic[num] = 1

        
        max_len = 0

        for num in dic:
            if num+1 in dic:
                length = dic[num] + dic[num+1]
                max_len = max(length,max_len)

        
        return max_len

        