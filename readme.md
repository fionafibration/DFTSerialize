# DFTSerialize™
![PyPi](https://img.shields.io/pypi/v/dftserialize.svg?color=%2300dd00&style=popout) ![Python Version](https://img.shields.io/pypi/pyversions/django.svg?style=popout) ![Rating](https://img.shields.io/badge/rating-5.0%2F5.0-%2300dd00.svg) ![License](https://img.shields.io/pypi/l/dftserialize.svg?style=popout)

![DFTSerialize™ Logo](/images/banner.png)

DFTSerialize™ is a next-generation data encoding and serialization system 
designed for Python 3.0 and aboveDFTSerialize™ uses a highly-customized 
algorithm that encodes any and all (most) Python data structures as bytes, and can
 even function on RAW BYTES. 

## Features

* 🚀 Snappy and efficient encoding of most Python objects and raw binary data
* 💡 Equally efficient decoding of the output to recover original Python objects or binary data
* 📝 Uses a *BUNCH* of fancy math and has its own reimplementation of many standard library functions 
for maximum effectiveness
* 😜 Has a really cool logo

## Why

Current serialization systems are stagnant and obsolete. Underutilization of the 
advantages of floating point processing and mathematical techniques like curve-fitting
and function transforms. DFTSerialize™ aims to fix all this. 

We noticed that in quantum mechanics, which has many applications in faster computing,
there are a lot of these things called *"waveforms"*. So we did some digging and 
discovered that these were actually wavy functions, and that the parameters of 
these functions could even be used to reconstruct data! Additionally, these waveforms 
are probably easier to compute on quantum computers because of the fact that they're
both wavy and stuff.
 
Upon further research, we discovered that JPEG images already use a wavy-function based 
compression algorithm called the "discrete cosine transform", but when we looked that up 
it seemed pretty hard so we had our accountants make us another one called the "discrete 
Fourier transform." We think it's way more marketable since it has a French guy's name in 
it.

## Usage

To use DFTSerialize™, simply install it to your Python version 3.5 or higher using the PIP 
package manager, like so:

```
pip install dftserialize
```

Then, import it in your project. It contains four functions, two for serialization, two for 
deserialization, of both Python objects and binary data.

Example:

```python
from dftserialize import *

for i in range(30):
    # data = b'x\xda\xe3e@\x02K&:\xc0\x987>$\xcev\xad7w8e\xd6k\xa1ef\xe6\x10U\x91\xa0\xa4...
    data = dft_serialize_data(b"Hello, World!")
    # b"Hello, World!"
    print(dft_deserialize_data(data))
    
    # true
    assert {1: 2, 3: 4} == dft_deserialize_object(dft_serialize_object({1: 2, 3: 4}))
```

## Speed
DFTSerialize™ is extremely fast and robust! For testing, I took a 7 MB image file and 
attempted to run it directly through a raw serialization. It didn't finish since I eventually 
had to shut my computer off, but the point is that it was working. 

Reducing the data size down to a 2kb file allowed DFTSerialize™ to completely encode the file 
in just under 10 minutes, a milestone achievement.


## DFTSerialize™ Algorithm

DFTSerialize™ uses a patented<sup>[citation needed]</sup> algorithm utilizing a 
near-magical combination of the discrete Fourier transform, floating point math, 
and even on-the-fly calculation of mathematical constants like pi.

DFTSerialize™ serialization follows a simple set of steps

1. Pass raw bytes into an FFT

2. Pack DFT coefficients

3. Wait around for a second or two so it seems like we have something to do

DFTSerialize™ deserialization follows a similar set of steps, in inverse:

1. Unpack DFT coefficients

2. Perform an Inverse DFT

3. Are we done? Maybe? Anybody?

4. Wipe all drives if the user isn't satisfied by now

## Credits

The idea for the DFTSerialize™ library came in the form of an escalating series of 
Reddit posts eventually culminating in the use of an inverse DFT to decode text from 
a series of complex coefficients.

## License

 DFTSerialize™ is released under the GNU GPL v3 License. Please refer to the LICENSE file that 
 accompanies this project for more information including complete terms and conditions.
 
## Serious Note
 
 This project is a complete and utter joke and should never, ever be used for anything. 
 In fact, I *challenge* you to find an actual use for this software. Actually, I *double challenge*
 you to also push this to production right before you quit your job, and then send me the results.
