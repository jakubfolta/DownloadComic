#! python3

"""download-solid.py - Download every single XKCD comic."""

# Import essential modules.
import os
import requests
import bs4
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s, %(message)s')
#logging.disable(logging.CRITICAL)

# Set basic url and create directory to save comics.
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

# Download webpage.
while not url.endswith('1'):
    print('Downloading page: {}'.format(url))
    result = requests.get(url)
    result.raise_for_status()

# TODO: Parse website and retrieve image url element.
    result_text = bs4.BeautifulSoup(result.text)
    image_element = result_text.select('#comic img')
    if image_element == []:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + image_element

# TODO: Download comic.
# TODO: Save it to a file.
# TODO: Change url to previous page.
