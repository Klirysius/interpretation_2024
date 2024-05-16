import math


def nas(h_func, k_func):
    def pump(h, k):
        return h_func(h)*0.5*math.exp(k_func(k))
    return pump


def nas_hr(a):
    return a*12.5


def nas_hc(a):
    return a*10.32


def nas_kr(a):
    return math.exp(a)


def nas_kc(a):
    return math.exp(1.2*a)


# Создаём функцию, но не вызываем расчёт
pump_r_func = nas(nas_hr, nas_kr)
pump_c_func = nas(nas_hc, nas_kc)

h_arg, k_arg = 5, 1.23
print("Рассчитанный параметр Р для r: ", pump_r_func(h_arg, k_arg))
print("Рассчитанный параметр Р для c: ", pump_c_func(h_arg, k_arg))