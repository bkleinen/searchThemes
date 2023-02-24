# https://github.com/adityatelange/hugo-PaperMod/master/theme.toml

# https://docs.python.org/3/howto/urllib2.html
import urllib.request
themesfile = "themes.txt"
themesfile = "themes_short.txt"

def read_toml(toml_url):
    with urllib.request.urlopen(toml_url) as response:
        toml_str = response.read()
        print(toml_str)

with open(themesfile, "r+") as themes:
    # Reading from a file
    # print(themes.read())
    for theme in themes.readlines():
        theme = theme.rstrip()


        repo = theme.replace("github.com/","")
        toml_url = f'https://raw.githubusercontent.com/{repo}/main/theme.toml'
        print('------------------')
        print(theme)
        print('------------------')
        try:
            read_toml(toml_url)
        except urllib.error.HTTPError as e:
            # print("no main")
            # print(e)
            # print(toml_url)
            try:
                toml_url_master = toml_url.replace("main","master")
                read_toml(toml_url_master)
            except urllib.error.HTTPError as e:
                print(f'theme {theme} not found')
                # print(e)
                # print(toml_url_master)



