import tomllib
import sys


tags = sys.argv[1:]

if len(tags) < 2:
    print('usage: find_tags <tags>')
    exit(2)

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
        tags_themes = tomllib.load(f)
        return tags_themes

result = find_tags(tags)
# print(result)
for l in result:
    print(f'https://{l}')

# print(str.join(result))