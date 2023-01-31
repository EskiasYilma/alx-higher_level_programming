#!/usr/bin/python3
"""
This is the text_indentation module

Returns print text "text" with the exception of the \
characters .", "?", ":" after which if encountered, will print two new lines.
"""


def text_indentation(text):
    """
    Function to print text "text" with the exception of the \
    characters .", "?", ":" after which if encountered, \
    will print two new lines.
    Checks:
        - if text is of type string and text exists
        - if text contains the characters ".", "?", ":"
    """
    if not isinstance(text, str) or (len(text) < 0):
        raise TypeError("text must be a string")
    new_txt = ""
    for i in text:
        if i in [".", "?", ":"]:
            new_txt += i + "\n\n"
        else:
            new_txt += i
    print("\n".join([line.strip() for line in new_txt.split("\n")]), end="")
