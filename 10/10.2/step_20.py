numbers = [1, 2, 3, 4, 5]
objects = [0, 1, True, False, 17, []]

def filterfalse(func, object):
    o = []
    if func is None:
        func = bool
    for i in object:
        if func(i) != True:
            o.append(i)
    return o






print(*filterfalse(lambda x: x >= 3, numbers))
print(*filterfalse(None, objects))

