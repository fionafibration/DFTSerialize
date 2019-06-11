# Discrete Fourier Transform to Text

This is an example of a python program using a fairly low-level inverse DFT to reconstruct some original text.
Many functions of the program are obfuscated by using low-level implementations instead of builtins. For example, pi is used as a constant, but instead of importing it or just pasting it in, it is calculated upon runtime by via the Chudnovsky algorithm.

Running the program is surprisingly fast, and you'll probably the snippet I chose to encode.

## Variable/Function Explanations

f: Standard factorial, used in Chudnovsky algorithm

u: Chudnovsky algorithm, `s` is the number of iterations. 5 is sufficient for our purposes.

g: Calculated pi value

s: CORDICS sin and cosine implementation. Top few lines are to remap inputs to the working domain of the CORDICS algorithm

o: Complex number multiplication, using tuples

k: Exponentiation of a real base (in this case `e`) to a complex constant

dark_magic: Actual inverse discrete Fourier transform. Generates approximate floats of each character, which are then rounded and turned into ASCII chars and then printed.