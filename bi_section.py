def bi_section(func, a, b, tol, n_max):
    def f(x):
        f = eval(func)
        return f

    n = 1
    c = (a + b) / 2
    diff = abs(b - a)
    temp_c = a

    relative_cond, abs_fc_cond, iter_cond = False, False, False

    while True:

        relative_c_change = abs(temp_c - c) / abs(c)
        temp_c = a
        c = (a + b) / 2

        if f(a) * f(b) >= 0:
            print("No root for this equation.")
            break
        elif f(c) * f(a) < 0:
            b = c
            diff = abs(b - a)
        elif f(b) * f(a) < 0:
            a = c
            diff = abs(b - a)
        else:
            print("Something wrong")

        print(f"The relative change is {relative_c_change}.")
        print(f"The error is {diff}, the iteration round#{n}.")
        print(f"The f(c) is {abs(f(c))}.")
        print(f"The lower boundary is {a} and the upper boundary is {b}.")
        print("------------------------------------------------------------")

        if n >= 2:
            # print(end='')
            if relative_c_change <= tol:
                print("Relative change is out of limit!")
                relative_cond = True

        if n_max <= n:
            print("Out of iteration limit!")
            iter_cond = True

        if abs(f(c)) <= tol:
            print("tolerance is out of limit!")
            abs_fc_cond = True

        if relative_cond or abs_fc_cond or iter_cond:
            return c

        n = n + 1

    return c


try:
    t = bi_section("(x**3)+(-6*x**2)+(11*x)+(-6)", 2.5, 4, 0.001, 1000)
    print(f"the root of a polynomial = {t}")
except NameError:
    print("An exception occurred")


def sign(a):
    if a > 0:
        return 1
    elif a < 0:
        return -1
    else:
        return 0
