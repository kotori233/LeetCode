from collections import Counter


class Solution(object):

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        c1 = Counter(s1)
        c2 = Counter()
        l1, l2 = len(s1), len(s2)
        left, right = 0, 0
        while right < l2:
            c2[s2[right]] += 1
            if c1 == c2:
                return True
            right += 1
            if right - left + 1 > l1:
                c2[s2[left]] -= 1
                if c2[s2[left]] == 0:
                    del c2[s2[left]]
                left += 1
        return False
