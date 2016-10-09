from collections import deque
class SnakeGame(object):

    def __init__(self, width,height,food):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        :type width: int
        :type height: int
        :type food: List[List[int]]
        """
        self.snake = deque()
        self.snake.append((0,0))
        self.width = width
        self.height = height
        self.food = food
        self.dir = {'U':(-1,0), 'L':(0,-1), 'R':(0,1), 'D':(1, 0)}
        self.i = 0
        self.eat = 0

    def move(self, direction):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        :type direction: str
        :rtype: int
        """
        snake, width, height, food, dir = self.snake, self.width, self.height, self.food, self.dir
        head = snake[-1]
        newhead = (head[0]+dir[direction][0], head[1]+dir[direction][1])
        nofood = False
        if self.i>=len(food) or food[self.i][0]!=newhead[0] or food[self.i][1]!=newhead[1]:
            snake.popleft()
            nofood = True
        if newhead in snake:
            return -1
        if newhead[0]<0 or newhead[0]>=height or newhead[1]<0 or newhead[1]>=width:
            return -1
        if not nofood:
            self.eat += 1
            self.i += 1
        snake.append(newhead)
        return self.eat




# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)
