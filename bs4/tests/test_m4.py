from bs4 import BeautifulSoup, Tag, NavigableString

# Test 1: Simple HTML
def test_simple_html():
    soup = BeautifulSoup("<p>Hello</p>", "html.parser")

    nodes = list(soup)

    assert len(nodes) == 2
    assert isinstance(nodes[0], Tag)
    assert nodes[0].name == "p"
    assert isinstance(nodes[1], NavigableString)
    assert str(nodes[1]) == "Hello"

# Test 2: Nested HTML
def test_nested_html():
    soup = BeautifulSoup(
        "<div><p>Hello</p><b>World</b></div>",
        "html.parser"
    )

    nodes = list(soup)

    assert [node.name if isinstance(node, Tag)
            else str(node) for node in nodes] == [
        "div", "p", "Hello", "b", "World"
    ]

# Test 3: Multiple text nodes
def test_multiple_text_nodes():
    soup = BeautifulSoup(
        "<p>Hello <b>World</b>!</p>",
        "html.parser"
    )

    nodes = list(soup)

    assert len(nodes) == 5
    assert str(nodes[1]) == "Hello "
    assert nodes[2].name == "b"
    assert str(nodes[3]) == "World"
    assert str(nodes[4]) == "!"

# Test 4: Empty HTML
def test_empty_html():
    soup = BeautifulSoup("", "html.parser")

    assert list(soup) == []

# Test 5: Repeated iteration
def test_repeated_iteration():
    soup = BeautifulSoup("<p>Hello</p>", "html.parser")

    first = [str(node) for node in soup]
    second = [str(node) for node in soup]

    assert first == second
    assert len(first) == 2
