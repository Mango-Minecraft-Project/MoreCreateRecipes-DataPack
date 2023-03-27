from os import listdir, system
from os.path import (
    join as path_join,
    isdir, isfile
)
import json

with open(path_join('..', 'base', 'minecraft', 'color.json')) as file:
    colors = json.load(file)

base_json = lambda color, tag, modid, item_id: {
    "forge:conditions": [
        {
            "type": "forge:mod_loaded",
            "mod_id": "create"
        },
        {
            "type": "forge:mod_loaded",
            "mod_id": modid
        }
    ],
    "fabric:load_conditions": [
        {
        "condition": "fabric:all_mods_loaded",
        "values": [
            "create",
            modid
            ]
        }
    ],
    "type": "create:splashing",
    "ingredients": [
        {
            "tag": tag,
            "count": 1
        }
    ],
    "results": [
        {
            "item": f"{modid}:{color}_{item_id}",
            "count": 1,
            "chance": 1
        }
    ]
}