# PynonyMous

PynonyMous is a simple Python library that provides public proxies and generates random headers for use in networking applications. It is designed to make tasks involving proxies easier, faster, and more secure.

## Installation

You can install PynonyMous using pip:

```bash
pip install pynonymous

## Usage 1

## Simply It lets a proxy from our library as a variable which makes work easier and secure.

from PynonyMous import PynonyMous

proxy = PynonyMous.varprox()


## Usage 2 

## It creates a 90-100 charcaters random string that can be used for User-Agent logging.

from PynonyMous import PynonyMous

header = PynonyMous.JunkHeader()
