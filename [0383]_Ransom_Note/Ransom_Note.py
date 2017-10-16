class Solution(object):

    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        sheet = {}
        for i in magazine:
            if i in sheet:
                sheet[i] += 1
            else:
                sheet[i] = 1
        for i in ransomNote:
            if i not in sheet or sheet[i] == 0:
                return False
            sheet[i] -= 1
        return True
