from setuptools import setup

setup(
    name='stock_downloader',
    version='0.2',
    py_modules=['downloader'],
    install_requires=[
        'yfinance',
    ],
)
