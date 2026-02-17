# Python Calculator Project

## Goal

This project is made to try to fulfill this requirement:

> "I'll make a calculator project to demonstrate several recursive algorithms
> (Fibonacci, exponents, factorials, palindromes, combinations, greatest
> common factor)"

## Functions

This calculator GUI uses Python's `eval()` function, so Python expressions are
used for calculations.

Python's math library is imported using `import math`, so any functions
from that may be used. Some of these functions are reimplemented in the local
namespace, including:

- `factorial(n: int) -> int`: Calculates the factorial using a for loop, and
  returns a `ValueError` when negative numbers or integers are used.
