# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

    def cloneGraph(self, node):
        def dfs(node, sheet):
            if node in sheet:
                return sheet[node]
            new = UndirectedGraphNode(node.label)
            sheet[node] = new
            for i in node.neighbors:
                new.neighbors.append(dfs(i, sheet))
            return new

        if node is None:
            return None
        return dfs(node, {})
