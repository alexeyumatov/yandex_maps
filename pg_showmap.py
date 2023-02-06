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
            if event.key == pygame.K_PAGEUP:
                if int(scale) < 17:
                    scale = int(scale) + 1
            if event.key == pygame.K_PAGEDOWN:
                if int(scale) > 0:
                    scale = int(scale) - 1
            if int(scale) > 10:
                ratio = 0.005
            else:
                ratio = 0.01
            if float(latitude) - ratio > 0 or float(longitude) - ratio > 0 or \
                    float(latitude) + ratio < 90 or float(longitude) + ratio < 180:
                if event.key == pygame.K_LEFT:
                    latitude = float(latitude) - ratio
                if event.key == pygame.K_UP:
                    longitude = float(longitude) + ratio
                if event.key == pygame.K_RIGHT:
                    latitude = float(latitude) + ratio
                if event.key == pygame.K_DOWN:
                    longitude = float(longitude) - ratio

            response = get_map(f"ll={latitude},{longitude}&z={scale}", "map")
            screen.blit(pygame.image.load(write_file(response)), (0, 0))
            pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
    # Удаляем за собой файл с изображением.
    os.remove(map_file)
