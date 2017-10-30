"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):

    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        sheet = {}
        for i in employees:
            sheet[i.id] = i
        father = [sheet[id]]
        res = 0
        while father:
            child = []
            for i in father:
                res += i.importance
                child.extend([sheet[x] for x in i.subordinates])
            father = child
        return res
