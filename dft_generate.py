from math import copysign as cp, atan
from decimal import Decimal as d
from numpy.fft import fft
from pprint import pformat

text = input("What is your desired input text?\n>>>")

l = len(text)

c = fft(list(ord(c) for c in text))

c = [(x.real, x.imag) for x in c]

print("c, l = %s, %s" % (pformat(c), len(text)))

print("Testing output:")

# Factorial is used in our Chudnovsky pi generation sum
# Standard recursive definition
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


# Pi generation sum itself
# With only 5 iterations we get a very accurate value for pi
def chudnovsky_pi_summation(n):
    pi = d(0)
    for k in range(n):
        pi += (d(-1) ** k) * (d(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (13591409 + 545140134 * k) / (640320 ** (3 * k)))
    pi = pi * d(10005).sqrt() / 4270934400

    return float(pi ** (-1))


pi = chudnovsky_pi_summation(5)


# CORDICs Sin and Cos algorithm, uses existing atan function
# For conciseness and possibly increased obfuscation
def cordics_algorithm(beta):
    # Get beta into the range it should be.
    if beta < -pi / 2 or beta > pi / 2:
        if beta < 0:
            x, y = cordics_algorithm(beta + pi)
        else:
            x, y = cordics_algorithm(beta - pi)
        return -x, -y

    x, y = 1, 0

    # Run our step
    for i in range(0, 200):
        d = 1.0 * cp(1, beta)

        u, v = x, y

        x = u - (d * (2.0 ** (-i)) * v)
        y = (d * (2.0 ** (-i)) * u) + v

        beta = beta - (d * atan(2 ** (-i)))

    # Pre-calculated K for 200 iterations
    return 0.6072529350088814 * x, 0.6072529350088814 * y


# Multiply two tuple-based complex numbers, or one complex and one real
def complex_mult(a, b):
    x, y = a
    u, v = b
    return (x * u - y * v), (x * v + y * u)


# Complex exponentiation
# See https://www.math.toronto.edu/mathnet/questionCorner/complexexp.html
def complex_exponentiate(a):
    r = 2.7182818284590452353602874 ** a[0]
    x, y = cordics_algorithm(a[1])
    return x * r, y * r


# Our actual inverse DFT
# Uses our previous functions and sums up the real results
def inverse_discrete_fourier_transform(n):
    multiplied = [complex_mult(c[k],
                               complex_exponentiate(
                               complex_mult(
                                [0, 2],
                                [3.14159265358979 * k * n / len(c), 0])
                        )
                               )
                  for k in range(len(c))]

    return sum(x[0] for x in multiplied) / len(c)

print("Copy and paste c and c constants into dft_golfed to print out your full text.")
for n in range(l):
    print(chr(int(round(inverse_discrete_fourier_transform(n)))), end="")
