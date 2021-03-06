import pyautogui
import pygame
from pygame.locals import *

import Character_Data.CharacterStats
import UIElement
import Game
import GameState

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def run():
    user = Game.user
    width, height = pyautogui.size()
    screen = pygame.display.set_mode((width, height))
    background = pygame.Surface(screen.get_size())

    fontsize = 60
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while user.getStatPoints() > 0:
        mouse_up = False

        textElement = UIElement.UITextElement(
            center_position=(width/6, height/ 8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Select a skill:",
            highlight_true = False,
            action=None,
        )
        defenseElement = UIElement.UITextElement(
            center_position=(width/6, height*2/ 8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Defense: " + str('%.1f'%(user.getStats()[0])),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        evasivenessElement = UIElement.UITextElement(
            center_position=(width/6, height*3/8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Evasiveness: " + str('%.1f'%(user.getStats()[1])),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        intelligenceElement = UIElement.UITextElement(
            center_position=(width/6, height*4/ 8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Intelligence: " + str('%.1f'%(user.getStats()[2])),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        attackElement = UIElement.UITextElement(
            center_position=(width/6, height*5/ 8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Attack: " + str('%.1f'%(user.getStats()[3])),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        powerElement = UIElement.UITextElement(
            center_position=(width/6, height*6/ 8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Power: " + str('%.1f'%(user.getStats()[4])),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        criticalElement = UIElement.UITextElement(
            center_position=(width/6, height*7/ 8),
            font_size=fontsize/2,
            bg_rgb=None,
            text_rgb=WHITE,
            text="Critical: " + str('%.1f'%(user.getStats()[5])),
            highlight_true = True,
            action= GameState.GameStates.GAME,
        )
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        defense_action = defenseElement.update(pygame.mouse.get_pos(), mouse_up)
        evasiveness_action = evasivenessElement.update(pygame.mouse.get_pos(), mouse_up)
        intelligence_action = intelligenceElement.update(pygame.mouse.get_pos(), mouse_up)
        attack_action = attackElement.update(pygame.mouse.get_pos(), mouse_up)
        power_action =  powerElement.update(pygame.mouse.get_pos(), mouse_up)
        critical_action = criticalElement.update(pygame.mouse.get_pos(), mouse_up)

        if defense_action is not None:
            user.maxHitpoints, user.maxEnergy, user.stats = Character_Data.CharacterStats.addDefense(user.maxHitpoints, user.maxEnergy, user.stats)
            user.hitpoints = user.hitpoints + 5
            user.energy = user.energy - 0.4
            user.changeStatPoints(-1)
        if evasiveness_action is not None:
            user.maxEnergy, user.stats = Character_Data.CharacterStats.addEvasiveness(user.maxEnergy, user.stats)
            user.energy = user.energy - 0.4
            user.changeStatPoints(-1)
        if intelligence_action is not None:
            user.maxEnergy, user.expPoints, user.stats = Character_Data.CharacterStats.addIntelligence(user.maxEnergy, user.expPoints, user.stats)
            user.energy = user.energy + 0.4
            user.changeStatPoints(-1)
        if attack_action is not None:
            user.maxEnergy, user.stats = Character_Data.CharacterStats.addAttack(user.maxEnergy, user.stats)
            user.energy = user.energy - 0.4
            user.changeStatPoints(-1)
        if power_action is not None:
            user.maxEnergy, user.stats = Character_Data.CharacterStats.addPower(user.maxEnergy, user.stats)
            user.energy = user.energy + 0.4
            user.changeStatPoints(-1)
        if critical_action is not None:
            user.maxEnergy, user.stats = Character_Data.CharacterStats.addCritical(user.maxEnergy, user.stats)
            user.energy = user.energy + 0.2
            user.changeStatPoints(-1)

        screen.fill(BLACK)

        UIElement.writeText("[Reduces damage taken.]", fontsize/3, WHITE, (width*2/6,(height*2/8 - fontsize/4)), screen)
        UIElement.writeText("[Bonus: Slight boost to your health and intelligence.]", fontsize/3, WHITE, (width*2/6, (height*2/8) + fontsize/4), screen)
        UIElement.writeText("[Higher chance of receiving no damage.]", fontsize/3, WHITE, (width*2/6, (height*3/8)-fontsize/4), screen)
        UIElement.writeText("[Bonus: Slight boost to your defense.]", fontsize/3, WHITE, (width*2/6, (height*3/8)+fontsize/4), screen)
        UIElement.writeText("[Increase the amount of EXP received.]", fontsize/3, WHITE, (width*2/6, (height*4/ 8)-fontsize/4), screen)
        UIElement.writeText("[Bonus: Slight boost to your energy and critical.]", fontsize/3, WHITE, (width*2/6, (height*4/ 8)+fontsize/4), screen)
        UIElement.writeText("[Increase damage sent.]", fontsize/3, WHITE, (width*2/6, (height*5/ 8)-fontsize/4), screen)
        UIElement.writeText("[Bonus: Slight boost to your power and critical.]", fontsize/3, WHITE, (width*2/6, (height*5/ 8)+fontsize/4), screen)
        UIElement.writeText("[Increase critical and normal damage.]", fontsize/3, WHITE, (width*2/6, (height*6/ 8) - fontsize/4), screen)
        UIElement.writeText("[Bonus: Slight boost to your energy and attack.]", fontsize/3, WHITE, (width*2/6, (height*6/ 8) + fontsize/4), screen)
        UIElement.writeText("[Higher chance of dealing critical damage.]", fontsize/3, WHITE, (width*2/6, (height*7/ 8)-fontsize/4), screen)
        UIElement.writeText("[Bonus: Slight boost to your attack and power.]", fontsize/3, WHITE, (width*2/6, (height*7/ 8)+fontsize/4), screen)

        allElements = [defenseElement, evasivenessElement, intelligenceElement, attackElement, powerElement, criticalElement, textElement]
        for i in range(len(allElements)):
            allElements[i].draw(screen)
        pygame.display.flip()
