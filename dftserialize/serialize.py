from struct import pack
from pickle import dumps
from zlib import compress
import numpy


__all__ = ['dft_serialize_object', 'dft_serialize_data']


fft_module, fft = None, None


# TODO: Optimize the import, dir() should sort so we can
# TODO: Use a binary search for the function instead
for thing in dir(numpy):
    try:
        if numpy.__dict__[thing].__name__ == 'numpy.fft':
            fft_module = numpy.__dict__[thing]


            for thing in dir(fft_module):
                try:
                    if fft_module.__dict__[thing].__name__ == 'fft':
                        fft = fft_module.__dict__[thing]
                        break

                except:
                    pass
    except:
        pass


if fft is None:
    # Damn fallbacks
    from numpy.fft import fft


# Encode our raw data using the dark magic of NumPy
def dft_encode_raw(data: bytes):
    coefficients = fft(list(data))

    coefficients = coefficients.view(numpy.dtype(float))

    coefficients = coefficients.reshape(-1)

    return compress(pack('<Q', len(data)) + coefficients.tobytes(), level=9)


def dft_serialize_object(data):
    return dft_encode_raw(dumps(data))


def dft_serialize_data(data):
    return dft_encode_raw(data)


"""
# Randomly try and find out FFT module if we forget the exact path
# Keep importing package to try again

import random
for thing in dir(numpy):
    try:
        numpy.__dict__[thing]([0, 1, 2, 3])
        if random.randint(1, 1000) == 1:
            fft = numpy.__dict__[thing]
            break
    except:
        try:
            for thing2 in dir(numpy.__dict__[thing]):
                try:
                    numpy.__dict__[thing].__dict__[thing2]([0, 1, 2, 3])
                    if random.randint(1, 1000) == 1:
                        fft = numpy.__dict__[thing].__dict__[thing2]
                        break
                except:
                    pass
        except:
            pass
"""