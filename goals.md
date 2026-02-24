# Goals

This file describes educational goals that need to be met; what have I been
assigned to do?

## Goals Met

- Grade 12 CS C: Recursive Algorithms
    - factorials - implemented `factorial(n: int) -> int` in `main.py`.

## Solve Linear Systems

Implement an algorithm for solving linear systems.

Use matrices to solve them, and see section 1.2 of the textbook for how to do
that.

They can be represented as a matrix, for example:

$x + y + z = 1$
$2x + 6y - z = -4$
$4x - 5y + 2z = 0$

could be represented as:

$$\left[ \begin{matrix} 1 & 1 & 1 \\ 2 & 6 & -1 \\ 4 & -5 & 2 \end{matrix} \; \right| \left. \begin{matrix} 1 \\ -4 \\ 0 \end{matrix} \right]$$

Gaussian elimination should then be used to solve this, which is
shown in [a Drawy notes file.](drawy/gaussian-elimination.drawy.json)

## Understand Memory State Diagrams

One relevant library I found (my own research) is the [`memory-graph`](https://pypi.org/project/memory-graph/) pip
package.
