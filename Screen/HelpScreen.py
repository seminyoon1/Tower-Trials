import pyautogui
import pygame
from pygame.locals import *

import GameState
import UIElement

BLUE = (106, 159, 181)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) 

def run(): 
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())

    fontsize = 60
    screen.blit(background, (0, 0))
    pygame.display.flip()

    titleElement = UIElement.UITextElement(
        center_position=(width*3 / 4, height* 5 / 6),
        font_size=int(fontsize*2/3),
        bg_rgb=None,
        text_rgb=WHITE,
        text="Back to Game",
        highlight_true = True,
        action=GameState.GameStates.GAME,
    )

    UIElement.writeText("Currently Working on Help Screen", fontsize/2, WHITE, (width/6, height/6), screen)

    viewHelp = True
    while viewHelp:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        title_action = titleElement.update(pygame.mouse.get_pos(), mouse_up)
        if title_action is not None:
            viewHelp = False    

        titleElement.draw(screen)

        pygame.display.flip()