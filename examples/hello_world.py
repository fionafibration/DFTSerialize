from decimal import Decimal as d
from math import frexp as p, ldexp as q, modf as t


def w(h):
    return (h > 0) - (h < 0) or 1


def f(p):
    if p < 1:
        return 1
    else:
        return p * f(p - 1)


def u(s):
    z = d(0)
    for k in range(s):
        z += (d(-1) ** k) * (
                d(f(6 * k)) / ((f(k) ** 3) * (f(3 * k))) * (13591409 + 545140134 * k) / (640320 ** (3 * k)))
    return float((z * d(10005 ** 0.5) / 4270934400) ** (-1))


g = u(5)


def e(s):
    j = 2
    for i in range(2, s):
        j += 1 / f(i)

    return j


b = e(50)


def r(h):
    if h > 1 or h < -1:
        return -r(1 / h) + w(h) * g / 2
    elif h == 1 or h == -1:
        return g / 4

    j = 0
    for z in range(80):
        j += (-1) ** z * (h ** (2 * z + 1)) / (2 * z + 1)
    return j


a = [r(2 ** (-i)) for i in range(30)]


def s(n):
    if n < -g / 2 or n > g / 2:
        if n < 0:
            x, y = s(n + g)
        else:
            x, y = s(n - g)
        return -x, -y

    x, y = 1, 0

    for i in range(0, 30):
        d = 1.0 * w(n)

        u, v = x, y

        x = u - (d * (2 ** (-i)) * v)
        y = (d * (2 ** (-i)) * u) + v

        n = n - (d * a[i])

    return 0.6072529350088814 * x, 0.6072529350088814 * y


def h(a, b):
    u, v = p(a)
    x, y = p(b)

    h, j = u * x, int(v + y)

    return q(h, j)


def j(e, h):
    if e < 10 or h < 10:
        return e * h

    y = max(e.bit_length(), h.bit_length()) // 2

    a = e // 2 ** y
    b = e % 2 ** y
    c = h // 2 ** y
    d = h % 2 ** y

    u = j(a, c)

    v = j(b, d)

    z = j(a + b, c + d) - u - v

    return u * 2 ** (y * 2) + (z * 2 ** y) + v


def m(a, b):
    x, y = t(a)
    u, v = t(b)

    return h(x, u) + h(y, u) + h(x, v) + j(int(y), int(v))


def o(h, e):
    x, y = h
    u, v = e

    return m(x, u) - m(y, v), m(x, v) + m(y, u)


def k(p):
    q = b ** p[0]
    h, z = s(p[1])

    return h * q, z * q


def dark_magic():
    return [print(chr(int(round(sum(x[0] for x in [o((c[a], c[a + 1]), k(o([0, 2], [g * a * n / len(c), 0])))
                                                   for a in range(0, len(c), 2)]) / (len(c) / 2)))), end="") for n in range(l)]


c, l = [1129.0,
        0.0,
        23.49715586796887,
        22.211581739879684,
        -179.7230388530905,
        -157.5036698239512,
        7.806224011347112,
        20.798766949019274,
        4.275687275221713,
        -116.59625874580514,
        -3.9410319705666126,
        -17.579175939686984,
        51.58500366911933,
        -6.977531208354918,
        51.58500366911933,
        6.977531208354918,
        -3.9410319705666126,
        17.579175939686984,
        4.275687275221713,
        116.59625874580514,
        7.806224011347112,
        -20.798766949019274,
        -179.7230388530905,
        157.5036698239512,
        23.49715586796887,
        -22.211581739879684], 13

dark_magic()
