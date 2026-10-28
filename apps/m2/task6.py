import sys
from bs4 import BeautifulSoup, SoupReplacer

filename = sys.argv[1]
file = open(filename, "r")
content = file.read()
file.close()

if filename.endswith(".xml"):
    parser = "xml"
else:
    parser = "html.parser"

replacer = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(content, parser, replacer=replacer)

output = open("apps/m2/task6_output.html", "w")
output.write(soup.prettify())
output.close()
