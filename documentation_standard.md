# Documentation Standard

How should I document my code? I should use a standardized format for
docstrings, but which one?

Sources:
    - [Google's Python documentation standard,](https://github.com/google/styleguide/blob/gh-pages/pyguide.md) which depends on:
    - [reStructuredText](https://docutils.sourceforge.io/rst.html) markup, which is used by:
    - [Sphinx](https://www.sphinx-doc.org/en/master/usage/domains/python.html) documentation generator (similar to Doxygen).

Will follow Google's standard.

Most interesting parts (to me):

- 2.3: I didn't know how to use subdirectories before.
- 2.4: I didn't know about `finally` blocks.
- 2.7: I didn't know about comprehensions & generator expressions before.

Reference the official Google document, not the copy below (if you're not me.)
I slimmed it down to only what's important _to me._

## Notes

### 2.2: Imports

- `from x import y` should only be used for modules, not individual functions or
  variables.
    - Except for the modules `typing` and `collections.abc`.
- `from x import y as z` may only be used if the last point is true, and any of
  the following is true:
    - Two modules named `y` are to be imported.
    - `y` conflicts with a top-level name in the current module.
    - `y` conflicts with a common parameter name in the public API.
    - `y` is an inconveniently long name.
    - `y` is too generic in the context of your code.
- Use `import y as z` only when `z` is a standard abbreviation.

### 2.3: Packages

- A package is an import that references a separate code file within the same
  project/repository.
- Packages should be imported by their full name (from the root of the Python
  project)
- To use directories, use a `.` instead of a `/`, and always remove the `.py`
  file extensions when using imports.

### 2.4: Exceptions

- Exceptions are to be used carefully, and `assert` may only be used in
  pytests.
- Never use catch-all `except:` statements, or catch `Exception` or `StandardError` unless:
    - re-raising the exception
    - creating an isolation point to make sure exceptions aren't propogated, but
      instead recorded and suppressed.
- Minimize the amount of code in `try`/`except` blocks, to ensure you're
  catching the error you intended to catch.
- Use `finally` block to execute code whether or not an exception is raised.

### 2.5: Mutable Global State

- Avoid mutable global state.
- In the rare case it's warranted, declare it in a module or class with an
  underscore prepended to its name.
    - In a comment or linked doc, explain why mutable global state is necessary.
- Module-level _constants_ are encouraged. (Named with all caps)

### 2.6: Nested/Local/Inner Classes and Functions

- Avoid nested classes, and prefix class members that are only used internally
  with an `_`.

### 2.7: Comprehensions & Generator Expressions

- Optimize for readability, not conciseness.
- Multiple `for` clauses or filter expressions not permitted.
