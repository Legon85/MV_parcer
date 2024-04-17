import json

import requests


# from bs4 import BeautifulSoup
# from time import sleep


def get_data():
    cookies = {
        '__lhash_': 'de9054329c3cb9251f7b8a32777d19f9',
        'MVID_AB_PERSONAL_RECOMMENDS': 'true',
        'MVID_AB_UPSALE': 'true',
        'MVID_ACCESSORIES_PDP_BY_RANK': 'true',
        'MVID_ALFA_PODELI_NEW': 'true',
        'MVID_CASCADE_CMN': 'true',
        'MVID_CHAT_VERSION': '6.6.0',
        'MVID_CITY_ID': 'CityCZ_975',
        'MVID_CREDIT_DIGITAL': 'true',
        'MVID_CREDIT_SERVICES': 'true',
        'MVID_CRITICAL_GTM_INIT_DELAY': '3000',
        'MVID_DISPLAY_ACCRUED_BR': 'true',
        'MVID_DISPLAY_PERS_DISCOUNT': 'true',
        'MVID_EMPLOYEE_DISCOUNT': 'true',
        'MVID_FAVORIT_NEW': 'true',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_GTM_ENABLED': '011',
        'MVID_INTERVAL_DELIVERY': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_KLADR_ID': '7700000000000',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_NEW_CHAT_PDP': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_PODELI_PDP': 'true',
        'MVID_REGION_ID': '1',
        'MVID_REGION_SHOP': 'S002',
        'MVID_SERVICES': '111',
        'MVID_SERVICE_AVLB': 'true',
        'MVID_SINGLE_CHECKOUT': 'true',
        'MVID_SP': 'true',
        'MVID_TIMEZONE_OFFSET': '3',
        'MVID_TYP_CHAT': 'true',
        'MVID_WEB_SBP': 'true',
        'SENTRY_ERRORS_RATE': '0.1',
        'SENTRY_TRANSACTIONS_RATE': '0.5',
        'MVID_ENVCLOUD': 'prod2',
        'mindboxDeviceUUID': '48f5ad83-12a6-4847-8da4-232c5aae48f9',
        'directCrm-session': '%7B%22deviceGuid%22%3A%2248f5ad83-12a6-4847-8da4-232c5aae48f9%22%7D',
        '_ym_uid': '1713214630419416586',
        '_ym_d': '1713214630',
        '_ym_isad': '2',
        '_ga': 'GA1.1.1862728246.1713214630',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        'SMSError': '',
        'authError': '',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '11a25c6e-74e6-4e10-ae04-89377f2ed7c1',
        'tmr_lvid': 'a80be2f815c18d741d24d7b1cc50aef7',
        'tmr_lvidTS': '1713214633466',
        'flocktory-uuid': 'cfc1958d-7a91-435b-b49c-584365d3198a-8',
        'customer_email': 'null',
        'uxs_uid': 'bc1286e0-fb6a-11ee-b5dc-dbedafa504d2',
        'advcake_track_id': 'e252b717-8afd-0cf1-38b9-ae423c814eff',
        'advcake_session_id': '72fcf68a-b490-320d-5c7d-58aab3394962',
        'flacktory': 'no',
        'BIGipServeratg-ps-prod_tcp80': '1141169162.20480.0000',
        'bIPs': '-826759811',
        'domain_sid': 'DrHiRk1jpJKBuw8A_hxJL%3A1713214633755',
        'afUserId': 'a748b190-a92b-4bd6-95da-4396958b763e-p',
        'AF_SYNC': '1713214634065',
        '_sp_ses.d61c': '*',
        '__rhash_': 'a79e670c99c9884cf779ccdbf479b512',
        '__hash_': '75ff26c26df9c84cf7794033c0cd1ca3',
        'session': '1',
        'advcake_track_url': '%3D20240415xuiZzNo0qGdFHNwG%2FiPZYuvaMFgq3dyQcHcUXU0gKu%2FR7niJnNxS%2BzEYSWsNA6GNLi868K%2B9xHuG6aMoQzwV91WHjEIs7E2aM1%2BgfWz%2FboFpfCPa2uAtqRk7ocKVE2FdCsdbVzDceIuds5F8Kbb%2FduLa6nXq6GWyMi5vjzheX5WmHvme7Fz7GzGHNzOIdTXN9mYO35LvcVwrPVoa3GXHN5JYkgQff4KwjgtCnuZLxoPZl%2BVZOhSpvqlmFUf%2Bwus%2FgMETB7szKCaZ61gcC2l113VFh4rhW0%2Fy5sGV17EXGvN72hyrC1%2F4rq5sIW0Wlv5Uees5p3zLngAwuzkRRtOPrW6tGYCkdZRpdtsZxZJFZBHM1FlCi71CfRPFEGx65N%2FM7noPyjom1xVc3P1Wull4iFZULatztDiHBib9pg3fiYjMRWFU6zvJy4gXuiWAB9tVvH0KaIaxvBMWmAyr002VBCAS3cCvuEkxh7pZPPx5ohSj2ONflxnpOxOYeXuI9cXHYz4mKOV%2B49lSBy6JXvaoOESQosbwbCrcHe9Sbqd8jvAczWns3GnAwDp%2BzPAjdquaxM2PhtR%2FkaTPGaoP4td3Da879c0%2B2cAr8m2f7WuUj%2FotbLlF%2FZkPrXQky6eCtodt5GbUbPtg5kg7VWMf8fx8CeeL%2FSHnGSGwxrO5lDAdC7JYOgW6cVm%2BDKs%3D',
        'tmr_detect': '0%7C1713286138731',
        '_sp_id.d61c': '3b1f9335-87ae-42a5-a6b6-e5b88404f6d4.1713214630.3.1713286150.1713217973.d6dae760-d21b-4906-aacb-ec37383da6d1.5b6ea3b8-6796-4a51-877f-92061f3f5606.3b9da0c0-6232-48e7-8a36-09662216beb5.1713281287791.129',
        '_ga_CFMZTSS5FM': 'GS1.1.1713281287.4.1.1713286226.0.0.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1713281287.4.1.1713286226.60.0.0',
        'gsscgib-w-mvideo': 'gu+r8ky6A19L11UI5tY9uqYo7N6WKIA55od9HH6uI+xY8TeFvMzfv9Dol+AbgjiMt3GOHiDzLs+PKw3cG3pWBChC09NwIAsQXoASpZde28vW+hEnHO8Xod+kBnguQYTl0vCYrIfQ94Rcd+FR3hLg/qwjs+QgVpEL4TSlRgcYy1S6927yGvG6K1oB3Xc4YjXmGJYDqVp3uZAV2Uk+xyqoRyVWBvR73A2rytzVC3zWmTFMj6jJ/M3T5qfRHMGBtTDo2Q==',
        'gsscgib-w-mvideo': 'gu+r8ky6A19L11UI5tY9uqYo7N6WKIA55od9HH6uI+xY8TeFvMzfv9Dol+AbgjiMt3GOHiDzLs+PKw3cG3pWBChC09NwIAsQXoASpZde28vW+hEnHO8Xod+kBnguQYTl0vCYrIfQ94Rcd+FR3hLg/qwjs+QgVpEL4TSlRgcYy1S6927yGvG6K1oB3Xc4YjXmGJYDqVp3uZAV2Uk+xyqoRyVWBvR73A2rytzVC3zWmTFMj6jJ/M3T5qfRHMGBtTDo2Q==',
        'fgsscgib-w-mvideo': 'bnoobace9986aac410d3682eefd8176c0bfbe791',
        'fgsscgib-w-mvideo': 'bnoobace9986aac410d3682eefd8176c0bfbe791',
        'gsscgib-w-mvideo': 'X/VrxwkrgdjTYU95NSLYK7zTYgJQ6PF5YIsai1fPW8/OcmTzDtyDTC4knb4rJoBwE/T046Z+DUI+R2xb1utfnkqPaPNuhpCUz3UwlZ78+/DyDluBnHv5TGbTYOGogrZz9pPeSyQk9fOrTDCO3AWJ1BfXxc9WAZ/7j2dDDLeWVPc9RHdVYa3a0unfZqy0u3mTzFE5HyccajOI2RqPaGyT6nQh5RaO7rxAb2Jsb91Lws0AvivLVxFk3Mtghehi3/lOyg==',
        'cfidsgib-w-mvideo': '0Fny1dPdQQSn0oCHzKw22wKCrpCP9Td31Q/DMVzuODDwx1Cxu2qDpzswLyWyL7NN7mfeKDoeFJLiEgZ+H1+ToGbTShjta45R5hQIB2vNlmR2A2jM5rclysPOqwGg7XZ0flU/l4fbvU4DwI8G7m7zEydTVnyX57w/5r9AJ3I=',
    }

    headers = {
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'baggage': 'sentry-environment=production,sentry-release=release_24_4_2(6802),sentry-public_key=ae7d267743424249bfeeaa2e347f4260,sentry-trace_id=25b159d69cab4a048607e3c9852e0228,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=true',
        # 'cookie': '__lhash_=de9054329c3cb9251f7b8a32777d19f9; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ACCESSORIES_PDP_BY_RANK=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CHAT_VERSION=6.6.0; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_DISPLAY_ACCRUED_BR=true; MVID_DISPLAY_PERS_DISCOUNT=true; MVID_EMPLOYEE_DISCOUNT=true; MVID_FAVORIT_NEW=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_NEW_CHAT_PDP=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_PODELI_PDP=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICE_AVLB=true; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; mindboxDeviceUUID=48f5ad83-12a6-4847-8da4-232c5aae48f9; directCrm-session=%7B%22deviceGuid%22%3A%2248f5ad83-12a6-4847-8da4-232c5aae48f9%22%7D; _ym_uid=1713214630419416586; _ym_d=1713214630; _ym_isad=2; _ga=GA1.1.1862728246.1713214630; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=11a25c6e-74e6-4e10-ae04-89377f2ed7c1; tmr_lvid=a80be2f815c18d741d24d7b1cc50aef7; tmr_lvidTS=1713214633466; flocktory-uuid=cfc1958d-7a91-435b-b49c-584365d3198a-8; customer_email=null; uxs_uid=bc1286e0-fb6a-11ee-b5dc-dbedafa504d2; advcake_track_id=e252b717-8afd-0cf1-38b9-ae423c814eff; advcake_session_id=72fcf68a-b490-320d-5c7d-58aab3394962; flacktory=no; BIGipServeratg-ps-prod_tcp80=1141169162.20480.0000; bIPs=-826759811; domain_sid=DrHiRk1jpJKBuw8A_hxJL%3A1713214633755; afUserId=a748b190-a92b-4bd6-95da-4396958b763e-p; AF_SYNC=1713214634065; _sp_ses.d61c=*; __rhash_=a79e670c99c9884cf779ccdbf479b512; __hash_=75ff26c26df9c84cf7794033c0cd1ca3; session=1; advcake_track_url=%3D20240415xuiZzNo0qGdFHNwG%2FiPZYuvaMFgq3dyQcHcUXU0gKu%2FR7niJnNxS%2BzEYSWsNA6GNLi868K%2B9xHuG6aMoQzwV91WHjEIs7E2aM1%2BgfWz%2FboFpfCPa2uAtqRk7ocKVE2FdCsdbVzDceIuds5F8Kbb%2FduLa6nXq6GWyMi5vjzheX5WmHvme7Fz7GzGHNzOIdTXN9mYO35LvcVwrPVoa3GXHN5JYkgQff4KwjgtCnuZLxoPZl%2BVZOhSpvqlmFUf%2Bwus%2FgMETB7szKCaZ61gcC2l113VFh4rhW0%2Fy5sGV17EXGvN72hyrC1%2F4rq5sIW0Wlv5Uees5p3zLngAwuzkRRtOPrW6tGYCkdZRpdtsZxZJFZBHM1FlCi71CfRPFEGx65N%2FM7noPyjom1xVc3P1Wull4iFZULatztDiHBib9pg3fiYjMRWFU6zvJy4gXuiWAB9tVvH0KaIaxvBMWmAyr002VBCAS3cCvuEkxh7pZPPx5ohSj2ONflxnpOxOYeXuI9cXHYz4mKOV%2B49lSBy6JXvaoOESQosbwbCrcHe9Sbqd8jvAczWns3GnAwDp%2BzPAjdquaxM2PhtR%2FkaTPGaoP4td3Da879c0%2B2cAr8m2f7WuUj%2FotbLlF%2FZkPrXQky6eCtodt5GbUbPtg5kg7VWMf8fx8CeeL%2FSHnGSGwxrO5lDAdC7JYOgW6cVm%2BDKs%3D; tmr_detect=0%7C1713286138731; _sp_id.d61c=3b1f9335-87ae-42a5-a6b6-e5b88404f6d4.1713214630.3.1713286150.1713217973.d6dae760-d21b-4906-aacb-ec37383da6d1.5b6ea3b8-6796-4a51-877f-92061f3f5606.3b9da0c0-6232-48e7-8a36-09662216beb5.1713281287791.129; _ga_CFMZTSS5FM=GS1.1.1713281287.4.1.1713286226.0.0.0; _ga_BNX5WPP3YK=GS1.1.1713281287.4.1.1713286226.60.0.0; gsscgib-w-mvideo=gu+r8ky6A19L11UI5tY9uqYo7N6WKIA55od9HH6uI+xY8TeFvMzfv9Dol+AbgjiMt3GOHiDzLs+PKw3cG3pWBChC09NwIAsQXoASpZde28vW+hEnHO8Xod+kBnguQYTl0vCYrIfQ94Rcd+FR3hLg/qwjs+QgVpEL4TSlRgcYy1S6927yGvG6K1oB3Xc4YjXmGJYDqVp3uZAV2Uk+xyqoRyVWBvR73A2rytzVC3zWmTFMj6jJ/M3T5qfRHMGBtTDo2Q==; gsscgib-w-mvideo=gu+r8ky6A19L11UI5tY9uqYo7N6WKIA55od9HH6uI+xY8TeFvMzfv9Dol+AbgjiMt3GOHiDzLs+PKw3cG3pWBChC09NwIAsQXoASpZde28vW+hEnHO8Xod+kBnguQYTl0vCYrIfQ94Rcd+FR3hLg/qwjs+QgVpEL4TSlRgcYy1S6927yGvG6K1oB3Xc4YjXmGJYDqVp3uZAV2Uk+xyqoRyVWBvR73A2rytzVC3zWmTFMj6jJ/M3T5qfRHMGBtTDo2Q==; fgsscgib-w-mvideo=bnoobace9986aac410d3682eefd8176c0bfbe791; fgsscgib-w-mvideo=bnoobace9986aac410d3682eefd8176c0bfbe791; gsscgib-w-mvideo=X/VrxwkrgdjTYU95NSLYK7zTYgJQ6PF5YIsai1fPW8/OcmTzDtyDTC4knb4rJoBwE/T046Z+DUI+R2xb1utfnkqPaPNuhpCUz3UwlZ78+/DyDluBnHv5TGbTYOGogrZz9pPeSyQk9fOrTDCO3AWJ1BfXxc9WAZ/7j2dDDLeWVPc9RHdVYa3a0unfZqy0u3mTzFE5HyccajOI2RqPaGyT6nQh5RaO7rxAb2Jsb91Lws0AvivLVxFk3Mtghehi3/lOyg==; cfidsgib-w-mvideo=0Fny1dPdQQSn0oCHzKw22wKCrpCP9Td31Q/DMVzuODDwx1Cxu2qDpzswLyWyL7NN7mfeKDoeFJLiEgZ+H1+ToGbTShjta45R5hQIB2vNlmR2A2jM5rclysPOqwGg7XZ0flU/l4fbvU4DwI8G7m7zEydTVnyX57w/5r9AJ3I=',
        'referer': 'https://www.mvideo.ru/komputernaya-tehnika-4107/monitory-101?f_category=igrovye-monitory-3587&f_brand=thunderobot&f_tolko-v-nalichii=da&f_diagonal-ekrana=ot-30-do-34',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': '25b159d69cab4a048607e3c9852e0228-9a77d47e6a4a977e-1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-set-application-id': 'cacb4415-21f7-4326-85d6-8d04c919a629',
    }

    params = {
        'categoryId': '101',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJjYXRlZ29yeSIsIiIsImlncm92eWUtbW9uaXRvcnktMzU4NyJd',
            'WyJicmFuZCIsIiIsInRodW5kZXJvYm90Il0=',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
            'WyJkaWFnb25hbC1la3JhbmEiLCIiLCJvdC0zMC1kby0zNCJd',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()

    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get("materialPrices")

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json') as file:
        products_data = json.load(file)

    with open('4_items_prices.json') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        product_id = item.get('productId')

        if product_id in products_prices:
            prices = products_prices[product_id]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)



def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
