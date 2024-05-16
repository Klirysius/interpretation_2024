def fun1(n):
    return n/(2*n+1)**3


def fun2(a, b):
    return a + b


def fun(b, a):
    if a == b:
        return fun1(a)
    else:
        return fun2(fun1(a), fun(b, a-1))


print(fun(1, 3))
