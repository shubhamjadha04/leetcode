
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        count = [0] * 26

        for ch in licensePlate.lower():
            if 'a' <= ch <= 'z':
                count[ord(ch) - ord('a')] += 1

        res = ""

        for word in words:
            word_count = [0] * 26

            for ch in word.lower():
                if 'a' <= ch <= 'z':
                    word_count[ord(ch) - ord('a')] += 1

            valid = True

            for i in range(26):
                if word_count[i] < count[i]:
                    valid = False
                    break

            if valid:
                if res == "" or len(word) < len(res):
                    res = word

        return res
