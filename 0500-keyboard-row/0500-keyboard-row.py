class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        res = []
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        for word in words:
            

            if all(ch in row1 for ch in word.lower()):
                res.append(word)

            if all(ch in row2 for ch in word.lower()):
                res.append(word)
            
            if all(ch in row3 for ch in word.lower()):
                res.append(word)

        return res


        