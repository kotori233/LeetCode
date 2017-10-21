class Solution(object):

    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        pigs = 0
        n = minutesToTest // minutesToDie + 1
        while n ** pigs < buckets:
            pigs += 1
        return pigs
