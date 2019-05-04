#! python3

"""download-solid.py - Download every single XKCD comic."""

# Import essential modules.
import os
import requests
import bs4
import logging

logging.basicConfig(level = logging.DEBUG, format = '%(levelname)s, %(message)s')
logging.disable(logging.CRITICAL)

# Set basic url and create directory to save comics.
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

# Download webpage.
while not url.endswith('1'):
    print('Downloading page: {}'.format(url))
    result = requests.get(url)
    result.raise_for_status()

# Parse website and retrieve image url element.
    result_text = bs4.BeautifulSoup(result.text)
    image_element = result_text.select('#comic img')
    if image_element == []:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + image_element[0].get('src')

# Download comic.
            print('Downloading comic: {}'.format(os.path.basename(comic_url)))
            result = requests.get(comic_url)
            result.raise_for_status()
        except requests.exceptions.MissingSchema:
            logging.info('Not valid URL!')
            prev_element = result_text.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_element.get('href')
            continue

# Save it to ./xkcd.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in result.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

# Change url to previous page.
    prev_element = result_text.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_element.get('href')

print('Done!')
