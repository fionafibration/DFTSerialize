from numpy.fft import fft
from pprint import pformat


def generate_dft_array(data: bytes, truncation):
    array = fft(list(data))

    array = [(x.real, x.imag) for x in array]

    array = [item for sublist in array for item in sublist]

    array = [round(x, truncation) for x in array]
    
    print("c, l = %s, %s" % (pformat(array), len(data)))

    return array, len(data)

truncation = int(input("Truncation:\n>>>"))

data = input("Text:\n>>>").encode('utf-8')

generate_dft_array(data, truncation)
