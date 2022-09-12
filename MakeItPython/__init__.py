# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Gtd232

import os


def make(file_json,encoding='utf-8',screenWidth=480,screenHeight=360,title='Axolotl Application'):
    with open(r'MakeItPython\tpl.py', 'r',encoding=encoding) as f:
        file_head = f.read()
    os.system('mkdir output')
    with open(r'./output/main.py', 'w', encoding=encoding) as f:
        f.write(file_head
            .replace('{{width}}', str(screenWidth))
            .replace('{{height}}', str(screenHeight))
            .replace('{{title}}', title))

if __name__ == '__main__':
    make('')
