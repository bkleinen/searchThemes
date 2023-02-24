import sys
# new in python 3.11, use other library for pyscript:
# import tomllib
import tomlkit
toml_lib = tomlkit
tags = ["minimal", "blog", "bootstrap"]
tags_themes_file = 'theme_tags.toml'


def find_tags(tags):
    tags_themes = read_list()
    theme_lists = [tags_themes[tag] for tag in tags]
    theme_sets = [set(theme_list) for theme_list in theme_lists]
    if len(theme_sets) < 2:
        return theme_sets
    else:
        head = theme_sets[0]
        tail = theme_sets[1:]
        result = head.intersection(*tail)
        return list(result)



def read_list(file=tags_themes_file):
    with open(file, "r+b") as f:
        tags_themes = toml_lib.load(f)
        return tags_themes

result = find_tags(tags)
# print(result)
for l in result:
    print(f'https://{l}')

# print(str.join(result))