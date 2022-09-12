# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Gtd232

import pygame
import sys

# 初始化
pygame.init()
screen = pygame.display.set_mode(({{width}}, {{height}}))
pygame.display.set_caption("{{title}}")

background = pygame.image.load('bg.png')

class Sprite:
    def __init__(self, name, x, y, ):
        self.name = name
        self.x = x
        self.y = y
    

class Stage:
    def __init__(self, bg):
        self.bg = bg

{{main_program1}}

# 游戏循环
while True:
    for event in pygame.event.get(): # 循环遍历事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    pygame.display.update()