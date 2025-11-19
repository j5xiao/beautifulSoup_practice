import requests
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import re

URL = 'https://ssr1.scrape.center/'

def scrape_page(url):
    try:
        respones = requests.get(url)
        if respones.status_code == 200:
            return respones.text
    except:
        return "Wrong!"
    
def get_page(url, count):
    path_url = f'{url}page/{count}'
    return scrape_page(path_url)

def find_all_url(html):
    html = BeautifulSoup(html, 'lxml')
    #result = html.find_all('a', class_='name')
    result = html.select('a.name')
    if len(result) == 0:
        return []
    for i in result:
        yield urljoin(URL, i['href'])

def main():
    html = get_page(URL, 1)
    content = find_all_url(html)
    save_file = []
    for i in list(content):
        save_elements = {}
        htmls = BeautifulSoup(scrape_page(i), 'lxml')
        name = htmls.select_one('div a h2').string
        categories = htmls.select('div .categories button span')
        category = []
        for i in categories:
            category.append(i.string)
        drama = htmls.select('div .drama p')[0].string.strip()

        save_elements['name'] = name
        save_elements['categories '] = ", ".join(category)
        save_elements['drama'] = drama

        save_file.append(save_elements)

    return save_file

        


if __name__ == '__main__':
    result = main()
    print(result)