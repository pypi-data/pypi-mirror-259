from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='qcktypes',
    author='smugvee',
    description='Python implementation of dyne\'s file extension list',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/smugvee/qcktypes',
    version="1.1",
    packages=find_packages(),
classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License'
    ],
    python_requires='>=3.3'
)
