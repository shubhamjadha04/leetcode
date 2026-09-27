class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        map ={}
        used = set()

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in map:
                if map[a] != b:
                    return False

            else:
                if b in used:
                    return False

                map[a] = b
                used.add(b)
            
        return True



        