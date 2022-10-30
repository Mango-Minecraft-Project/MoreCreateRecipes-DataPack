import json

base = lambda color: {
  "fabric:load_conditions": [
    {
      "condition": "fabric:all_mods_loaded",
      "values": [
        "create",
        "ae2"
      ]
    }
  ],
  "type": "create:",
  "ingredients": [
    {
      "item": f"ae2:{color}_lumen_paint_ball",
      "count": 1
    }
  ],
  "results": [
    {
      "item": f"ae2:{color}_paint_ball",
      "count": 1,
      "return_chance": 1.0
    }
  ]
}

for color in 'white orange magenta light_blue yellow lime pink gray light_gray cyan purple blue brown green red black'.split():
  with open(f'{color}_lumen_paint_ball.json', 'w') as file:
    json.dump(base(color), file, indent=2)