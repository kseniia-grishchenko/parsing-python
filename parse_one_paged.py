import requests
from bs4 import BeautifulSoup as BS


def parse_one_paged(url, product_class, name_class, price_class, headers):
    r = requests.get(url, headers=headers)
    html = BS(r.content, 'html.parser')

    print(url, product_class, name_class, price_class)

    product_list = []

    for idx, product in enumerate(html.select(product_class)):
        name = product.select(name_class)
        price = product.select(price_class)
        if not price or not name:
            continue

        product_dict = {
            'name': name[0].text,
            'price': price[0].text
        }

        product_list.append(product_dict)

    return product_list
