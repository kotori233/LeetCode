# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        if node is None:
            return None
        queue = [node]
        new = UndirectedGraphNode(node.label)
        sheet = {node: new}
        while queue:
            cur = queue.pop(0)
            for each in cur.neighbors:
                if each not in sheet:
                    queue.append(each)
                    copy = UndirectedGraphNode(each.label)
                    sheet[each] = copy
                    sheet[cur].neighbors.append(copy)
                else:
                    sheet[cur].neighbors.append(sheet[each])
        return new
