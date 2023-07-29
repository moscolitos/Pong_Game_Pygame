# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 20:13:46 2023

@author: Mosco
"""

import pygame


class Paddle:
    """
    Represents a paddle in the Pong game. 
    A paddle has a rectangle shape and can move up or down.
    """
    def __init__(self, x, y):
        """
        Initializes a new Paddle object.
        
        Args:
        x (int): The initial x-coordinate of the paddle.
        y (int): The initial y-coordinate of the paddle.
        """
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 15, 80)

    def draw(self, screen):
        """
        Draws the paddle on the given screen.
        
        Args:
        screen (pygame.Surface): The surface to draw on.
        """
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move(self, speed):
        """
        Moves the paddle according to the user's key presses.
        
        Args:
        speed (int): The speed of the paddle movement.
        """
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -speed)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, speed)
    def ai_move(self, ball, speed):
        """
        Moves the AI-controlled paddle in response to the ball's position.
        
        Args:
        ball (Ball): The ball that the AI responds to.
        speed (int): The speed of the paddle movement.
        """
        
        if ball.rect.bottom > self.rect.bottom:
            self.rect.move_ip(0, speed)
        elif ball.rect.top < self.rect.top:
            self.rect.move_ip(0, -speed)




    def check_bounds(self, screen_height):
        """
        Checks if the paddle has hit the top or bottom of the screen, and prevents it from moving past those bounds.
        
        Args:
        screen_height (int): The height of the screen.
        """
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > screen_height:
            self.rect.bottom = screen_height


class Ball:
    """
    Represents a ball in the Pong game. A ball has a rectangle shape and can move in any direction.
    """
    def __init__(self, x, y):
        """
        Initializes a new Ball object.
        
        Args:
        x (int): The initial x-coordinate of the ball.
        y (int): The initial y-coordinate of the ball.
        """
        self.x = x
        self.y = y
        self.dx = 1  # direction of ball in x-axis
        self.dy = 1  # direction of ball in y-axis
        self.rect = pygame.Rect(self.x, self.y, 15, 15)

    def draw(self, screen):
        """
        Draws the ball on the given screen.
        
        Args:
        screen (pygame.Surface): The surface to draw on.
        """
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def move(self, speed, game):
        """Moves the ball and checks if the ball has hit the left or right of the screen.
        
        Args:
        speed (int): The speed of the ball movement.
        game (PongGame): The game object.
        """
        self.rect.move_ip(self.dx * speed, self.dy * speed)
        if self.rect.left < 0:
            game.score[1] += 1
            game.reset()
        if self.rect.right > game.screen.get_width():
            game.score[0] += 1
            game.reset()

    def bounce(self, axis):
        """
        Reverses the ball's direction on the given axis.
        
        Args:
        axis (str): The axis to bounce the ball on ('x' or 'y').
        """
        if axis == 'x':
            self.dx *= -1
        elif axis == 'y':
            self.dy *= -1


class PongGame:
    """
    Represents a Pong game. A game has two paddles, a ball, a score, and game settings like speed.
    """
    def __init__(self, width=800, height=600):
        """Initializes a new PongGame object.
        Args:
        
        width (int, optional): The width of the game screen. Defaults to 800.
        height (int, optional): The height of the game screen. Defaults to 600.
        """
        
        pygame.init()
        self.font = pygame.font.Font(None, 36)
        self.score = [0, 0]  # Score for player 1 and 2

        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.paddle_speed = 2
        self.ball_speed = 2
        self.paddle1 = Paddle(0, height / 2)
        self.paddle2 = Paddle(width - 15, height / 2)
        self.ball = Ball(width / 2, height / 2)
    
    def reset(self):
        """
        Resets the game to its initial state, with paddles and the ball in their original positions.
        """
        width, height = self.screen.get_size()
        self.paddle1 = Paddle(0, height / 2)
        self.paddle2 = Paddle(width - 15, height / 2)
        self.ball = Ball(width / 2, height / 2)
    def menu(self):
        """
        Shows the game's menu, where the player can choose a difficulty level for the AI opponent.
        """
        font = pygame.font.Font(None, 36)
        button_width = 200
        button_height = 50

        easy_button = pygame.Rect(self.screen.get_width()/2 - button_width/2, 
                                  self.screen.get_height()/2 - button_height/2 - 100, 
                                  button_width, button_height)
        medium_button = pygame.Rect(self.screen.get_width()/2 - button_width/2, 
                                    self.screen.get_height()/2 - button_height/2, 
                                    button_width, button_height)
        hard_button = pygame.Rect(self.screen.get_width()/2 - button_width/2, 
                                  self.screen.get_height()/2 - button_height/2 + 100, 
                                  button_width, button_height)

        buttons = [(easy_button, 'easy'), (medium_button, 'medium'), (hard_button, 'hard')]

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    for button, difficulty in buttons:
                        if button.collidepoint(mouse_pos):
                            self.ai_speed = {'easy': 1.5, 'medium': 2, 'hard': 2.5}[difficulty]
                            return

            self.screen.fill((0, 0, 0))
            for button, difficulty in buttons:
                pygame.draw.rect(self.screen, (255, 255, 255), button, 2)
                text = font.render(difficulty.capitalize(), True, (255, 255, 255))
                text_rect = text.get_rect(center=button.center)
                self.screen.blit(text, text_rect)
            
            pygame.display.flip()
            self.clock.tick(60)



    def run_game(self):
        """
        Runs the main game loop, where all the game logic takes place.
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.paddle1.move(self.paddle_speed)
            self.paddle1.check_bounds(self.screen.get_height())
            self.paddle2.ai_move(self.ball, self.paddle_speed)
            self.paddle2.check_bounds(self.screen.get_height())
            self.ball.move(self.ball_speed, self)
            
            if self.ball.rect.colliderect(self.paddle1.rect) or self.ball.rect.colliderect(self.paddle2.rect):
                self.ball.bounce('x')
            elif self.ball.rect.top <= 0 or self.ball.rect.bottom >= self.screen.get_height():
                self.ball.bounce('y')

            self.screen.fill((0, 0, 0))
            self.paddle1.draw(self.screen)
            self.paddle2.draw(self.screen)
            self.ball.draw(self.screen)
            
            score_text = self.font.render(f"Player 1: {self.score[0]}  Player 2: {self.score[1]}", True, (255, 255, 255))
            self.screen.blit(score_text, (self.screen.get_width() / 2 - score_text.get_width() / 2, 10))

            pygame.display.flip()
            self.clock.tick(60)


if __name__ == "__main__":
    pong = PongGame()
    pong.menu()
    pong.run_game()
