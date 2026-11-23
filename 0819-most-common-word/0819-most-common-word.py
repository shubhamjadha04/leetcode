class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:

        count = {}

        para = re.findall(r'[a-z]+', paragraph.lower())

        for i in para:
            if i not in banned:
                count[i] = count.get(i, 0) + 1

        max_word = max(count, key=count.get)

        return max_word