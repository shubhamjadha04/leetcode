class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        words = "abcdefghijklmnopqrstuvwxyz"
        d = {}

        for i in range(len(words)):
            d[words[i]] = widths[i]


        res = []
        count = 1
        S= 0

        for w in s:
            if S + d[w] > 100:
                count += 1
                S = d[w]
            else:
                S += d[w]

        return [count, S]

        