# Snake Game

This is a simple Snake game implemented in Python using the Pygame library. The game features a snake that grows as it eats food, obstacles to avoid, and power-ups to enhance gameplay.

## Project Structure

```
snake-game
├── src
│   ├── main.py          # Entry point of the game
│   ├── game             # Game logic and mechanics
│   │   ├── __init__.py
│   │   ├── snake.py     # Snake class for managing the snake
│   │   ├── food.py      # Food class for generating food items
│   │   ├── board.py     # Board class for the game area
│   │   ├── obstacles.py  # Obstacles class for managing obstacles
│   │   └── powerups.py   # PowerUps class for managing power-ups
│   ├── ui               # User interface components
│   │   ├── __init__.py
│   │   ├── menu.py      # Menu class for the main menu
│   │   ├── hud.py       # HUD class for displaying game stats
│   │   └── gameover.py   # GameOver class for handling game over screen
│   ├── assets           # Assets for sounds and themes
│   │   ├── sounds.py    # Sound management
│   │   └── themes.py    # Theme management
│   └── utils            # Utility functions
│       ├── __init__.py
│       └── helpers.py    # Helper functions
├── requirements.txt      # Dependencies for the project
└── README.md             # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd snake-game
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Game

To start the game, run the following command:
```
python src/main.py
```

## Gameplay

- Use the arrow keys to control the snake.
- Eat the food to grow the snake.
- Avoid obstacles and the snake's own body.
- Collect power-ups for special abilities.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements!