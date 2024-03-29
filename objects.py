from pygame.math import Vector2
import math
import pygame

player_img_prev = pygame.image.load("assets/player.png")
zombie_img_prev = pygame.image.load("assets/zombie.png")

player_img = pygame.transform.scale_by(player_img_prev, 0.5)
zombie_img = pygame.transform.scale_by(zombie_img_prev, 0.5)


def clamp(n, min_num, max_num):
    if n < min_num:
        return min_num
    elif n > max_num:
        return max_num
    else:
        return n


class Image:
    def __init__(self, image):
        self.image = image
        self.position = Vector2(0, 0)
        self.angle = 0


class Entity(Image):
    def __init__(self, image, speed, max_health):
        super().__init__(image)
        self.velocity = Vector2(0, 0)
        self.speed = speed
        self.drag = 2
        self._max_health = max_health
        self._health = max_health

    def update(self, dt):
        self.velocity *= 1 - self.drag * dt
        self.position += self.velocity * dt
        print(self.angle)

    def change_health(self, by):
        self._health = clamp(self._health + by, 0, self._max_health)


class Player(Entity):
    def __init__(self, speed, max_health=100):
        super().__init__(player_img, speed, max_health)


class Zombie(Entity):
    def __init__(self, speed, max_health=100):
        super().__init__(zombie_img, speed, max_health)

    def move_towards(self, position: Vector2, dt):
        direction = (position - self.position).normalize()
        self.velocity += direction * self.speed * dt

    def point_towards(self, position):
        direction = position - self.position
        mouse_direction = direction.normalize()
        self.angle = math.degrees(math.atan2(mouse_direction.x, mouse_direction.y)) - 95

