class Theme:
    def __init__(self, name, background_color, snake_color, food_color, obstacle_color):
        self.name = name
        self.background_color = background_color
        self.snake_color = snake_color
        self.food_color = food_color
        self.obstacle_color = obstacle_color

class ThemeManager:
    def __init__(self):
        self.themes = {}
        self.current_theme = None

    def add_theme(self, theme):
        self.themes[theme.name] = theme

    def load_theme(self, name):
        if name in self.themes:
            self.current_theme = self.themes[name]
        else:
            raise ValueError(f"Theme '{name}' not found.")

    def apply_theme(self):
        if self.current_theme:
            return {
                "background_color": self.current_theme.background_color,
                "snake_color": self.current_theme.snake_color,
                "food_color": self.current_theme.food_color,
                "obstacle_color": self.current_theme.obstacle_color,
            }
        return None

# Example themes
def initialize_themes():
    theme_manager = ThemeManager()
    
    classic_theme = Theme("Classic", (0, 0, 0), (0, 255, 0), (255, 0, 0), (255, 255, 0))
    dark_theme = Theme("Dark", (30, 30, 30), (0, 200, 0), (200, 0, 0), (200, 200, 0))
    
    theme_manager.add_theme(classic_theme)
    theme_manager.add_theme(dark_theme)
    
    return theme_manager