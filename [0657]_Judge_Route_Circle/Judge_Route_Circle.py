class Solution(object):

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        sheet = {'R': 0, 'L': 0, 'U': 0, 'D': 0}
        for i in moves:
            sheet[i] += 1
        if sheet['R'] == sheet['L'] and sheet['U'] == sheet['D']:
            return True
        return False
