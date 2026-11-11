import sys
from bs4 import BeautifulSoup, SoupReplacer


def change_attrs(tag):
    attrs = dict(tag.attrs)

    if tag.name == "p":
        attrs["class"] = "test"

    return attrs


filename = sys.argv[1]

file = open(filename, "r")
content = file.read()
file.close()

replacer = SoupReplacer(
    attrs_xformer=change_attrs
)

soup = BeautifulSoup(
    content,
    "html.parser",
    replacer=replacer
)

output = open("task7_output.html", "w")
output.write(soup.prettify())
output.close()

print("Output saved to task7_output.html")
