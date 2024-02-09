import pygame
from constants import SCREEN_SIZE, BACKGROUND_COLOR, FPS


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    dt = 1 / FPS

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND_COLOR)

        pygame.display.flip()
        dt = clock.tick(FPS) / 1000


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print(f"An error occurred! Read below.\n{error}")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
