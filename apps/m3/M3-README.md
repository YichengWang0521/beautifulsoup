# Milestone 3 — SoupReplacer API Technical Brief

## 1. Introduction

In Milestone 2, I implemented a SoupReplacer API that allows users to replace HTML tag names during parsing. In Milestone 3, I extended this API to support user-defined transformation functions that can modify tag names and attributes.

This technical brief compares the two API designs and provides recommendations for extending BeautifulSoup.

## 2. Comparison of the APIs

### Milestone 2 API

The Milestone 2 API allows users to specify an original tag name and a replacement tag name.

`SoupReplacer("b", "blockquote")`

This design is simple and easy to use because users only need to provide two strings. It is suitable for straightforward tag replacement.

However, the API is limited to a fixed replacement pair and does not provide a flexible way to modify tag attributes.

### Milestone 3 API

The Milestone 3 API introduces three optional transformer functions:

`SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)`

The `name_xformer` function returns a new tag name, while `attrs_xformer` returns new tag attributes. The `xformer` function can directly modify a Tag object without returning a value.

Compared with Milestone 2, this API is more flexible. Users can define conditional transformation rules, modify attributes, and perform multiple transformations during parsing.

For example, in the Milestone 3 application, I used `attrs_xformer` to assign `class="test"` to all paragraph tags during parsing, instead of modifying them after parsing as I did in Milestone 1.

However, the new API also introduces additional complexity because users need to understand Python functions and BeautifulSoup Tag objects.

## 3. Recommendation

I recommend supporting both APIs instead of replacing the Milestone 2 interface entirely.

The Milestone 2 API should remain available for simple tag replacement because it is easy to understand and requires less code.

The Milestone 3 API should be provided for more advanced transformations because it offers greater flexibility and extensibility.

Supporting both interfaces would preserve backward compatibility while allowing users to choose the approach that best fits their needs.

I would also recommend clearly documenting the execution order of multiple transformer functions and ensuring that tag transformations preserve the correct structure of the HTML parse tree.

## 4. Conclusion

The Milestone 2 API emphasizes simplicity, while the Milestone 3 API provides greater flexibility.

I recommend combining both approaches to create a SoupReplacer API that is easy to use for simple tasks and powerful enough for more complex HTML transformations.