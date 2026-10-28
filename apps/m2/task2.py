import sys
from bs4 import BeautifulSoup,SoupStrainer
filename=sys.argv[1]
file=open(filename,'r')
content=file.read()
file.close()
if filename.endswith('.xml'):
    parser="xml"
else:
    parser="html.parser"

only_a_tags=SoupStrainer("a")
soup=BeautifulSoup(content,parser,parse_only=only_a_tags)
links=soup.find_all('a')
for link in links:
    print(link)
#print("Number of links:", len(links))