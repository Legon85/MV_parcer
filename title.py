# import json
import requests


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
    'afUserId': 'a748b190-a92b-4bd6-95da-4396958b763e-p',
    'AF_SYNC': '1713214634065',
    '_ym_isad': '2',
    'domain_sid': 'DrHiRk1jpJKBuw8A_hxJL%3A1713310654007',
    '_sp_id.d61c': '3b1f9335-87ae-42a5-a6b6-e5b88404f6d4.1713214630.5.1713373847.1713310654.40886c2e-1e6b-43b9-9067-de5b329f60c3.97712b41-c66a-4475-9237-9150b1acb7bd.a114fa78-0480-46fc-98ac-82d48cbb320f.1713373817464.13',
    'advcake_track_url': '%3D20240415ZI6LEpwe1ucD9%2FSd7qgSwla5b%2Fyh8iRtHiZSsFC52dN1j9pIsQtpu2QzcBvgiuTj%2B%2Broyy2gweH5bDUWvNNBU5A3bFHCmgDXLe7KA%2FOw0NnJQrfojmB4TqcP7OApNG3nRMuwovXi3PL1EzTr%2BwqvNbvfp41nPfdoSIJJpNG9X2QtB5YVEvi7H8OjhW3Gt0wcDcK%2BLTsBXtKBZUwV5gvfJlO1QHvXXj6mDeA8vqjT7PNDorTrwN0aogKszh3WWUee0YncT8vW3tY6B7mSo9XA3nsMWjt6P5DOiyqMXBYtACDMekwRHiCZs0t8fiojVgwLTGIzl8R3tmGAPJBFljWUhJi8ab%2Fke4zSUDUgnJkMQap0mThiVLOprcfwnKkLn5ylAhYc06BzYkP4dyHJAuKNZpJhdFX1kaEBzMsv4WFFih4gaMXTqhXScOTJ4ZfnQpgkfLrvdrnaz%2FVG%2F1HRrJxrR6lRh%2FkWRDXhpu7i0tKjB49uXmklDsh8ha3A7la%2Bgl%2Ba%2BxWhFI5PrvQw0YmPBTGc%2BBILxJQ5fltbi2Ege9XhJlOHNqRsH8Cgrog%2F8dqpnRvU%2FMPABFFmb9o0uP4PTc1x6AhnEXsAVIryXt6uxzh0bNfDeoqX6g1XxqCJ37zb52rc46AxkLvKit2Z0HKY4egr9R4%2BAUoQcaknrUfzCbM8SdvTGzQlHwJcbeo%3D',
    'tmr_detect': '0%7C1713373849314',
    'gsscgib-w-mvideo': 'Kqklb2eQmYzNl2N7E+4vp1OD82ckSHzsuSrgopyvEWIoYK5XPxofa/rxQJquSerB2alpi6G+0Hr8gQyvfEFOXP82xFu1APGs57DAPafxh7op5VDndlh8RaGFABJtz2iO2t5xZXiQ9HU90xyBVBcTJAuSd+bWyjjw5kT8x7GEtNv3JWFrDOucxmJk7krWNkOBGCJZ/OYNoBCjCjvZaFECuiBwYoCB19dwAVtgDoStShH79g7StkMhynfTcIoW6qjiRzs=',
    'gsscgib-w-mvideo': 'Kqklb2eQmYzNl2N7E+4vp1OD82ckSHzsuSrgopyvEWIoYK5XPxofa/rxQJquSerB2alpi6G+0Hr8gQyvfEFOXP82xFu1APGs57DAPafxh7op5VDndlh8RaGFABJtz2iO2t5xZXiQ9HU90xyBVBcTJAuSd+bWyjjw5kT8x7GEtNv3JWFrDOucxmJk7krWNkOBGCJZ/OYNoBCjCjvZaFECuiBwYoCB19dwAVtgDoStShH79g7StkMhynfTcIoW6qjiRzs=',
    'fgsscgib-w-mvideo': 'Kvp7978b2822777a0723b605ea1d3b7e95e2c635',
    'fgsscgib-w-mvideo': 'Kvp7978b2822777a0723b605ea1d3b7e95e2c635',
    'gsscgib-w-mvideo': 'g8Szd4X5mYT7DhxLFYHjjWw+YJzFaFBT8Ppz26HPK0ZDEQPSwCwCF/9NPhpPpJVfFN6XD5sGiMsoamNYAIJ7LzZII3SeGRMzzB2ShdNggoI3BFKOqSYNMXh6gm0kIbGqfXxZ2LHFlllP6q3lkPV+FWGRS7TUWxKsudscb+v/1OTarrOnktNriSN/POroqPjDI1a8idPyVseQa0aIe6pCaCQQmCsU4S1KYn9emn8uyYFnwVoKw09vcHhYlAd/CUjSgnU=',
    'cfidsgib-w-mvideo': '5H/aKbtCKZ/gx85XViSCSo/7daHCtIlzYNVd2WJiFFSW9pv54ZTAssEZ399uVmB8S82fKxnRyrJM5lmqj5au5/6QL17ll7QCGBJfGdbxwZje95DTZeEyMxhz70czhS52cgEYULyFcjFq0WV3Vx1awQCWJ7z+28vb/wwE78w=',
    '__hash_': 'ef79732326e6c8679778f9b8328f54b3',
    '_ga_CFMZTSS5FM': 'GS1.1.1713381263.8.0.1713381263.0.0.0',
    '_ga_BNX5WPP3YK': 'GS1.1.1713381263.8.0.1713381263.60.0.0',
}

headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': '__lhash_=de9054329c3cb9251f7b8a32777d19f9; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_AB_UPSALE=true; MVID_ACCESSORIES_PDP_BY_RANK=true; MVID_ALFA_PODELI_NEW=true; MVID_CASCADE_CMN=true; MVID_CHAT_VERSION=6.6.0; MVID_CITY_ID=CityCZ_975; MVID_CREDIT_DIGITAL=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_DISPLAY_ACCRUED_BR=true; MVID_DISPLAY_PERS_DISCOUNT=true; MVID_EMPLOYEE_DISCOUNT=true; MVID_FAVORIT_NEW=true; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GTM_ENABLED=011; MVID_INTERVAL_DELIVERY=true; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_NEW_CHAT_PDP=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_PODELI_PDP=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICE_AVLB=true; MVID_SINGLE_CHECKOUT=true; MVID_SP=true; MVID_TIMEZONE_OFFSET=3; MVID_TYP_CHAT=true; MVID_WEB_SBP=true; SENTRY_ERRORS_RATE=0.1; SENTRY_TRANSACTIONS_RATE=0.5; MVID_ENVCLOUD=prod2; mindboxDeviceUUID=48f5ad83-12a6-4847-8da4-232c5aae48f9; directCrm-session=%7B%22deviceGuid%22%3A%2248f5ad83-12a6-4847-8da4-232c5aae48f9%22%7D; _ym_uid=1713214630419416586; _ym_d=1713214630; _ga=GA1.1.1862728246.1713214630; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; SMSError=; authError=; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=11a25c6e-74e6-4e10-ae04-89377f2ed7c1; tmr_lvid=a80be2f815c18d741d24d7b1cc50aef7; tmr_lvidTS=1713214633466; flocktory-uuid=cfc1958d-7a91-435b-b49c-584365d3198a-8; customer_email=null; uxs_uid=bc1286e0-fb6a-11ee-b5dc-dbedafa504d2; advcake_track_id=e252b717-8afd-0cf1-38b9-ae423c814eff; advcake_session_id=72fcf68a-b490-320d-5c7d-58aab3394962; flacktory=no; BIGipServeratg-ps-prod_tcp80=1141169162.20480.0000; bIPs=-826759811; afUserId=a748b190-a92b-4bd6-95da-4396958b763e-p; AF_SYNC=1713214634065; _ym_isad=2; domain_sid=DrHiRk1jpJKBuw8A_hxJL%3A1713310654007; _sp_id.d61c=3b1f9335-87ae-42a5-a6b6-e5b88404f6d4.1713214630.5.1713373847.1713310654.40886c2e-1e6b-43b9-9067-de5b329f60c3.97712b41-c66a-4475-9237-9150b1acb7bd.a114fa78-0480-46fc-98ac-82d48cbb320f.1713373817464.13; advcake_track_url=%3D20240415ZI6LEpwe1ucD9%2FSd7qgSwla5b%2Fyh8iRtHiZSsFC52dN1j9pIsQtpu2QzcBvgiuTj%2B%2Broyy2gweH5bDUWvNNBU5A3bFHCmgDXLe7KA%2FOw0NnJQrfojmB4TqcP7OApNG3nRMuwovXi3PL1EzTr%2BwqvNbvfp41nPfdoSIJJpNG9X2QtB5YVEvi7H8OjhW3Gt0wcDcK%2BLTsBXtKBZUwV5gvfJlO1QHvXXj6mDeA8vqjT7PNDorTrwN0aogKszh3WWUee0YncT8vW3tY6B7mSo9XA3nsMWjt6P5DOiyqMXBYtACDMekwRHiCZs0t8fiojVgwLTGIzl8R3tmGAPJBFljWUhJi8ab%2Fke4zSUDUgnJkMQap0mThiVLOprcfwnKkLn5ylAhYc06BzYkP4dyHJAuKNZpJhdFX1kaEBzMsv4WFFih4gaMXTqhXScOTJ4ZfnQpgkfLrvdrnaz%2FVG%2F1HRrJxrR6lRh%2FkWRDXhpu7i0tKjB49uXmklDsh8ha3A7la%2Bgl%2Ba%2BxWhFI5PrvQw0YmPBTGc%2BBILxJQ5fltbi2Ege9XhJlOHNqRsH8Cgrog%2F8dqpnRvU%2FMPABFFmb9o0uP4PTc1x6AhnEXsAVIryXt6uxzh0bNfDeoqX6g1XxqCJ37zb52rc46AxkLvKit2Z0HKY4egr9R4%2BAUoQcaknrUfzCbM8SdvTGzQlHwJcbeo%3D; tmr_detect=0%7C1713373849314; gsscgib-w-mvideo=Kqklb2eQmYzNl2N7E+4vp1OD82ckSHzsuSrgopyvEWIoYK5XPxofa/rxQJquSerB2alpi6G+0Hr8gQyvfEFOXP82xFu1APGs57DAPafxh7op5VDndlh8RaGFABJtz2iO2t5xZXiQ9HU90xyBVBcTJAuSd+bWyjjw5kT8x7GEtNv3JWFrDOucxmJk7krWNkOBGCJZ/OYNoBCjCjvZaFECuiBwYoCB19dwAVtgDoStShH79g7StkMhynfTcIoW6qjiRzs=; gsscgib-w-mvideo=Kqklb2eQmYzNl2N7E+4vp1OD82ckSHzsuSrgopyvEWIoYK5XPxofa/rxQJquSerB2alpi6G+0Hr8gQyvfEFOXP82xFu1APGs57DAPafxh7op5VDndlh8RaGFABJtz2iO2t5xZXiQ9HU90xyBVBcTJAuSd+bWyjjw5kT8x7GEtNv3JWFrDOucxmJk7krWNkOBGCJZ/OYNoBCjCjvZaFECuiBwYoCB19dwAVtgDoStShH79g7StkMhynfTcIoW6qjiRzs=; fgsscgib-w-mvideo=Kvp7978b2822777a0723b605ea1d3b7e95e2c635; fgsscgib-w-mvideo=Kvp7978b2822777a0723b605ea1d3b7e95e2c635; gsscgib-w-mvideo=g8Szd4X5mYT7DhxLFYHjjWw+YJzFaFBT8Ppz26HPK0ZDEQPSwCwCF/9NPhpPpJVfFN6XD5sGiMsoamNYAIJ7LzZII3SeGRMzzB2ShdNggoI3BFKOqSYNMXh6gm0kIbGqfXxZ2LHFlllP6q3lkPV+FWGRS7TUWxKsudscb+v/1OTarrOnktNriSN/POroqPjDI1a8idPyVseQa0aIe6pCaCQQmCsU4S1KYn9emn8uyYFnwVoKw09vcHhYlAd/CUjSgnU=; cfidsgib-w-mvideo=5H/aKbtCKZ/gx85XViSCSo/7daHCtIlzYNVd2WJiFFSW9pv54ZTAssEZ399uVmB8S82fKxnRyrJM5lmqj5au5/6QL17ll7QCGBJfGdbxwZje95DTZeEyMxhz70czhS52cgEYULyFcjFq0WV3Vx1awQCWJ7z+28vb/wwE78w=; __hash_=ef79732326e6c8679778f9b8328f54b3; _ga_CFMZTSS5FM=GS1.1.1713381263.8.0.1713381263.0.0.0; _ga_BNX5WPP3YK=GS1.1.1713381263.8.0.1713381263.60.0.0',
    'referer': 'https://www.mvideo.ru/products/monitor-igrovoi-thunderobot-34-va-3440x1440-165gc-chernyi-kq34c144c-400095286',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

params = {
    'productId': '400095286',
}

response = requests.get('https://www.mvideo.ru/bff/product-details?productId=400095286', cookies=cookies,
                        headers=headers).json()

print(response)

# with open('name.json', 'w', encoding='utf-8') as file:
#     json.dump(response, file, indent=2, ensure_ascii=False)
#
#
# def get_name():
#     with open('name.json', 'r', encoding='utf-8', errors='ignore') as f:
#         products_data = json.load(f)
#
#     print(products_data)
#
#
# if __name__ == '__main__':
#     get_name()
