class Solution(object):

    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        all_words = ' '.join(sentence) + ' '
        length = len(all_words)
        occupy = 0
        for i in range(rows):
            occupy += cols
            # occupy正好装下(此行最后一个不是空格)
            if all_words[occupy % length] == ' ':
                # 为了与all_words格式一致，加一空格结尾
                occupy += 1
            else:
                # 除去末尾残留的半截单词，直至以空格结尾(与all_words格式一致)
                while occupy and all_words[(occupy - 1) % length] != ' ':
                    occupy -= 1
        return occupy // length
