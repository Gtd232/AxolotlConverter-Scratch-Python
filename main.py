# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Gtd232

import os
import zipfile
import json

def make(file_json,encoding='utf-8',screenWidth=480,screenHeight=360,title='Axolotl Application'):
    with open(r'tpl.py', 'r',encoding=encoding) as f:
        file_head = f.read()
    if os.name == 'nt':
        os.system(r'mkdir output')
        os.system(r'copy .\assets\bg.png .\output\bg.png')
    else:
        os.system(r'mkdir -p output')
        os.system(r'cp ./assets/bg.png ./output/bg.png')

    main_program1 = ''''''

    for i in file_json['targets']:
        if i['isStage'] != True:
            main_program1 += '''
            spriteDic['{}'] = Sprite('{}', {}, {}, {}, {}, {})
            '''.format(i['name'], i['name'], i['x'], i['y'], i['layerOrder'], i['currentCostume'],i['costumes']).replace('    ', '')
    
    # vars
    for i in file_json['targets']:
        if i['name'] == 'Stage':
            for j in i['variables']:
                main_program1 += '''
                pvars['{}'] = {name: {}, value: {}}
                '''.format(i['variables'][j], i['variables'][j][0], i['variables'][j][1]).replace('    ', '')


    with open(r'./output/main.py', 'w', encoding=encoding) as f:
        f.write(file_head
            .replace('{{width}}', str(screenWidth))
            .replace('{{height}}', str(screenHeight))
            .replace('{{title}}', title)
            .replace('{{main_program1}}', main_program1))

    

def unzip(filepath):
    f = zipfile.ZipFile(filepath, 'r')
    if os.name == 'nt':os.system(r'mkdir temp') 
    else:os.system(r'mkdir -p temp')
    f.extractall('temp')

if __name__ == '__main__':
    unzip('input.sb3')
    with open('./temp/project.json', 'r') as f:
        make(json.loads(f.read()))

