from bs4 import BeautifulSoup as beautifulSoup

soup = beautifulSoup('<p>Hello World!</p>', 'lxml')
print(soup.p.string)

with open("practice_code.html", "r", encoding="utf-8") as f:
    html = f.read()

soup = beautifulSoup(html, 'lxml')

print(soup.title.string)
print(soup.head)
print(soup.p.attrs)
print(soup.p.attrs['class'])


### CSS selector
print(soup.select('.movie-title'))
print(soup.select('.movie-title')[0].string)