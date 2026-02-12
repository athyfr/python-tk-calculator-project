# Python Calculator Programming Journal

## Feb 4th, 2026

1. Decided to make a calculator program, as that can integrate many algorithms.

2. Went to the [recommended](https://docs.python.org/3/library/tkinter.html)
   Tkinter [tutorial](https://tkdocs.com/tutorial/intro.html) to learn how to
   make GUIs.

## Feb 5th, 2026

3. Decided to use GIMP to create sketches (plans) of GUI before implementation.

4. Using [Zed editor](https://zed.dev/) instead of Thonny, as I'm more
   familiar/comfortable using that. (I'm using
   [ty](https://github.com/astral-sh/ty) and
   [Ruff](https://github.com/astral-sh/ruff) LSPs)

5. Decided to pause the tutorial; the first example contains everything I need
   for this project.

6. Found that one grid doesn't do the job; I need a second frame to contain the
   buttons.

7. Searched online to find the Python equivalent of C/C++
   `function.bind(argument)`; it is `partial(function, argument)`,
   `from functools import partial`. (see [GeeksforGeeks article](https://www.geeksforgeeks.org/python/how-to-bind-arguments-to-given-values-in-python-functions/))

8. Skimmed TkDocs, and found that journal entry 6 was wrong; a widget can span
   multiple grid cells using `columnspan` and `rowspan`. Regardless, the design
   I came up with has other advantages; I'm now using a `ttk.Notebook` to allow
   different calculator button sets. (Basic one would be arithmetic.)

9. Tweaked my development environment; `rumdl` for Markdown formatting (this
   journal), and `harper-ls` for spell/grammar checking in Markdown and
   comments.

## Feb 9th or 10th?, 2026

10. Tweaked ruff formatter/linter to be compliant to PEP 8
    (line length 88 -> 79)

11. Decided to use Python's `eval()` to calculate expressions.

## Feb 11th, 2026

12. Reminded myself of core competencies plan; decided that iterating upon this
    calculator project for _all_ the core-competencies would be a good idea.

13. Created/iterated on documentation (Markdown) files, including:
    - `curricular-competencies.md`
    - `README.md`
