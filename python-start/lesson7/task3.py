class Cell:
    def __init__(self, cell_number: int = 1):
        self.data = cell_number
        self.info = "*"*cell_number

    def __add__(self, other):
        return Cell(cell_number=self.data + other.data)

    def __sub__(self, other):
        if self.data > other.data:
            return Cell(cell_number=self.data - other.data)
        else:
            print("Cell number of origin cell is less than new")
            return self

    def __mul__(self, other):
        return Cell(cell_number=self.data * other.data)

    def __truediv__(self, other):
        return Cell(cell_number=self.data // other.data)

    def __str__(self):
        return self.info

    def make_order(self, row_count):
        rows = self.data // row_count
        less = self.data - rows * row_count
        result = ""
        for _ in range(rows):
            result += "*"*row_count + "\n"
        result += "*"*less
        self.info = result


if __name__ == "__main__":
    cell = Cell(cell_number=3)
    cell_2 = Cell(cell_number=4)
    cell_3 = cell + cell_2
    cell_3.make_order(row_count=3)
    print(cell_3, "\n")
    cell_4 = cell_3 - cell_2
    cell_4.make_order(row_count=4)
    cell_5 = cell_3 * cell
    cell_5.make_order(row_count=5)
    cell_6 = cell_5 / cell
    cell_6.make_order(row_count=3)
    print(cell_4, "\n")
    print(cell_5, "\n")
    print(cell_6, "\n")

