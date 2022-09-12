# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Gtd232

import pygame
import sys

# 初始化
pygame.init()
screen = pygame.display.set_mode(({{width}}, {{height}}))
pygame.display.set_caption("{{title}}")

# 游戏循环
while True:
    for event in pygame.event.get(): # 循环遍历事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()