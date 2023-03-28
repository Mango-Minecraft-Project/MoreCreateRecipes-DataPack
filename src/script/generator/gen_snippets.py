import json

from snippets_data import *

raw = {}

for loader, string in condition_snippets.items():
    raw |= gen_condition_snippet(loader, string)
for key, string in create_recipe_snippets.items():
    raw |= gen_recipe_snippet(key, string)

with open("./.vscode/modloader-condition.code-snippets", "w") as file_ref:
    json.dump(raw, file_ref, indent="\t")