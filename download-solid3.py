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
    print('Downloading page {}'.format(url))
    result = requests.get(url)
    result.raise_for_status()

# Parse webpage and retrieve image elements using bs4 module.
    result_text = bs4.BeautifulSoup(result.text)
    image_element = result_text.select('#comic img')
    if image_element == []:
        print('Could not find image file!')
    else:
        try:

# Set comic url to download.
            comic_url = 'http:' + image_element[0].get('src')

# Download comic using requests module.
            result = requests.get(comic_url)
            result.raise_for_status()
        except requests.exceptions.MissingSchema:
            prev_element = result_text.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_element.get('href')
            continue

# Save comic to new folder.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in result.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

# Set new url to download in next iteration.
    prev_element = result_text.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_element.get('href')

print('All comics downloaded!')
