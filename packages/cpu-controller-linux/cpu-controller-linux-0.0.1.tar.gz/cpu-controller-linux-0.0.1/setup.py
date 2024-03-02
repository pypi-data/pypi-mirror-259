from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Turn on/off cpu cores in Linux'
LONG_DESCRIPTION = 'A package that allows you to turn on/off cpu cores in Linux to increase battery life'

# Setting up
setup(
    name="cpu-controller-linux",
    version=VERSION,
    author="Devansh Arora",
    author_email="hsnaved.reverse@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['subprocess', 'PyQt6'],
    keywords=['python', 'linux', 'cpu', 'battery life', 'cpu cores',],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)