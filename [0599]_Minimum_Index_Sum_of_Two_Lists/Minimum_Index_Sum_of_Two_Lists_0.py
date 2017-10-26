class Solution(object):

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        sheet = {}
        min_sum = 2000
        choice = []
        for index, value in enumerate(list1):
            sheet[value] = index
        for i in range(len(list2)):
            try:
                each_sum = sheet[list2[i]] + i
                if each_sum == min_sum:
                    choice.append(list2[i])
                if each_sum < min_sum:
                    choice = [list2[i]]
                    min_sum = each_sum
            except KeyError:
                pass
        return choice
