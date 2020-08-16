from parse_one_paged import parse_one_paged

AVAILABLE_SITES = [
    {
        'name': 'make up',
        'url': 'https://makeup.com.ua/brand/1771098/',
        'product_class': '.simple-slider-list__link',
        'name_class': '.simple-slider-list__name',
        'price_class': '.simple-slider-list__price',
        'type': 'one-paged'
    }
]

headers_example = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
}


def collect_data():
    for site in AVAILABLE_SITES:
        if site['type'] == 'one-paged':
            product_list = parse_one_paged(site['url'], site['product_class'], site['name_class'],
                                           site['price_class'], {})
            print(product_list)


if __name__ == "__main__":
    collect_data()
