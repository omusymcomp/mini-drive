import pygame
from pygame.locals import *

# pygameを初期化
pygame.init()

# Xboxコントローラを初期化
joystick = pygame.joystick.Joystick(0)
joystick.init()

# AボタンとBボタンの状態を追跡する変数
a_button_down = False
b_button_down = False

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # AボタンとBボタンの状態をチェック
        if event.type == JOYBUTTONDOWN:
            if joystick.get_button(0):  # Aボタンはボタン0
                print('a pushed')
                a_button_down = True
            if joystick.get_button(1):  # Bボタンはボタン1
                print('b pushed')
                b_button_down = True

        if event.type == JOYBUTTONUP:
            if a_button_down and not joystick.get_button(0):  # Aボタンが離された
                print('a released')
                a_button_down = False
            if b_button_down and not joystick.get_button(1):  # Bボタンが離された
                print('b released')
                b_button_down = False
