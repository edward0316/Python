def func(a, r):
    b = a + 1
    r = r * b
    if a >= 6:
        print(r)
        return 'end'
    return func(b, r)

func(1, 1)