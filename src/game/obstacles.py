class Obstacles:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.obstacles = []

    def generate_obstacles(self, count):
        import random
        for _ in range(count):
            x = random.randint(0, self.board_width - 1)
            y = random.randint(0, self.board_height - 1)
            self.obstacles.append((x, y))

    def check_collision(self, position):
        return position in self.obstacles

    def reset_obstacles(self):
        self.obstacles.clear()