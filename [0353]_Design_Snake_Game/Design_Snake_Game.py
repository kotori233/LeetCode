class SnakeGame(object):

    def __init__(self, width, height, food):
        """
        Initialize your data structure here.
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.width = width
        self.height = height
        self.food = food
        self.res = 0
        self.snake = [[0, 0]]

    def move(self, direction):
        """
        :type direction: int
        :rtype: int
        """
        i, j = self.snake[-1]
        tail = self.snake.pop(0)
        if direction == 'U':
            i -= 1
        elif direction == 'D':
            i += 1
        elif direction == 'L':
            j -= 1
        elif direction == 'R':
            j += 1
        if i < 0 or i >= self.height or \
                j < 0 or j >= self.width:
            return -1
        if [i, j] in self.snake:
            return -1
        self.snake.append([i, j])
        if self.food and [i, j] == self.food[0]:
            self.food.pop(0)
            self.snake.insert(0, tail)
            self.res += 1
        return self.res
