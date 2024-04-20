from get_thanderobot import get_thunder_prices
from get_pus8507 import get_pus8507_prices
import time
import requests
from config import TELE_TOKEN, chatId


def send_message(message):
    url = f"https://api.telegram.org/bot{TELE_TOKEN}/sendMessage?chat_id={chatId}&text={message}"
    requests.get(url).json()


def notice():
    last_thunder_prices = (None, None, None)
    last_pus8507_prices = (None, None, None)

    while True:

        # ПРОВЕРКА ЦЕН НА МОНИТОР
        current_thunder_prices = get_thunder_prices()
        if last_thunder_prices != current_thunder_prices:
            message = (
                f'Цены изменились\nСтарые цены:\n базовая цена: {last_thunder_prices[0]},цена со скидкой:'
                f' {last_thunder_prices[
                    1]}, '
                f'бонусы: {last_thunder_prices[2]} \nТекущие цены:\n базовая цена: '
                f'{current_thunder_prices[0]}, '
                f'цена со скидкой: '
                f'{current_thunder_prices[1]}, бонусы: {current_thunder_prices[2]}')

            send_message(message)

            last_thunder_prices = current_thunder_prices

        else:
            pass
            #     message2 = (f'Цены не изменились\nТекущие цены:\n  базовая цена: {current_thunder_prices[0]},'
            #                 f' цена со скидкой'
            #                 f':{current_thunder_prices[1]}, '
            #                 f'бонусы: {current_thunder_prices[2]}')
            #     send_message(message2)

            time.sleep(7)

        # ПРОВЕРКА ЦЕН НА ТЕЛЕВИЗОР
        current_pus8507_prices = get_pus8507_prices()
        if last_pus8507_prices != current_pus8507_prices:
            message = (
                f'Цены изменились\nСтарые цены:\n базовая цена: {last_pus8507_prices[0]},цена со скидкой:'
                f' {last_pus8507_prices[
                    1]}, '
                f'бонусы: {last_pus8507_prices[2]} \nТекущие цены:\n базовая цена: '
                f'{current_pus8507_prices[0]}, '
                f'цена со скидкой: '
                f'{current_pus8507_prices[1]}, бонусы: {current_pus8507_prices[2]}')

            send_message(message)

            last_pus8507_prices = current_pus8507_prices

        else:
            pass
        #     message2 = (f'Цены не изменились\nТекущие цены:\n  базовая цена: {current_pus8507_prices[0]},'
        #                 f' цена со скидкой'
        #                 f':{current_pus8507_prices[1]}, '
        #                 f'бонусы: {current_pus8507_prices[2]}')
        #     send_message(message2)

        time.sleep(7)


if __name__ == '__main__':
    notice()
