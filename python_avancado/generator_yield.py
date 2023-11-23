my_list = [1, 2, 3, 4, 5]

iter_example = iter(my_list)

# para percorrer a lista

print(next(iter_example))


def my_gen():
    n = 1
    print(f'primeiro print n = {n}')
    yield n

    n += 1
    print(f'segundo print, n = {n}')
    yield n

    n += 1
    print(f'terceiro e ultimo print, n = {n}')
    yield n


if __name__ == '__main__':
    test = my_gen()
    test.__next__()
    test.__next__()
