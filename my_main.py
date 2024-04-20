import json
import requests
import time
from config import cookies, headers, params, TELE_TOKEN, chatId


def send_message(message):
    url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendMessage?chat_id={chatId}&text={message}"
    requests.get(url).json()


def get_prices():
    last_base_price = None
    last_sale_price = None
    last_bonus_rubles = None

    while True:
        # response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
        #                         headers=headers).json()
        with open('Thanderobot.json') as file:
            response = json.load(file)

        # with open('Thanderobot.json', 'w', encoding='utf-8') as f:
        #     json.dump(response, f, indent=4, ensure_ascii=False)

        current_bonus_rubles = response['body']['materialPrices'][0]['bonusRubles']['total']
        current_base_price = response['body']['materialPrices'][0]['price']['basePrice']
        current_sale_price = response['body']['materialPrices'][0]['price']['salePrice']

        if last_sale_price != current_sale_price:
            message = (f'Цены изменились\nСтарые цены:\n базовая цена: {last_base_price},цена со скидкой:'
                       f' {last_sale_price}, '
                       f'бонусы: {last_bonus_rubles} \nТекущие цены:\n базовая цена: {current_base_price}, '
                       f'цена со скидкой: '
                       f'{current_sale_price}, бонусы: {current_bonus_rubles}')

            send_message(message)

            last_sale_price = current_sale_price
            last_bonus_rubles = current_bonus_rubles
            last_base_price = current_base_price

        else:
            message2 = (f'Цены не изменились\nТекущие цены:\n  базовая цена: {current_base_price}, цена со скидкой'
                        f':{current_sale_price}, '
                        f'бонусы: {current_bonus_rubles}')
            send_message(message2)

        time.sleep(7)


# if __name__ == '__main__':
get_prices()
