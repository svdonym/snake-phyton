class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def draw(self, surface):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:  # Snake body
                    pygame.draw.rect(surface, (0, 255, 0), (x * 20, y * 20, 20, 20))
                elif self.grid[y][x] == 2:  # Food
                    pygame.draw.rect(surface, (255, 0, 0), (x * 20, y * 20, 20, 20))
                elif self.grid[y][x] == 3:  # Obstacles
                    pygame.draw.rect(surface, (255, 255, 0), (x * 20, y * 20, 20, 20))

    def update(self, snake, food, obstacles):
        self.clear()
        for segment in snake.body:
            self.grid[segment[1]][segment[0]] = 1
        self.grid[food.position[1]][food.position[0]] = 2
        for obstacle in obstacles.positions:
            self.grid[obstacle[1]][obstacle[0]] = 3

    def clear(self):
        self.grid = [[0 for _ in range(self.width)] for _ in range(self.height)]