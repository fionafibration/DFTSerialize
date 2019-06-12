try:
    from .deserialize import *
    from .serialize import *
except:
    from serialize import *
    from deserialize import *


# Who needs unit tests?
if __name__ == '__main__':
    import random, os
    for i in range(100):
        # I haven't bothered to check if floating point inaccuracies
        # Kill the decoding of large data,
        data = os.urandom(random.randint(0, 100))

        encoded = dft_serialize_data(data)

        assert data == dft_deserialize_data(encoded)

        print('Test %s good!' % i)