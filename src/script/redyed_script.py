from os import listdir, system
from os.path import (
    join as path_join,
    isdir, isfile
)
import json

with open(path_join('..', 'base', 'minecraft', 'color.json')) as file:
    colors = json.load(file)

base_json = lambda color: 