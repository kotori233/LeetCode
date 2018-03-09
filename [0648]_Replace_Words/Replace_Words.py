class Solution(object):

    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split(' ')
        dict.sort(key=len)
        ret = [[] for i in range(26)]
        for each in dict:
            ret[ord(each[0]) - 97].append(each)
        res = []
        for each in sentence:
            for word in ret[ord(each[0]) - 97]:
                if len(each) < len(word):
                    break
                if each[:len(word)] == word:
                    each = word
            res.append(each)
        return ' '.join(res)
