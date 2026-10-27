import sys
from bs4 import BeautifulSoup,SoupStrainer
filename = sys.argv[1]
file = open(filename, "r")
content = file.read()
file.close()
if filename.endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"

all_tags = SoupStrainer(True)
soup = BeautifulSoup(content, parser, parse_only=all_tags)
tags=soup.find_all()
for tag in tags:
    print(tag.name)