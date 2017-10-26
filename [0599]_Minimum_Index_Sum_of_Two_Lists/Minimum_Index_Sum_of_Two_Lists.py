class Solution(object):

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min_sum = len(list1) + len(list2)
        choice = []
        both = set(list1) & set(list2)
        for i in both:
            each_sum = list1.index(i) + list2.index(i)
            if each_sum == min_sum:
                choice.append(i)
            if each_sum < min_sum:
                choice = [i]
                min_sum = each_sum
        return choice
