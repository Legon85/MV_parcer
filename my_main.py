import json
from notifiers import get_notifier
import time
import telegram_send
import requests
from config import cookies, headers, params, TELE_TOKEN, chatId


def get_prices():
    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    bonusRubles = response['body']['materialPrices'][0]['bonusRubles']['total']
    basePrice = response['body']['materialPrices'][0]['price']['basePrice']
    salePrice = response['body']['materialPrices'][0]['price']['salePrice']

    print(f"базовая цена: {basePrice}")
    print(f"цена со скидкой: {salePrice}")
    print(f"бонусы: {bonusRubles}")


def notif():
    while True:
        what = input('О чём напомнить?\nДля выхода отправьте \'exit\'')
        if what == 'exit':
            break
        else:
            t = input("через сколько минут напомнить?\n")
            t = int(t) * 60
            time.sleep(t)

            telegram = get_notifier('telegram')
            telegram.notify(token=TELE_TOKEN, chat_id=chatId, message=what)

# if __name__ == '__main__':
    # tele_send()
    # get_prices()
