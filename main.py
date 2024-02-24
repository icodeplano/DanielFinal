import pygame
import time
from constants import SCREEN_SIZE, BACKGROUND_COLOR, FPS
from utility import render_entities
from objects import Player, Zombie
from pygame.math import Vector2
import math

zombie_spawn_cooldown = 3

current_cooldown = 3

def main():
    objects = []
    zombies = []

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Zombie Game")
    clock = pygame.time.Clock()
    dt = 1 / FPS

    player = Player(500, 100)
    player.position = Vector2(100, 100)
    objects.append(player)

    def spawn_zombie():
        global current_cooldown
        if time.time() - current_cooldown < 3:
            return

        current_cooldown = time.time()
        new_zombie = Zombie(400)
        objects.append(new_zombie)
        zombies.append(new_zombie)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            player.velocity += Vector2(0, -player.speed * dt)

        if keys[pygame.K_s]:
            player.velocity += Vector2(0, player.speed * dt)

        if keys[pygame.K_a]:
            player.velocity += Vector2(-player.speed * dt, 0)

        if keys[pygame.K_d]:
            player.velocity += Vector2(player.speed * dt, 0)

        spawn_zombie()

        for _, zombie in enumerate(zombies):
            zombie.move_towards(player.position, dt)
            #zombie.point_towards(player.position)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = Vector2(mouse_pos[0], mouse_pos[1])
        direction = mouse_pos - player.position
        mouse_direction = direction.normalize()
        player.angle = math.degrees(math.atan2(mouse_direction.x, mouse_direction.y)) - 95

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
