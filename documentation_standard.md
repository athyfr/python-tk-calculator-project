# Documentation Standard

How should I document my code? I should use a standardized format for
docstrings, but which one?

Sources:
    - [Google's Python documentation standard,](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings) which depends on:
    - [reStructuredText](https://docutils.sourceforge.io/rst.html) markup, which is used by:
    - [Sphinx](https://www.sphinx-doc.org/en/master/usage/domains/python.html) documentation generator (similar to Doxygen).

Will follow Google's standard, except excluding typing as Python's type hints
are already enough.
