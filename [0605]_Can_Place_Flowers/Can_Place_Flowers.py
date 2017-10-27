class Solution(object):

    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0] + flowerbed + [0, 1]
        count = 0
        for i in flowerbed:
            if i == 0:
                count += 1
            elif count:
                n -= (count - 1) // 2
                if n < 1:
                    return True
                count = 0
        return False
