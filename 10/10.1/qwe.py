a = enumerate('beegeek')
print(type(a))
print(a)

a = [1, 2, 3, 4, 5]
print(type(a))
print(a)

a = 'beegeek'
print(type(a))
print(a)

a= range(10)
print(type(a))
print(a)

a = map(str.upper, 'beegeek')
print(type(a))
print(a)

a = (1, 2, 3, 4, 5)
print(type(a))
print(a)

a= filter(None, '11010111')
print(type(a))
print(a)

a= {'bee': 1, 'geek': 2}
print(type(a))
print(a)

a = {1, 2, 3, 4, 5}
print(type(a))
print(a)

a = zip('bee', 'geek')
print(type(a))
print(a)

for i in a:
    print(i)

numbers = (-2, -1, 0, 1, 2)

non_zero = filter(None, numbers)
positive = map(abs, non_zero)

print(*non_zero)
