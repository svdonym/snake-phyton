import pygame
import sys
from game.board import Board
from game.snake import Snake
from game.food import Food
from game.obstacles import Obstacles
from game.powerups import PowerUps
from ui.menu import Menu
from ui.hud import HUD
from ui.gameover import GameOver

def main():
    pygame.init()
    clock = pygame.time.Clock()
    
    # Set up the game window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game")

    # Initialize game components
    board = Board(screen_width, screen_height)
    snake = Snake()
    food = Food(board)
    obstacles = Obstacles(board)
    powerups = PowerUps(board)
    menu = Menu()
    hud = HUD()
    game_over_screen = GameOver()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update game state
        snake.move()
        if snake.check_collision():
            game_over_screen.display_gameover()
            running = False

        if food.check_eaten(snake):
            snake.grow()
            food.spawn_food()

        # Draw everything
        board.draw(screen)
        snake.draw(screen)
        food.draw(screen)
        obstacles.draw(screen)
        powerups.draw(screen)
        hud.draw(screen)

        pygame.display.flip()
        clock.tick(15)  # Control the game speed

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()