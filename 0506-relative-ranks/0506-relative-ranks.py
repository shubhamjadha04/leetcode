class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        rank ={}

        s = sorted(score, reverse= True)

        for i in range(len(s)):
            rank[s[i]] = i+1

        res =[]
        for x in score:
            r = rank[x]

            if r == 1:
                res.append("Gold Medal")
            
            elif r == 2:
                res.append("Silver Medal")

            elif r == 3:
                res.append("Bronze Medal")
            
            else:
                res.append(str(r))

        return res 


        