class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull, cow = 0, 0
        sheet = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                sheet[guess[i]] = sheet.get(guess[i], 0) - 1
                if sheet[guess[i]] >= 0:
                    cow += 1
                sheet[secret[i]] = sheet.get(secret[i], 0) + 1
                if sheet[secret[i]] <= 0:
                    cow += 1
        return '%dA%dB' % (bull, cow)
