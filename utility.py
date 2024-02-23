import pygame


def render_entities(screen: pygame.Surface, object_list: list, dt):
    for image_object in object_list:
        image_object.update(dt)

        image = pygame.transform.rotate(image_object.image, image_object.angle)
        position = image_object.position

        screen.blit(image, (position.x, position.y))
