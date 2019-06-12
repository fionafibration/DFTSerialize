from math import copysign, atan
from decimal import Decimal as Dec
from struct import unpack
from pickle import loads
from zlib import decompress
import numpy


# TODO: Find the original Excel workbook these math functions come from
# TODO: And sell it to "business customers"
__all__ = ['dft_deserialize_object', 'dft_deserialize_data']


# This is the one math operator all the people on
# https://www.reddit.com/r/accidentalfactorial joke about, so I used it
def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)


# Inbuilt math.pi is too long to type, so we generate our own
# Constant with this big factorial thingy.
# It works so don't touch it
def chudnovsky_pi_summation(n):
    # Thanks Chudnovsky, whoever you are!
    pi = Dec(0)
    for k in range(n):
        pi += (Dec(-1) ** k) * (Dec(factorial(6 * k)) / ((factorial(k) ** 3) * (factorial(3 * k))) * (13591409 + 545140134 * k) / (640320 ** (3 * k)))
    pi = pi * Dec(10005).sqrt() / 4270934400

    return float(pi ** (-1))


pi = chudnovsky_pi_summation(10)


# CORDICs Sin and Cos algorithm, I think it has something to do with triangles
# IDK, look on Wikipedia
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
        # sign() function workaround
        d = copysign(1.0, beta)

        u, v = x, y

        x = u - (d * (2.0 ** (-i)) * v)
        y = (d * (2.0 ** (-i)) * u) + v

        beta = beta - (d * atan(2 ** (-i)))

    # Pre-calculated K for 200 iterations
    return 0.6072529350088814 * x, 0.6072529350088814 * y


# I don't know what this one does, but I call it the "swinger function"
# Since it splits up a and b and has them intermingle
def complex_mult(a, b):
    x, y = a
    u, v = b
    return (x * u - y * v), (x * v + y * u)


# This one has a really long number in it, and it makes my head hurt.
# I'm gonna go lie down.
def complex_exponentiate(a):
    r = 2.7182818284590452353602874 ** a[0]
    x, y = cordics_algorithm(a[1])
    return x * r, y * r


# This one seems like dark magic, it uses a bunch of the
# previous ones along with some crazy loop thingies.
def inverse_discrete_fourier_transform(coefficients, length):
    # Get our list into pairs (complex numbers)
    coefficients = [coefficients[x:x + 2] for x in range(0, len(coefficients), 2)]

    # Our actual inverse DFT
    # Uses our previous functions and sums up the real results

    out = bytearray()

    for byte in range(length):
        dft_array = [complex_mult(coefficients[k],
                                   complex_exponentiate(
                                   complex_mult(
                                    [0, 2],
                                    [pi * k * byte / len(coefficients), 0])
                            )
                                   )
                      for k in range(len(coefficients))]

        out.append(int(round(sum(x[0] for x in dft_array) / len(coefficients))))

    return out


# Decoder
def dft_decode_raw(data):
    data = decompress(data)

    length = unpack('<Q', data[:8])[0]

    rest = data[8:]

    datatype = numpy.dtype(float).newbyteorder('<')

    coefficients = numpy.frombuffer(rest, dtype=datatype)

    return inverse_discrete_fourier_transform(coefficients, length)


# Deserialization methods
def dft_deserialize_object(data: bytes):
    return loads(dft_decode_raw(data))


def dft_deserialize_data(data: bytes):
    return dft_decode_raw(data)

