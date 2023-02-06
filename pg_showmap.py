import pygame
import os
from samples.mapapi_PG import get_map
from functions import write_file

FPS = 60


def show_map(latitude, longitude, scale):
    response = get_map(f"ll={latitude},{longitude}&z={scale}", "map")
    map_file = write_file(response)
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
                if int(scale) < 17:
                    scale = int(scale) + 1
                response = get_map(f"ll={latitude},{longitude}&z={scale}", "map")
                screen.blit(pygame.image.load(write_file(response)), (0, 0))
            if event.key == pygame.K_DOWN:
                if int(scale) > 0:
                    scale = int(scale) - 1
                response = get_map(f"ll={latitude},{longitude}&z={scale}", "map")
                screen.blit(pygame.image.load(write_file(response)), (0, 0))
            pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_file)
