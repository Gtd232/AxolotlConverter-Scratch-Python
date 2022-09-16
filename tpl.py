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

pics = {}

class Sprite:
    def __init__(self, name, x, y, layerOrder, currentCostume, costumes):
        self.name = name
        self.x = x
        self.y = y
        self.layerOrder = layerOrder
        self.currentCostume = currentCostume
        self.costumes = costumes
        j = 0
        for i in costumes:
            pics['{}-{}'.format(name, str(j))] = pygame.image.load(i['md5ext'])
            j += 1
    

class Stage:
    def __init__(self, bg):
        self.bg = bg

spriteDic = {}

{{main_program1}}

# 游戏循环
while True:
    for event in pygame.event.get(): # 循环遍历事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    for i in range(len(spriteDic) + 1):
        for j in spriteDic:
            if spriteDic[j].layerOrder == i:
                screen.blit(pics['{}-{}'.format(spriteDic[j].name, spriteDic[j].currentCostume)], (0,0))
    pygame.display.update()