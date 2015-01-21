from pyquery import PyQuery as pq
import requests
import os
from urlparse import urlparse
from itertools import chain

d = pq(filename='index.html')


def fetch_for(document, tag, attribute):
    for element in document('{}[{}]'.format(tag, attribute)):
        url_string = pq(element).attr[attribute]
        url = urlparse(url_string)
        if url.scheme:
            target_path = '{}{}'.format(url.netloc, url.path)
            if not os.path.exists(target_path):
                if not os.path.exists(os.path.dirname(target_path)):
                    os.makedirs(os.path.dirname(target_path))
                response = requests.get(url_string)
                with open(target_path, 'w+') as f:
                    f.write(response.content)

            yield (url_string, './' + target_path)

urls = chain(
    fetch_for(d, 'link', 'href'),
    fetch_for(d, 'img', 'src'),
    fetch_for(d, 'script', 'src'),
)

with open('index.html') as f:
    data = f.read()
    for url, path in urls:
        data = data.replace(url, path)

with open('index2.html', 'w+') as f:
    f.write(data)
