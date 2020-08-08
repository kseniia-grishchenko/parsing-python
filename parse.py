import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://shine-bright.com.ua/balibody')
html = BS(r.content, 'html.parser')
# print(html)

for product in html.select('.product'):
    # print(el)
    name = product.select('.data-gtag-name')
    price = product.select('.data-gtag-price')
    print(name[0].text, price[0].text)
