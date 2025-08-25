class GameOver:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont('Arial', 48)
        self.restart_font = pygame.font.SysFont('Arial', 24)

    def display_gameover(self, score):
        self.screen.fill((0, 0, 0))
        gameover_surface = self.font.render('Game Over', True, (255, 0, 0))
        score_surface = self.font.render(f'Your Score: {score}', True, (255, 255, 255))
        restart_surface = self.restart_font.render('Press R to Restart', True, (255, 255, 255))

        self.screen.blit(gameover_surface, (self.screen.get_width() // 2 - gameover_surface.get_width() // 2, self.screen.get_height() // 2 - 50))
        self.screen.blit(score_surface, (self.screen.get_width() // 2 - score_surface.get_width() // 2, self.screen.get_height() // 2))
        self.screen.blit(restart_surface, (self.screen.get_width() // 2 - restart_surface.get_width() // 2, self.screen.get_height() // 2 + 50))

        pygame.display.flip()

    def restart_game(self):
        # Logic to reset the game state can be implemented here
        pass