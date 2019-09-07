import pygame
from pygame.locals import *
from math import ceil
from src import numbers_gen
import copy
from src import sort_algs

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
    # criando superfície das cartas
    card_skin = pygame.Surface((60, 90))
    card_skin.fill((150, 65, 200))
    card_skin_first = pygame.Surface((60, 90))
    card_skin_first.fill((0,0,255))
    card_skin_second = pygame.Surface((60, 90))
    card_skin_second.fill((0,255,0))
    # criando fonte dos números das cartas
    myfont = pygame.font.SysFont('bold', 48)
    first = []
    second = []
    dict = {}
    numbers = numbers_gen.numbers_gen()
    i = 0
    sorted_numbers = copy.copy(numbers)
    user_swaps = 0
    sorted_numbers, machine_swaps = sort_algs.insertion_sort(sorted_numbers)
    while i < len(numbers):
        dict[card_pos[i]] = numbers[i]
        i+=1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_position = (pygame.mouse.get_pos()[1], pygame.mouse.get_pos()[0])
                if mouse_position[0] >= 200 and mouse_position[0] <= 290:
                    card_selected = ceil(mouse_position[1]/70)-1
                    if card_selected == first:
                        first = []
                    elif first == []:
                        first = card_selected
                    elif second == []:
                        second = card_selected
                    else:
                        first = card_selected
                        second = []
        pygame.display.update()
        screen.fill((0, 0, 0))

        if second != [] and first != []:
            pos_a = ()
            pos_b = ()
            a = 0
            b = 0
            for i in dict:
                if a == first:
                    pos_a = i
                elif b == second:
                    pos_b = i
                a+=1
                b+=1
            dict[pos_a], dict[pos_b] = dict[pos_b], dict[pos_a]
            numbers[first], numbers[second] = numbers[second], numbers[first]
            user_swaps+=1
            if numbers == sorted_numbers:
                print("uhuuull")
                print(user_swaps)
            first = []
            second = []

        i = 0
        while i < len(card_pos):
            show = card_skin
            if i == first:
                show = card_skin_first
            elif i == second:
                show = card_skin_second
            screen.blit(show, card_pos[i])

            i+=1

        for pos in card_pos:
            number_surface = myfont.render(str(dict[pos]), False, (255, 255, 255))
            screen.blit(number_surface, (pos[0]+2, pos[1] + 30))


