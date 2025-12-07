def test_gen(start, stop):
    n = start
    while n != stop - 1:
        yield n
        n -= 1

print(list(test_gen(10, 5)))