class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:

        new_arr = sorted(arr)

        num = {}

        for n in new_arr:
            if n not in num:
                num[n] = len(num) + 1

        res = []

        for n in arr:
            res.append(num[n])

        return res