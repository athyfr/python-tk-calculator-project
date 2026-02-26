VALIDATE: bool = True

class Matrix:
    data: list[list[float]]  # outer list is columns.
    dimensions: tuple[int, int]  # caches dimensions.

    def __init__(self, data: list[list[float]]):

        # ---- Validate
        if VALIDATE:
            # - 1. Type and size check

            # Make sure data is a list (supports duck-typing)
            try:
                data = list(data)
            except ValueError:
                raise ValueError(
                    "Initializer data is not castable to list"
                )

            # Check dimensions
            self.dimensions = (len(data), len(data[0]))

            # Can be either augmented matrix, or regular (uniform) matrix
            if self.dimensions[0] != self.dimensions[1] and \
                self.dimensions[0] - 1 != self.dimensions[1]:
                raise ValueError(
                    "Matrix must be a uniform size (may be augmented)"
                )

            # Loop through columns
            for col in range(self.dimensions[0]):
                # Make sure columns is list
                try:
                    data[col] = list(data[col])
                except ValueError:
                    raise ValueError(
                        "Matrix column", col, "is not castable to list"
                    )

                # Make sure column is correct size
                if len(data[col]) != self.dimensions[1]:
                    raise ValueError(
                        "Matrix has inconsistent column size"
                    )

                for cell in range(self.dimensions[1]):
                    # Make sure cell is correct type
                    try:
                        data[col][cell] = float(data[col][cell])
                    except ValueError:
                        raise ValueError(
                            "Matrix cell is not castable to float"
                        )

        # --- Load

        self.data = data

    def add_row(self, row_a: int, row_b: int, factor: float) -> None
        """Adds row ``row_b`` * ``factor`` to row ``row_a`` (replacing row ``row_a``) in the Matrix

        Performs Elementary Row Operation 1 on row ``row_a``, adding row ``row_b`` with a factor of ``factor``.

        The math expression this represents is as follows:
        .. math::
            $$\verb|factor| \cdot R_{\verb|row_b|} + R_{\verb|row_a|} \rightarrow R_{\verb|row_a|}$$

        Row arguments indicate indices.

        Args:
            row_a: The index of the row to add to, (and change).
            row_b: The index of addend row.
            factor: What to multiply row ``row_b`` by before adding to row ``row_a``.
        """

        for col in range(self.dimensions[0]):
            # Add row_b * factor to row_a
            self.data[col][row_a] += self.data[col][row_b] * factor

    def multiply_row(self, row: int, factor: float) -> None:
        """Multiplies row ``row`` by ``factor``.

        Performs Elementary Row Operation 2 on row ``row``, the nonzero scalar being ``factor``.

        ..math::
            $$\verb|factor| \cdot R_{\verb|row|} \rightarrow R_{\verb|row|}$$

        Args:

        """

        for col in range(self.dimensions[0]):
            # Multiply row by factor
            self.data[col][row] *= factor
