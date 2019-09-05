import pygame
from pygame.locals import *
from math import ceil

def start():
    pygame.init()

    screen_size = (710, 512)

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Sort the cards')

    w = 10
    card_pos = []
    # criando posições das cartas
    while w < 705:
        card_pos.append((w, 200))
        w += 70
    print(len(card_pos))
    # criando superfície das cartas
    card_skin = pygame.Surface((60, 90))
    card_skin.fill((150, 65, 200))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
                print(mouse_position)
                if mouse_position[0] >= 200 and mouse_position[0] <= 290:
                    print(ceil(mouse_position[1]/70))
        pygame.display.update()
        screen.fill((0, 0, 0))
        for i in card_pos:
            screen.blit(card_skin, i)

