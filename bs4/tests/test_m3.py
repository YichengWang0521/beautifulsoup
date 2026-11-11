from bs4 import BeautifulSoup, SoupReplacer

def test_name_xformer():
    def change_name(tag):
        if tag.name == "b":
            return "blockquote"
        return tag.name

    replacer = SoupReplacer(
        name_xformer=change_name
    )

    soup = BeautifulSoup(
        "<p>Hello <b>world</b></p>",
        "html.parser",
        replacer=replacer
    )

    assert soup.find("blockquote") is not None
    assert soup.find("b") is None
    assert soup.blockquote.string == "world"

def test_name_xformer_unchanged():
    def change_name(tag):
        if tag.name == "b":
            return "blockquote"
        return tag.name

    replacer = SoupReplacer(name_xformer=change_name)

    soup = BeautifulSoup(
        "<p>Hello</p>",
        "html.parser",
        replacer=replacer
    )

    assert soup.p is not None
    assert soup.p.string == "Hello"


def test_attrs_xformer():
    def remove_class(tag):
        attrs = dict(tag.attrs)
        attrs.pop("class", None)
        return attrs

    replacer = SoupReplacer(attrs_xformer=remove_class)

    soup = BeautifulSoup(
        '<p class="intro" id="first">Hello</p>',
        "html.parser",
        replacer=replacer
    )

    assert "class" not in soup.p.attrs
    assert soup.p["id"] == "first"


def test_xformer():
    def change_tag(tag):
        if tag.name == "b":
            tag.name = "strong"
            tag["class"] = "highlight"

    replacer = SoupReplacer(xformer=change_tag)

    soup = BeautifulSoup(
        "<b>Hello</b>",
        "html.parser",
        replacer=replacer
    )

    assert soup.strong is not None
    assert soup.strong["class"] == "highlight"
    assert soup.strong.string == "Hello"


def test_combined_xformers():
    def change_name(tag):
        return "blockquote" if tag.name == "b" else tag.name

    def remove_class(tag):
        attrs = dict(tag.attrs)
        attrs.pop("class", None)
        return attrs

    replacer = SoupReplacer(
        name_xformer=change_name,
        attrs_xformer=remove_class
    )

    soup = BeautifulSoup(
        '<b class="old" id="one">Hello</b>',
        "html.parser",
        replacer=replacer
    )

    assert soup.blockquote is not None
    assert "class" not in soup.blockquote.attrs
    assert soup.blockquote["id"] == "one"


def test_nested_tags():
    def change_name(tag):
        return "blockquote" if tag.name == "b" else tag.name

    replacer = SoupReplacer(name_xformer=change_name)

    soup = BeautifulSoup(
        "<div><b>Hello</b><p>World</p></div>",
        "html.parser",
        replacer=replacer
    )

    assert soup.div is not None
    assert soup.blockquote.parent == soup.div
    assert soup.p.parent == soup.div
    assert soup.blockquote.string == "Hello"
    assert soup.p.string == "World"
