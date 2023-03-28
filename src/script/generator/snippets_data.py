def translate_tab(func):
    def wrapper(key, string):
        return func(key, string.replace("  ", "\t"))
    return wrapper

#? ================================================ ?#

condition_snippets = {
    "forge": """"forge:conditions": [
  {
    "type": "forge:mod_loaded",
    "modid": "create"
  },
  {
    "type": "forge:mod_loaded",
    "modid": "${modid}"
  }
],""",
    "fabric": """"fabric:load_conditions": [
  {
    "condition": "fabric:all_mods_loaded",
    "values": [
      "create",
      "${modid}"
    ]
  }
],"""
}

@translate_tab
def gen_condition_snippet(loader: str, string: str) -> dict:
    return {
        loader.title(): {
            "scope": "json",
            "prefix": f"{loader} condition",
            "body": string.splitlines(),
            "description": f"{loader} loader's data condition"
        }
    }

#? ================================================ ?#

create_recipe_snippets = {
    "base": """{
  "type": "create:${recipe_id}",
  "ingredients": [],
  "results": []
}""",
    "mechanical crafting": """{
  "type": "create:mechanical_crafting",
  "pattern": [],
  "key": {},
  "result": {
    "item": ""
  },
  "acceptMirrored": true
}""",
    "recipe sequence": """{
  "type": "create:sequenced_assembly",
  "ingredients": [],
  "transitionalItem": {
    "item": ""
  },
  "sequence": [],
  "results": []
}"""
}

@translate_tab
def gen_recipe_snippet(key: str, string: str) -> dict:
    return {
        key.title(): {
            "scope": "json",
            "prefix": f"{key} recipe",
            "body": string.splitlines(),
            "description": f"{key}'s recipes"
        }
    }