import pygame
import os
from samples.mapapi_PG import get_map

FPS = 24


def show_map(latitude, longitude, spn):
    map_file = get_map(f"ll={latitude},{longitude}&spn={spn}", "map")
    # Инициализируем pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    # Рисуем картинку, загружаемую из только что созданного файла.
    screen.blit(pygame.image.load(map_file), (0, 0))

    pygame.display.flip()
    clock = pygame.time.Clock()

    # Главный цикл
    running = True
    while running:
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
        clock.tick(FPS)

    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_file)
