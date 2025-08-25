class Snake:
    def __init__(self, initial_position, initial_length=1):
        self.body = [initial_position]
        self.direction = (0, 1)  # Moving down by default
        self.growth_pending = 0

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.body.insert(0, new_head)

        if self.growth_pending > 0:
            self.growth_pending -= 1
        else:
            self.body.pop()

    def grow(self):
        self.growth_pending += 1

    def check_collision(self, position):
        return position in self.body

    def change_direction(self, new_direction):
        # Prevent the snake from reversing
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def get_head_position(self):
        return self.body[0]

    def get_body(self):
        return self.body[1:]  # Return the body excluding the head

    def reset(self, initial_position):
        self.body = [initial_position]
        self.direction = (0, 1)
        self.growth_pending = 0