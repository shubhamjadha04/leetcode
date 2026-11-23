class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        count = {}

        para = re.findall(r'[a-z]+', paragraph.lower())

        res = []

        for word in para:
            s = ""

            for w in word:
                if w.isalpha():
                    s += w

            if s:
                res.append(s)

        for i in res:
            if i not in banned:
                count[i] = count.get(i, 0) + 1

        max_word = max(count, key=count.get)

        return max_word