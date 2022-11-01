from json import load, dump
from os import listdir

for filename in listdir():
  if filename.endswith('.json'):
    with open(filename) as file:
      data = load(file)
    with open(filename, 'w') as file:
      dump(data, file, indent=2)