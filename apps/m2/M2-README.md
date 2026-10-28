# Milestone-2

## Part 2: BeautifulSoup API Source Code Locations

I reviewed the BeautifulSoup APIs used in Milestone 1 (Tasks 1–8) and Milestone 2 Part 1 (Tasks 2–4).

The following table lists the APIs and attributes used in my programs and their locations in the BeautifulSoup source code.

| API / Attribute | Source File | Line Number | Used In |
|---|---|---|---|
| `BeautifulSoup()` | `bs4/__init__.py` | 209 | M1 Tasks 1–8; M2 Tasks 2–4 |
| `SoupStrainer()` | `bs4/filter.py` | 345 | M2 Tasks 2–4 |
| `find_all()` | `bs4/element.py` | 2715 | M1 Tasks 2, 3, 4, 6, 7; M2 Tasks 2–4 |
| `find()` | `bs4/element.py` | 2684 | M1 Task 5 |
| `find_parent()` | `bs4/element.py` | 992 | M1 Task 5 |
| `prettify()` | `bs4/element.py` | 2601 | M1 Tasks 1, 6, 7 |
| `get_text()` | `bs4/element.py` | 524 | M1 Task 8 |
| `Tag.name` | `bs4/element.py` | 1648 | M1 Tasks 3, 6; M2 Task 3 |
| `Tag.__setitem__()` | `bs4/element.py` | 2223 | M1 Task 7 |

### Additional Notes

- `BeautifulSoup()` creates a parse tree from HTML or XML.
- `SoupStrainer()` defines which parts of a document should be parsed.
- `find_all()` searches for all matching elements, while `find()` returns the first matching element.
- `find_parent()` searches for a matching parent element.
- `prettify()` formats the parse tree for readable output.
- `get_text()` extracts text from the parse tree.
- `Tag.name` is an attribute rather than a method.
- `Tag.__setitem__()` supports assigning tag attributes using syntax such as `p["class"] = "test"`.
- The `parse_only` argument is part of the `BeautifulSoup` constructor, not a separate API function.

All line numbers in the table refer to the original BeautifulSoup source code before my Part 3 modifications.

## Part 3: SoupReplacer Implementation

I added a new API called `SoupReplacer` to BeautifulSoup.

### Implementation

- Added the `SoupReplacer` class in `bs4/filter.py`. It stores the original tag name and the replacement tag name.
- Modified `BeautifulSoup.__init__()` in `bs4/__init__.py` to accept an optional `replacer` argument.
- Modified `handle_starttag()` to replace matching tag names during parsing, before creating the Tag objects.
- Modified `_popToTag()` to handle closing tags using their original names.

### Application

I created `apps/m2/task6.py` to replace `<b>` tags with `<blockquote>` tags using the new API, instead of modifying the parse tree after parsing.

### Tests

I added two tests in `bs4/tests/soupreplacer.py`:

1. `test_replace_multiple_tags`: checks whether multiple matching tags are replaced.
2. `test_replace_nested_tags`: checks whether nested elements and parent-child relationships are preserved.

Both new tests passed using pytest (`2 passed`).