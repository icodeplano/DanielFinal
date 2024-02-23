import pygame
from constants import SCREEN_SIZE, BACKGROUND_COLOR, FPS
from utility import render_entities
from objects import Player, Zombie
from vector2d import Vector2D
import math


def main():
    objects = []

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Zombie Game")
    clock = pygame.time.Clock()
    dt = 1 / FPS

    player = Player(500, 100)
    objects.append(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player.velocity += Vector2D(0, -player.speed * dt)

        if keys[pygame.K_s]:
            player.velocity += Vector2D(0, player.speed * dt)

        if keys[pygame.K_a]:
            player.velocity += Vector2D(-player.speed * dt, 0)

        if keys[pygame.K_d]:
            player.velocity += Vector2D(player.speed * dt, 0)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = Vector2D(mouse_pos[0], mouse_pos[1])
        direction = mouse_pos - player.position
        mouse_direction = direction.unit()
        player.angle = math.radians(math.atan2(mouse_direction.x, mouse_direction.y))

        screen.fill(BACKGROUND_COLOR)
        render_entities(screen, objects, dt)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"An error occurred! Read below.\n{error}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
