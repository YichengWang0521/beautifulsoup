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

only_id=SoupStrainer(id=True)
soup = BeautifulSoup(content, parser,parse_only=only_id)

tags = soup.find_all(id=True)
for tag in tags:
    print(tag)