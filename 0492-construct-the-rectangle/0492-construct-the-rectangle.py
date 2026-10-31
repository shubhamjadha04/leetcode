class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        l = int(area**0.5)
        length=0

        while l > 0:
            if area % l == 0:
                length = l
                break
            l-=1

        width = area//length

        return [width,length]
        

        