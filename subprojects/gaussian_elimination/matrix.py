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

    def add_row(row_a: int, row_b: int, factor: float)
