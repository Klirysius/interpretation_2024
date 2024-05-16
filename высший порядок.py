import operator


def f1(n):
    return n/(2*n+1)**3


def f2(a, b, s):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '^': operator.xor,
    }
    return ops[s](a, b)


def fun(b, a, o, fun1, fun2):
    if a == b:
        return fun1(a)
    else:
        return fun2(fun1(a), fun(b, a-1, o, fun1, fun2), o)


print(fun(1, 3, "+", f1, f2))
