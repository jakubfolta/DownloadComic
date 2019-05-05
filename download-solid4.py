#! python3

"""download-solid4.py - Downloads every single XKCD comic."""

# Import essential modules.
import os
import requests
import bs4

# Set basic url to download and create directory to save comics.
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

# In a while loop download webpage using requests module, check for error.
while not url.endswith('#'):
    result = requests.get(url)
    result.raise_for_status()

# TODO: Parse downloaded webpage and retrieve image element using bs4 module.
# TODO: Create comic url, download it. If error occurs go to next comic.
# TODO: Save comic to new folder.
# TODO: Set new url with next comic and repeat.
