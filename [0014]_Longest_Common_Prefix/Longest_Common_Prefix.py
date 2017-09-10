class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == [] or '' in strs:
            return ''
        length = len(strs[0])
        n = len(strs)
        for i in range(1, n):
            l = len(strs[i])
            if l < length:
                length = l
        target = strs[0][0:length]
        for i in range(1, n):
            while length:
                if target[0:length] == strs[i][0:length]:
                    break
                else:
                    length -= 1
        return target[0:length]
