def func():
    print('function starts')
    # PAUSE
    yield

    print('end function')


try:
    y = func()
    print(type(y))
    next(y)
    next(y)

except StopIteration:
    pass

print('------------------------------------------')


def func_send():
    print('part 1')
    x = yield
    print(x)
    print('part 2')

    a = yield
    print(a)
    print('parte 3')


try:
    y = func_send()
    next(y)
    y.send(6)

    y.send(12)

except StopIteration:
    pass