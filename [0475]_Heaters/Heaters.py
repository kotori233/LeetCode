class Solution(object):

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        d = 0
        houses.sort()
        heaters.sort()
        for each in houses:
            if each < heaters[0]:
                m = heaters[0] - each
            elif each > heaters[-1]:
                m = each - heaters[-1]
            else:
                left, right = 0, len(heaters) - 1
                while right - left > 1:
                    middle = (left + right) // 2
                    if heaters[middle] > each:
                        right = middle
                    else:
                        left = middle
                m = min(each - heaters[left], heaters[right] - each)
            d = max(m, d)
        return d
