class Menu:
    def __init__(self):
        self.options = ["Start Game", "Options", "Quit"]
        self.selected = 0

    def display_menu(self, screen):
        screen.fill((0, 0, 0))  # Clear the screen with black
        font = pygame.font.SysFont(None, 55)
        title_surface = font.render("Snake Game", True, (255, 255, 255))
        screen.blit(title_surface, (screen.get_width() // 2 - title_surface.get_width() // 2, 100))

        for i, option in enumerate(self.options):
            color = (255, 255, 0) if i == self.selected else (255, 255, 255)
            option_surface = font.render(option, True, color)
            screen.blit(option_surface, (screen.get_width() // 2 - option_surface.get_width() // 2, 250 + i * 60))

        pygame.display.flip()

    def handle_selection(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.selected = (self.selected - 1) % len(self.options)
        elif keys[pygame.K_DOWN]:
            self.selected = (self.selected + 1) % len(self.options)
        elif keys[pygame.K_RETURN]:
            return self.options[self.selected]
        return None