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
    print('Downloading page {}'.format(url))
    result = requests.get(url)
    result.raise_for_status()

# Parse downloaded webpage and retrieve image element using bs4 module.
    result_text = bs4.BeautifulSoup(result.text)
    image_element = result_text.select('#comic img')
    if image_element == []:
        print('Could not find image!')
    else:
        try:

# Create comic url, download it. If error occurs go to next comic.
            comic_url = 'http:' + image_element[0].get('src')
            print('Downloading comic ---------- {}'.format(os))
            result = requests.get(comic_url)
            result.raise_for_status()
        except requests.exceptions.MissingSchema:
            prev_link = result_text.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_link.get('href')
            continue

# Save comic to new folder.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in result.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

# Set new url with next comic and repeat.
    prev_link = result_text.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('All comics downloaded!')
