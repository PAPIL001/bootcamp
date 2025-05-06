# Markdown Cheatsheet for READMEs

This guide will walk you through the basics of Markdown, so you can easily write a great README file for your projects.

## Headings

Headings help organize your content and make it easier to read. There are six levels of headings in Markdown, indicated by the number of `#` symbols at the beginning of the line.
# This is an H1
## This is an H2
### This is an H3
#### This is an H4
##### This is an H5
###### This is an H6

## Text Formatting

You can emphasize text in a few ways:

  * **Bold:** Use two asterisks or underscores around the text.

    ```
    **This text will be bold**
    __This text will also be bold__
    ```

    Result: **This text will be bold**, **This text will also be bold**

  * *Italics:* Use one asterisk or underscore around the text.

    ```
    *This text will be italic*
    _This text will also be italic_
    ```

    Result: *This text will be italic*, *This text will also be italic*

  * ~~Strikethrough:~~ Use two tilde symbols around the text.

    ```
    ~~This text will be strikethrough~~
    ```

    Result: ~~This text will be strikethrough~~

## Lists

Markdown supports ordered (numbered) and unordered (bulleted) lists.

### Unordered Lists

Use asterisks (`*`), plus signs (`+`), or hyphens (`-`) followed by a space for each list item.

* Item 1
* Item 2
    * Sub-item 1
    * Sub-item 2
+ Another item
- Yet another item
Result:

* Item 1
* Item 2
    * Sub-item 1
    * Sub-item 2
* Another item
* Yet another item

### Ordered Lists

Use numbers followed by a period and a space for each list item.
1. First item
2. Second item
3. Third item
    1. Sub-item A
    2. Sub-item B
Result:

1. First item
2. Second item
3. Third item
    1. Sub-item A
    2. Sub-item B
## Links

You can create inline links or use reference-style links.

### Inline Links

The link text is enclosed in square brackets `[]`, and the URL is enclosed in parentheses `()`. You can optionally add a title attribute in double quotes after the URL.
[Visit Google](https://www.google.com "Google's Homepage")
Result: [Visit Google](https://www.google.com "Google's Homepage")

### Reference-style Links

Reference-style links make your Markdown more readable, especially for long URLs. You define the link in the text using a label in square brackets, and then you define the link itself elsewhere in the document.
[Google][google_link]

[google_link]: [https://www.google.com](https://www.google.com) "Google's Homepage"
Result: [Google][google_link]
## Images

You can embed images using a syntax similar to links, with an exclamation mark `!` at the beginning.
![Alt text for the image](path/to/your/image.jpg "Optional title")
For example (this will only work if you have an internet connection):
![A cute cat](https://placekitten.com/200/300 "A picture of a kitten")
Result:

## Code Blocks

You can display code inline or in a separate block.

### Inline Code

Use backticks \` around the code.
The `print()` function in Python displays output.
Result: The `print()` function in Python displays output.

### Fenced Code Blocks

For larger blocks of code, use triple backticks \`\`\` before and after the code. You can optionally specify the programming language for syntax highlighting.
\`\`\`python
def greet(name):
    print(f"Hello, {name}!")

greet("World")
\`\`\`
Result:

```python
def greet(name):
    print(f"Hello, {name}!")

greet("World")

## Tables

You can create tables using hyphens `-` and pipes `|`. Hyphens are used to create the header separator.

## Tables

You can create tables using hyphens `-` and pipes `|`. Hyphens are used to create the header separator.

| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

Result:

| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |
| Cell 3   | Cell 4   |

You can also align text within columns by adding colons `:` to the header separator:

  * `:--`: Left-align
  * `--:`: Right-align
  * `:-:`: Center-align

| Left   | Center | Right |
| :----- | :----: | ----: |
| Left   | Center | Right |
| Left   | Center | Right |

Result:

| Left   | Center | Right |
| :----- | :----: | ----: |
| Left   | Center | Right |
| Left   | Center | Right |

## Horizontal Rules

You can create a horizontal rule (a thematic break) using three or more asterisks (`***`), hyphens (`---`), or underscores (`___`) on a line by themselves.
***
---
___

All three will produce the same result:

---

---
