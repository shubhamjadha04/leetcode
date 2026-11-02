class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                 "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                 "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                 "-.--", "--.."]

        unique = set()

        for word in words:
            transformation = ""

            for char in word:
                index = ord(char) - ord('a')
                transformation += morse[index]

            unique.add(transformation)

        return len(unique)