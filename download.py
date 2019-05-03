#! python3

"""download.py - Downloads every single XKCD comic."""

import requests
import os
import bs4

url = 'http://xkcd.com' # starting url
os makedirs('xkcd', exists_ok=True) # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page {}'.format(url))
    result = requests.get(url)
    result.raise_for_status()

    # TODO: Find the URL of the comic image.
    result_text = bs4.BeautifulSoup(result.text)
    image_element = result_text.select('#comic img')
    if image_element == []:
        print('Could not find comic image.')
    else:
        try:
            comic_url = 'http:' + image_element[0].get('src')

    # TODO: Download the image.
            print('Downloading image {}'.format(comic_url))
            result = requests.get(comic_url)
            result.raise_for_status()
        except requests.exceptions.MissingSchema:
            # Skip this comic.
            prev_link = result_text.select('a[rel="prev"]')[0]
            url = 'http://xkcd.com' + prev_link.get('href')
            continue


    # TODO: Save the image to ./xkcd.
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        for chunk in result.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # TODO: Get the Prev button's url.
    prev_link = result_text.select('s[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done.')


# TODO: Change project status - github
