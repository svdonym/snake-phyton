class PowerUps:
    def __init__(self):
        self.powerups = []
        self.types = ['speed', 'size', 'invincibility']
    
    def spawn_powerup(self, board_width, board_height):
        import random
        x = random.randint(0, board_width - 1)
        y = random.randint(0, board_height - 1)
        type = random.choice(self.types)
        self.powerups.append({'position': (x, y), 'type': type})
    
    def apply_effect(self, snake, powerup):
        if powerup['type'] == 'speed':
            snake.speed += 1
        elif powerup['type'] == 'size':
            snake.grow()
        elif powerup['type'] == 'invincibility':
            snake.invincible = True
    
    def check_collision(self, snake):
        for powerup in self.powerups:
            if snake.position == powerup['position']:
                self.apply_effect(snake, powerup)
                self.powerups.remove(powerup)