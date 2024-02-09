import pygame
import pymunk

object_list = []


class Object:
    def __init__(self, position):
        self.body = pymunk.Body()
        self.body.position = position


class ColoredObject(Object):
    def __init__(self, position, color):
        super().__init__(position)
        self.color = color


class Circle(ColoredObject):
    def __init__(self, space, color=(0, 0, 0), radius=25, position=(0, 0), mass=10, friction=1):
        super().__init__(position, color)
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.mass = mass
        self.shape.friction = friction
        space.add(self.body, self.shape)
        object_list.append(self)


def render_objects(screen):
    for index, object_class in enumerate(object_list):
        if isinstance(object_class, Circle):
            position = (object_class.body.position.x, object_class.body.position.y)
            py
