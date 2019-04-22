import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='nancy',
    version='0.1.0',
    scripts=['nancy'],
    author='Alamin Mahamud',
    author_email='alamin.ineedahel@gmail.com',
    description='A docker and AWS utility package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/alamin-mahamud/nancy',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],    
)
