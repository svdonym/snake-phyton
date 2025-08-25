def random_position(board_width, board_height):
    import random
    return (random.randint(0, board_width - 1), random.randint(0, board_height - 1))

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

def clamp(value, min_value, max_value):
    return max(min_value, min(value, max_value))

def load_image(file_path):
    import pygame
    return pygame.image.load(file_path).convert_alpha()