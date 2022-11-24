class GenerateInts:
    def __init__(self, n):  # конструктор принимает верхнюю границу диапазона
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.n:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


iterator1 = GenerateInts(5)           # создаем итератор, содержащий числа 0 1 2 3 4

print(type(iterator1))

print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))
print(next(iterator1))

iterator2 = GenerateInts(3)           # создаем итератор, содержащий числа 0 1 2

for num in iterator2:
    print(num)

num1, num2 = GenerateInts(2)          # создаем итератор, содержащий числа 0 1

print(num1, num2)