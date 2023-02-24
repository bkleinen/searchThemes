import tomllib

tags = sys.argv

tags_themes_file = 'theme_tags.toml'

def find_tags(tags):
    tags_themes = read_list()
    print(tags_themes)


def read_list(file=tags_themes_file):
    with open(file, "r+b") as f:
        tags_themes = tomllib.load(f)
        return tags_themes

find_tags(tags)