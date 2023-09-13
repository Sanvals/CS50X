class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError ("Wrong capacity")

        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if n > self.capacity or self.size + n > self.capacity:
            raise ValueError ("Exceed capacity")

        self._size += n

    def withdraw(self, n):
        if n < 0 or self.size < n:
            raise ValueError ("Below minimum")

        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(3)
    print(str(jar))


main()