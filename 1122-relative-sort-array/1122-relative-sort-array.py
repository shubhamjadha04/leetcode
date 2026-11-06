class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        res = []

        # Add elements according to arr2 order
        for i in arr2:
            for j in arr1:
                if i == j:
                    res.append(j)

        # Find elements that are not in arr2
        remaining = []

        for num in arr1:
            if num not in arr2:
                remaining.append(num)

        # Sort remaining elements
        remaining.sort()

        return res + remaining