from bs4 import (BeautifulSoup, SoupReplacer)

def test_replace_multiple_tags():
    html = "<div><b>Hello</b><b>Python</b><p>World</p></div>"

    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    assert len(soup.find_all("blockquote")) == 2
    assert len(soup.find_all("b")) == 0
    assert soup.find("p").get_text() == "World"


def test_replace_nested_tags():
    html = "<div><b>Hello <i>Python</i></b><p>World</p></div>"

    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)

    blockquote = soup.find("blockquote")
    paragraph = soup.find("p")

    assert blockquote.get_text() == "Hello Python"
    assert blockquote.find("i").get_text() == "Python"
    assert paragraph.parent.name == "div"
    assert blockquote.parent == paragraph.parent
