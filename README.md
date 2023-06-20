# stock_downloader Package

The stock_downloader package provides functionality to download and save stock market data using the Yahoo Finance API.

## Installation

You can install the package using pip:

pip install stock_downloader

## Usage

The package includes the following files:

- __init__.py: An empty file that marks the stock_downloader directory as a Python package.
- downloader.py: Contains functions to download and save stock market data.
- example.py: An example script demonstrating the usage of the run_iterations function.

To use the package, you can import the necessary functions from stock_downloader.downloader:

from stock_downloader.downloader import run_iterations

ticker = 'BHP.AX'
num_iterations = 10

run_iterations(ticker, num_iterations)

## Project Structure

The stock_downloader package has the following structure:

stock_downloader/
├── __init__.py
├── downloader.py
├── example.py
├── README.md
└── setup.py

## Development and Contribution

- Source Code: [GitHub Repository](https://github.com/AdamSierakowski/stock_downloader)
- Issue Tracker: [GitHub Issues](https://github.com/AdamSierakowski/stock_downloader/issues)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
