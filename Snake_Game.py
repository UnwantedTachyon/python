import sys
import random

import pygame
from pygame.math import Vector2


pygame.init()

display_width = 800
display_height = 600
game_display = pygame.display.set_mode((display_width, display_height))
DISPLAY_RECT = pygame.Rect(0, 0, display_width, display_height)

WHITE = pygame.Color('white')
BLACK = pygame.Color('black')
TEAL = pygame.Color(0, 128, 128)


def update_snake(snake, new_pos):
    for part in snake:
        part.topleft, new_pos = new_pos, part.topleft


def check_death(snake):
    touched_body = any(snake[0].colliderect(part) for part in snake[1:])
    in_game_area = DISPLAY_RECT.contains(snake[0])
    return touched_body or not in_game_area


def main():
    clock = pygame.time.Clock()
    score = 60
    size = 10
    snake = [pygame.Rect(10, y, size, size) for y in range(20, 171, 10)]
    food = pygame.Rect(
        random.randrange(0, display_width, 10),
        random.randrange(0, display_height, 10),
        size, size)
    pos = Vector2(snake[0].topleft)
    vel = Vector2(10, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    vel = Vector2(-10, 0)
                elif event.key == pygame.K_d:
                    vel = Vector2(10, 0)
                elif event.key == pygame.K_w:
                    vel = Vector2(0, -10)
                elif event.key == pygame.K_s:
                    vel = Vector2(0, 10)
                elif event.key == pygame.K_c:
                    vel = Vector2(0, 0)

        pos += vel
        update_snake(snake, pos)

        if snake[0].colliderect(food):
            score += 10
            food.topleft = (random.randrange(0, display_width, 10),
                            random.randrange(0, display_height, 10))
            snake.append(snake[-1].copy())
            print(len(snake), score)

        if check_death(snake):
            running = False

        game_display.fill(WHITE)
        pygame.draw.rect(game_display, BLACK, food)
        for rect in snake:
            pygame.draw.rect(game_display, TEAL, rect)

        pygame.display.update()
        pygame.time.wait(35)
        clock.tick(60)


if __name__ == '__main__':
    main()
    pygame.quit()
    

