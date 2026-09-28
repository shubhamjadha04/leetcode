class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        if m*n != r*c:
            return mat

        res = []
        temp = []


        for row in mat:
            for num in row:
                temp.append(num)

                if len(temp) == c:
                    res.append(temp)
                    temp = []

        return res  