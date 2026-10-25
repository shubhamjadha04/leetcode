class Solution:
    def allCellsDistOrder(self, rows: int, cols: int,
                          rCenter: int, cCenter: int) -> list[list[int]]:

        res = []

        for r in range(rows):
            for c in range(cols):
                res.append([r, c])

        res.sort(key=lambda cell: abs(cell[0] - rCenter) + abs(cell[1] - cCenter))

        return res