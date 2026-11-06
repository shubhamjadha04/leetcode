class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = {}

        # Count frequency of each number
        for num in arr1:
            count[num] = count.get(num, 0) + 1

        res = []

        # Add numbers in arr2 order
        for num in arr2:
            res.extend([num] * count[num])
            del count[num]

        # Add remaining numbers in ascending order
        for num in sorted(count):
            res.extend([num] * count[num])

        return res