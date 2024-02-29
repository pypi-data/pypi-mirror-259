from setuptools import setup, find_packages

setup(
    name='jettonpriceapi',
    version='0.1.0',
    packages=find_packages(),
    install_requires=['requests'],
    url='https://github.com/labfunny/jetton-price-api',
    license='MIT',
    author='Max',
    description='A Python library for interacting with the Tonapi API',
    classifiers = ['Programming Language :: Python :: 3.6']
)