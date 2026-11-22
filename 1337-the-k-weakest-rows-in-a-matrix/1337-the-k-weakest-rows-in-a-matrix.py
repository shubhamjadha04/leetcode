class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:

        res = []

        for i, val in enumerate(mat):
            res.append((val.count(1),i))

        
        res.sort()
        ans = []

        for i in range(k):
            ans.append(res[i][1])

        return ans

        

        

        