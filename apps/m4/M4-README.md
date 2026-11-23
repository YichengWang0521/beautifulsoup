# Milestone 4 — Iterable BeautifulSoup

## Overview
This milestone makes BeautifulSoup objects iterable, allowing users to traverse all nodes in an HTML tree using a `for` loop.

## Implementation
Added `__iter__()` to the `BeautifulSoup` class in `bs4/__init__.py`.

The method returns the existing `descendants` generator, which visits nodes one at a time without collecting them into a list.

The original iteration behavior of regular Tag objects remains unchanged.

## Unit Tests
Added five unit tests in `bs4/tests/test_m4.py`:

1. Simple HTML
2. Nested HTML
3. Multiple text nodes
4. Empty HTML
5. Repeated iteration

All five tests passed.

## Application
`apps/m4/task.py` demonstrates how to iterate over a BeautifulSoup object and print each tag or text node.

## How to Run

Run the application:

`python apps/m4/task.py`

Run the tests:

`python -m pytest bs4/tests/test_m4.py -v`
