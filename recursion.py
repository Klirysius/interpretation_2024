def fast_expt(b, n):
    def even(n):
        return n % 2 == 0

    a = 1
    if not even(n):
        a = b
        n -= 1
    while n != 1:
        b *= b
        n /= 2
    b *= a
    return b


a = -8
n = 2
print(fast_expt(a, n))
