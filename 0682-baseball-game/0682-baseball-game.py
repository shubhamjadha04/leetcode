class Solution:
    def calPoints(self, operations: list[str]) -> int:
        res = []

        for i in range(len(operations)):

            if operations[i] == "+":
                res.append(res[-1]+res[-2])

            elif operations[i]=="D":
                pro = res[-1]*2
                res.append(pro)

            elif operations[i] == "C":
                res.pop()

            else:
                res.append(int(operations[i]))

        return sum(res)

        