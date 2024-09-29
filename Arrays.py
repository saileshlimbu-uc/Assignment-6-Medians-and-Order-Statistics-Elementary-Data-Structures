class Array:
    def __init__(self, size):
        self.arr = [None] * size
        self.size = size

    def insert(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.arr[index] = value

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.arr[index] = None

    def access(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.arr[index]
