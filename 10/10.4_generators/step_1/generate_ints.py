def generate_ints(n):
    for num in range(n):
        yield num


generator1 = generate_ints(5)           # создаем генератор, порождающий числа 0 1 2 3 4

print(type(generator1))

print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))
print(next(generator1))

generator2 = generate_ints(3)           # создаем генератор, порождающий числа 0 1 2

for num in generator2:
    print(num)

num1, num2 = generate_ints(2)           # создаем генератор, порождающий числа 0 1

print(num1, num2)