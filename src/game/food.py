class Food:
    def __init__(self, board_width, board_height):
        self.board_width = board_width
        self.board_height = board_height
        self.position = self.spawn_food()

    def spawn_food(self):
        import random
        x = random.randint(0, self.board_width - 1)
        y = random.randint(0, self.board_height - 1)
        return (x, y)

    def check_eaten(self, snake_position):
        return self.position == snake_position

    def respawn(self):
        self.position = self.spawn_food()