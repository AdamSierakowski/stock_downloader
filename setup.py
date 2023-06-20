from setuptools import setup, find_packages

setup(
    name='stock_downloader',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'yfinance',
    ],
)
