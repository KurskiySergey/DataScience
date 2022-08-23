from random import uniform


class Matrix:
    def __init__(self, size: tuple, randomize: bool = False, dist: tuple = (0, 1), init_elem=None, diag=False):
        self.__init_elem = init_elem
        self.size = size
        self.data = self.__generate_object(randomize=randomize, dist=dist, diag=diag)

    def set_init_elem(self, elem):
        self.__init_elem = elem

    def __generate_object(self, randomize, dist, diag):
        matrix = []
        for i, dim in enumerate(self.size):
            if i < len(self.size) - 1:
                data = [[] for _ in range(dim)]
            else:
                if diag:
                    data = [0 for _ in range(dim)]
                else:
                    data = [uniform(dist[0], dist[1]) for _ in range(dim)] if randomize else [self.__init_elem for _ in range(dim)]
            matrix.insert(0, data)

        diag_count = 0
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i+1])):
                if i == 0 and diag and diag_count < len(matrix[i]):
                    matrix[i+1][j] = matrix[i].copy()
                    matrix[i+1][j][diag_count] = self.__init_elem
                    diag_count += 1
                else:
                    matrix[i+1][j] = matrix[i].copy()

        matrix = matrix.pop()
        return matrix

    def __str__(self):
        return str(self.data)

    def set_value(self, dim: [tuple, list], value):

        if len(dim) == 1:
            self.data[dim[0]] = value
        else:
            data = self.data
            for idx in dim[:-1]:
                data = data[idx]
            data[dim[-1]] = value
            self.set_value(dim=dim[:-1], value=data)

    def __update_dim(self, tmp_dim):
        back_count = 1
        if tmp_dim[-back_count] == self.size[-back_count] - 1:
            tmp_dim[-back_count] = 0
            while True:
                if back_count == len(self.size):
                    back_count = 1
                    break

                back_count += 1
                if tmp_dim[-back_count] != self.size[-back_count] - 1:
                    tmp_dim[-back_count] += 1
                else:
                    if back_count == len(self.size):
                        tmp_dim[-back_count] += 1
                        break
                    tmp_dim[-back_count] = 0
        else:
            tmp_dim[-back_count] += 1

        return tmp_dim

    def __elem_calc(self, other, func):
        tmp_dim = [0 for _ in self.size]
        matrix = Matrix(size=self.size, init_elem=0)
        while tmp_dim[0] != self.size[0]:
            tmp_data = self.data
            tmp_other = other.data
            for dim in tmp_dim:
                tmp_data = tmp_data[dim]
                tmp_other = tmp_other[dim]

            result = func(tmp_data, tmp_other)
            matrix.set_value(dim=tmp_dim, value=result)
            tmp_dim = self.__update_dim(tmp_dim=tmp_dim)

        return matrix

    def __add__(self, other):
        if other.size == self.size:
            return self.__elem_calc(other, lambda x, y: x+y)

    def __sub__(self, other):
        if other.size == self.size:
            return self.__elem_calc(other, lambda x, y: x-y)

    def __mul__(self, other):
        pass


class SquareMatrix(Matrix):
    def __init__(self, size: int, randomize=False, dist=(0, 1), diag=False, init_elem=None):
        super().__init__(size=(size, size), randomize=randomize, dist=dist, diag=diag, init_elem=init_elem)


class E(Matrix):
    def __init__(self, size):
        super(E, self).__init__(size=size, diag=True, init_elem=1)


class Zero(Matrix):
    def __init__(self, size):
        super(Zero, self).__init__(size=size, init_elem=0)


if __name__ == "__main__":
    e_1 = E(size=(2,2))
    e_2 = E(size=(2,2))
    # print(e_1, e_2)
    e_3 = e_1 + e_2
    print(e_3)
    e_4 = E(size=(2,2))
    e_4.set_value(dim=[1,0], value=3)
    e_4.set_value(dim=[1,1], value=4)
    print(e_4)
    print(e_3 + e_4)