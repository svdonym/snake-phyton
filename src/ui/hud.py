class HUD:
    def __init__(self, screen):
        self.screen = screen
        self.score = 0
        self.lives = 3
        self.font = pygame.font.SysFont('Arial', 24)

    def update_score(self, points):
        self.score += points

    def draw(self):
        score_surface = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        lives_surface = self.font.render(f'Lives: {self.lives}', True, (255, 255, 255))
        self.screen.blit(score_surface, (10, 10))
        self.screen.blit(lives_surface, (10, 40))

    def reset(self):
        self.score = 0
        self.lives = 3