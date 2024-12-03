import numpy as np

class MatrixMixin:
    def __init__(self, data=None):
        self._data = data if data is not None else np.zeros((1, 1))

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @data.deleter
    def data(self):
        del self._data

class MatrixOpsMixin(MatrixMixin):
    def _create_new_instance(self, data):
        new_instance = self.__class__()

        for attr, value in self.__dict__.items():
            if attr != '_data':
                setattr(new_instance, attr, value)

        new_instance._data = data
        return new_instance

    def __add__(self, other: MatrixMixin):
        return self._create_new_instance(self._data + other._data)

    def __mul__(self, other: MatrixMixin):
        return self._create_new_instance(self._data * other._data)

    def __matmul__(self, other: MatrixMixin):
        return self._create_new_instance(self._data @ other._data)

class BetterStrMixin:
    def __str__(self):
        attrs = []
        for key, value in self.__dict__.items():
            value_str = str(value)

            if '\n' in value_str:
                indented_value = '\n      '.join(value_str.split('\n'))
                value_str = f"\n      {indented_value}"

            attrs.append(f"    {key}={value_str}")
        return f"{self.__class__.__name__}(\n" + "\n".join(attrs) + "\n)"

    def write_to_file(self, path: str):
        with open(path, "w") as f:
            f.write(str(self))
