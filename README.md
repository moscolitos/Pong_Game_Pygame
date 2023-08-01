# Pong Game with Pygame using OOP
This project is an implementation of the classic Pong game using Python and Pygame. It features a simple AI that moves the paddle in response to the ball's position, and a difficulty selector in the main menu.

## Getting Started

### Prerequisites
Python 3.6 or higher
Pygame 1.9.6 or higher

You can install Pygame with pip:

pip install pygame

## Running the Game
To start the game, simply run the main Python script:

python pong_game.py

## Game Instructions
- Player controls the left paddle using the Up and Down arrow keys.
- The right paddle is controlled by an AI opponent.
- The ball moves automatically, and bounces off paddles and the top and bottom of the screen.
- If the ball hits the left or right edge of the screen, the other player scores a point.
- The game can be reset at any point by closing and reopening the program.

## Game Features
- AI Opponent: The right paddle is controlled by an AI that moves at a speed depending on the difficulty level selected in the menu.

- Difficulty Selector: At the start of the game, a menu is presented where you can select the difficulty level ('Easy', 'Medium', or 'Hard') for the AI opponent.

- Scoring System: The current score is displayed at the top of the screen. A point is scored when the ball hits the opponent's side of the screen.

- Game Reset: The game can be easily reset to its initial state, which moves the paddles and ball back to their starting positions.

## Code Structure

The game code is divided into three classes: Paddle, Ball, and PongGame.

- Paddle: Represents a paddle in the game. It has methods for drawing itself on the screen, moving according to user input, moving in response to the ball (for the AI paddle), and checking if it's hit the screen bounds.

- Ball: Represents the ball in the game. It has methods for drawing itself on the screen, moving, bouncing off paddles or the screen edges, and scoring points.

- PongGame: Represents the overall game. It has methods for initializing the game state, running the game loop, resetting the game, and showing the main menu.

## Authors
Moscolitos

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.




