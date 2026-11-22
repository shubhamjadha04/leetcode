class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:

        count = {}
        res = []

        for i in range(len(mat)):
            s = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    s +=1

            count[i] = s

        
        count = dict(sorted(count.items(), key = lambda x: x[1]))

        for key in count:
            res.append(key)

        
        return res[:k]

        

        

        