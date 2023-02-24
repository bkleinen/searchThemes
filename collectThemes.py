# https://github.com/adityatelange/hugo-PaperMod/master/theme.toml

# https://docs.python.org/3/howto/urllib2.html
import urllib.request
import tomllib
from collections import defaultdict
import sys

remote = False
themesfile = "themes.txt"
themesfile = "themes_short.txt"
themes_list_url = "https://raw.githubusercontent.com/gohugoio/hugoThemesSiteBuilder/main/themes.txt"

tags= sys.argv

def find_tags(tags):
    print(tags)
    tag_urls = defaultdict(list)
    themes = load_themes_list(remote)
    for theme in themes:
        theme_toml = read_theme(theme)
        if theme_toml is not None:
            tags = theme_toml.get('tags', [])
            print(f'adding tags: {tags}')
            tag_urls[theme] = tags
    print_dict(tag_urls)
def print_dict(d):
    print('-------------------- dict --------------------')
    for k in iter(d):
        print(f'{k}: {d[k]}')
def read_toml(toml_url):
    with urllib.request.urlopen(toml_url) as response:
        toml_bytes = response.read()
        toml_str = toml_bytes.decode("utf-8")

        toml = tomllib.loads(toml_str)
        return toml



def load_themes_list(remote=False):
    str = load_themes(remote)
    print("---- str ---")
    print(str)
    list = [ l.rstrip() for l in str.split('\n')]
    return list
def load_themes(remote=False):
    if remote:
        with urllib.request.urlopen(themes_list_url) as response:
                bytes = response.read()
                return bytes.decode("utf-8")
    else:
        with open(themesfile, "r+") as themes:
            return themes.read()


#-----

def read_theme(theme):
        repo = theme.replace("github.com/","")
        toml_url = f'https://raw.githubusercontent.com/{repo}/main/theme.toml'
        print('------------------')
        print(theme)
        print('------------------')
        try:
            return read_toml(toml_url)
        except urllib.error.HTTPError as e:
            # print("no main")
            # print(e)
            # print(toml_url)
            try:
                toml_url_master = toml_url.replace("main","master")
                return read_toml(toml_url_master)
            except urllib.error.HTTPError as e:
                print(f'theme {theme} not found')
                # print(e)
                # print(toml_url_master)
                return None


find_tags(tags)
