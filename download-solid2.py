#! python3

"""download_solid2.py - Download every single XKCD comic."""

# Import essential modules.
import os
import requests
import bs4

# Set basic url and directory to save comics.
url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

# Download page.
while not url.endswith('1'):
    print('Downloading page {}'.format(url))
    result = requests.get(url)
    result.raise_for_status()

# Parse website and retrieve image element.
    result_text = bs4.BeautifulSoup(result.text)
    image_element = result_text.select('#comic img')
    if image_element == []:
        print('Could not find image file!')
    else:
        try:
            comic_url = 'http:' + image_element[0].get('src')

# Download comic.
            print('Downloading comic {}'.format(comic_url))
            result = requests.get(comic_url)
            result.raise_for_status()
        except requests.exceptions.MissingSchema:
            prev_link = result_text.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_link.get('href')
            continue

# Save it to hard drive.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in result.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

# Set next url to download comic.
    prev_link = result_text.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('All comics downloaded!')
