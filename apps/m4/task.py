from bs4 import BeautifulSoup, Tag, NavigableString

html_doc = "<div><p>Hello</p><b>World</b></div>"

soup = BeautifulSoup(html_doc, "html.parser")

for node in soup:
    if isinstance(node, Tag):
        print("Tag:", node.name)
    elif isinstance(node, NavigableString):
        print("Text:", str(node))
