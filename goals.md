# Goals

This file describes educational goals that need to be met; what have I been
assigned to do?

## Goals Met

- Grade 12 CS C: Recursive Algorithms
    - factorials - implemented `factorial(n: int) -> int` in `main.py`.

## Curriculum Content

Sourced from [here (Grade 12),](https://curriculum.gov.bc.ca/curriculum/mathematics/11/computer-science) and [here (Grade 11).](https://curriculum.gov.bc.ca/curriculum/mathematics/12/computer-science)

The Province of BC used an all rights reserved license, so I can't copy it here.

## Solve Linear Systems

Implement an algorithm for solving linear systems.

They can be represented as a matrix, for example:

$x + y + z - 1 = 0$
$2x + 6y - z + 4 = 0$
$4x - 5y + 2z = 0$

could be represented as:

```py
[
    [-1,  1,  1,  1],
    [ 4,  2,  6, -1],
    [ 0,  4, -5,  2]
]
```

(constant numbers on the _left_ for easier access by code)
