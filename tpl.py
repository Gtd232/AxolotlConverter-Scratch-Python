# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Gtd232

import pygame
import sys

# 初始化
pygame.init()
screenWidth = {{width}}
screenHeight = {{height}}
screen = pygame.display.set_mode((screenWidth, screenHeight))
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
            pics['{}-{}'.format(name, str(j))] = [pygame.transform.scale(pygame.image.load(i['md5ext']), (pygame.image.load(i['md5ext']).get_rect().size[0] / 2, pygame.image.load(i['md5ext']).get_rect().size[1] / 2)), i['rotationCenterX'], i['rotationCenterY'], pygame.image.load(i['md5ext']).get_rect().size[0], pygame.image.load(i['md5ext']).get_rect().size[1]]
            # 图像 rotationCenterX rotationCenterY Width Height   
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
                screen.blit(pics['{}-{}'.format(spriteDic[j].name, spriteDic[j].currentCostume)][0], (screenWidth / 2 + spriteDic[j].x - pics['{}-{}'.format(spriteDic[j].name, spriteDic[j].currentCostume)][1] / 2, screenHeight / 2 - spriteDic[j].y - pics['{}-{}'.format(spriteDic[j].name, spriteDic[j].currentCostume)][2] / 2))
    pygame.display.update()