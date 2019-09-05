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
    card_skin_first = pygame.Surface((60, 90))
    card_skin_first.fill((0,0,255))
    card_skin_second = pygame.Surface((60, 90))
    card_skin_second.fill((0,255,0))
    first = []
    second = []
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
                if mouse_position[0] >= 200 and mouse_position[0] <= 290:
                    card_selected = ceil(mouse_position[1]/70)-1
                    if first == []:
                        first = card_selected
                    elif second == []:
                        second = card_selected
                    else:
                        first = card_selected
                        second = []

        pygame.display.update()
        screen.fill((0, 0, 0))
        i = 0
        while i < len(card_pos):
            show = card_skin
            if i == first:
                show = card_skin_first
            elif i == second:
                show = card_skin_second
            screen.blit(show, card_pos[i])
            i+=1

