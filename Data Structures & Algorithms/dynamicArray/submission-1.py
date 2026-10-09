class DynamicArray:
    
    def __init__(self, capacity: int):
        self.array = [0] * capacity           # Sets the size of the array and creates the array
        self.capacity = capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.array[i]                 # Returns the array element at index i

    def set(self, i: int, n: int) -> None:
        self.array[i] = n                    # Sets the array element at index i to n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        result = self.array[self.length - 1]        # Pops the element at the end of the array
        self.length -= 1
        return result

    def resize(self) -> None:
        self.capacity *= 2               # Doubles the space of the array
        self.array = self.array[:self.length] + [0] * (self.capacity - self.length)


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity