import json
import requests
from config import cookies, headers, params2


def get_pus8507_prices():
    # response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params2, cookies=cookies,
    #                         headers=headers).json()

    with open('pus8507.json') as file:
        response = json.load(file)

    # with open('pus8507.json', 'w', encoding='utf-8') as f:
    #     json.dump(response, f, indent=4, ensure_ascii=False)

    current_bonus_rubles = response['body']['materialPrices'][0]['bonusRubles']['total']
    current_base_price = response['body']['materialPrices'][0]['price']['basePrice']
    current_sale_price = response['body']['materialPrices'][0]['price']['salePrice']

    return current_base_price, current_sale_price, current_bonus_rubles


if __name__ == '__main__':
    get_pus8507_prices()
