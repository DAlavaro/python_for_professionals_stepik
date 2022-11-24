numbers = [-3, 6, 1, -90, 34, -25, 23, -21]

positive_numbers = map(abs, numbers)     # создаем объект итератора

for num in positive_numbers:             # обходим итератор циклом for
    print(num)

for num in positive_numbers:             # обходим пустой итератор, тело цикла выполнено не будет
    print(num)

##############################################################

positive = (1, 2, 3)
negative = map(lambda x: -x, positive)

for a, b in zip(positive, negative):
    print(a + b)