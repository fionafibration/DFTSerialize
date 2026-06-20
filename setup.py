import setuptools

with open("readme.md", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="dftserialize",
    version="0.2.0",
    author="Finian Blackett",
    author_email="spamsuckersunited@gmail.com",
    description="A next-gen Python object serialization suite using the Discrete Fourier Transform",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ThePlasmaRailgun/DFTSerialize",
    packages=setuptools.find_packages(exclude=['examples']),
    classifiers=(
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'numpy',
    ],
)
