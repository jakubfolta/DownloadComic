#! python3

"""download-solid3.py - Download every single XKCD comic."""

# Import essential modules.
import os
import requests
import bs4

# Set basic url to download and directory to save comics.
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

# In a while loop download webpage.
while not url.endswith('#'):
    result = requests.get(url)
    result.raise_for_status()

# TODO: Parse webpage and retrieve image elements using bs4 module.
# TODO: Set comic url to download.
# TODO: Download comic using requests module.
# TODO: Save comic to new folder.
# TODO: Set new url to download in next iteration.
