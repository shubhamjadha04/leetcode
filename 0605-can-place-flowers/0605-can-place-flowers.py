class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0

        if n == 0:
            return True

        for i in range(len(flowerbed)):

            left = 0 if i == 0 else flowerbed[i - 1]
            right = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]

            if flowerbed[i] == 0 and left == 0 and right == 0:
                flowerbed[i] = 1
                count += 1

                if count >= n:
                    return True

        return False