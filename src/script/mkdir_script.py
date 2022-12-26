from os import mkdir
from os.path import (
    join as path_join,
    isdir
)

base_path = '..', 'new', 'MoreCreateRecipes - Datapack', 'data', 'recipes', 'general'
path = path_join(*base_path)

dirs = [
    'ae2',
    'tconstruct',
    'industrialforegoing',
    'immersiveengineering',
    'mekanism',
    'mekanismadditions',
    'cookingforblockheads',
    'thermal',
    'refinedstorage',
    'botania'
]

for dir_ in dirs:
    p = path_join(path, dir_)
    if isdir(p):
        continue
    try:
        mkdir(p)
    except Exception as error:
        print(error)