#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb", 27017)
db = client.mvideo
collection = db.fin


@app.route("/")
def index():
    data = collection.find()
    return render_template("index.html", data=data)


cookies = {
    "MVID_CITY_ID": "CityR_72",
    "MVID_GUEST_ID": "19370295700",
    "MVID_REGION_ID": "72",
    "searchType2": "1",
    "MVID_TIMEZONE_OFFSET": "3",
    "MVID_KLADR_ID": "1200000100000",
    "MVID_REGION_SHOP": "S967",
}

headers = {
    "authority": "www.mvideo.ru",
    "accept": "application/json",
    "accept-language": "ru,en;q=0.9",
    "baggage": "sentry-environment=production,sentry-public_key=1e9efdeb57cf4127af3f903ec9db1466,sentry-trace_id=2246fce8b7274b4daf5f5f823e80d010,sentry-sample_rate=0.5,sentry-transaction=%2F**%2F,sentry-sampled=true",
    # 'cookie': 'MVID_CITY_ID=CityR_72; MVID_GUEST_ID=19370295700; MVID_REGION_ID=72; searchType2=1; MVID_TIMEZONE_OFFSET=3; MVID_KLADR_ID=1200000100000; MVID_REGION_SHOP=S967; afUserId=6057cd2f-b95f-418b-b522-d26b08b17536-p; uxs_uid=419d4c50-6f4f-11ec-8154-03a87f988083; HINTS_FIO_COOKIE_NAME=1; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_GET_LOCATION_BY_DADATA=DaData; NEED_REQUIRE_APPLY_DISCOUNT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; __ttl__widget__ui=1657461851894-d12116a60fd0; MVID_WEB_SBP=true; _ym_uid=1641514673371224866; tmr_lvid=9e9e5cc9eb3538c6c6cf74275b9311d6; tmr_lvidTS=1641514672152; flocktory-uuid=1cff2c38-ed9b-40a9-9ec8-b461934883b0-1; MVID_CASCADE_CMN=true; MVID_CREDIT_SERVICES=true; MVID_CRITICAL_GTM_INIT_DELAY=3000; MVID_FILTER_CODES=true; MVID_FLOCKTORY_ON=true; MVID_MINDBOX_DYNAMICALLY=true; MVID_SERVICES=111; MVID_SP=true; MVID_TYP_CHAT=true; SENTRY_ERRORS_RATE=0.1; _ym_d=1694896109; utm_term=; _gpVisits={"isFirstVisitDomain":true,"idContainer":"100025D5"}; _ga_TY7GLH5RV3=GS1.2.1694896112.1.1.1694896194.52.0.0; _ga_HCF1KSW48B=GS1.2.1694896108.1.1.1694896255.60.0.0; MVID_ALFA_PODELI_NEW=true; MVID_CHAT_VERSION=4.16.4; MVID_CREDIT_DIGITAL=true; MVID_INTERVAL_DELIVERY=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_PODELI_PDP=true; MVID_SERVICE_AVLB=true; MVID_SINGLE_CHECKOUT=true; _ga=GA1.1.1142230903.1641514672; __SourceTracker=yandex.ru__organic; admitad_deduplication_cookie=yandex.ru__organic; MVID_AB_UPSALE=true; MVID_GTM_ENABLED=011; SENTRY_TRANSACTIONS_RATE=0.5; advcake_track_id=175a321c-8713-d8b6-d299-170a80ee836d; advcake_session_id=83fe0c9e-40ab-c039-ab72-4f9c549e1601; __lhash_=9a8c73d1407809f7c09b6f2ab0127aa2; MVID_GEOLOCATION_NEEDED=false; MVID_VIEWED_PRODUCTS=; wurfl_device_id=generic_web_browser; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_YANDEX_WIDGET=true; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; COMPARISON_INDICATOR=false; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; deviceType=desktop; MVID_FILTER_TOOLTIP=1; MVID_LAYOUT_TYPE=1; AF_SYNC=1701253191727; MVID_EMPLOYEE_DISCOUNT=true; cfidsgib-w-mvideo=DY72iq8zorAvnHIlSVIvNdtTlL5C5r1CMtp5ivQbyhvzxFsSmJyGj4BamtQok8/7LETTpcTm713yH+hRHBESRfvPtQRs1ZlpQcv/1ZMGhGsk+EvwCejsDrAr/xz44sq2OHI0fMOzfHyXlVJxb0Kr5I1NhgTT+Bj/eYvLx9So; MVID_ENVCLOUD=prod1; mindboxDeviceUUID=3f957c21-3492-4073-a3b9-4ff5b34f1d94; directCrm-session=%7B%22deviceGuid%22%3A%223f957c21-3492-4073-a3b9-4ff5b34f1d94%22%7D; _ym_isad=1; _sp_id.d61c=89eda147-92d0-44b3-bbac-ae98a4bd51f4.1673374018.17.1701339677.1701254635.39c3b223-3a97-410f-a1e5-35a88c647d54.1e073ed1-0e5a-4ff4-8866-e724246b0ea0.ef46495e-de0f-4c4f-bc1c-38531f8dc4d4.1701339676722.5; tmr_detect=1%7C1701339680222; _gp100025D5={"hits":1,"vc":1,"ac":1}; MVID_AB_PERSONAL_RECOMMENDS=true; MVID_CROSS_POLLINATION=true; MVID_DISPLAY_ACCRUED_BR=2; MVID_IS_NEW_BR_WIDGET=true; __rhash_=9d5f6e7b7ccf7cd0f76344d8d90cda73; gsscgib-w-mvideo=223Dr9So0e8/QK/zdU1xSCWv0VEvYiGgHe9AjzAi0PE0wRtq4s3uZfCM6oiGuJfRcd6ct2pwq/EVSLp98SZTz7YaWgvD4US9T54T0XJgepByWR4VVa2qfXWJT3bWZpz8X0GKV15NThfDqnbAocDnaW0ov8+wPu6gnTjM/eS9rjDjCa4uICiRgtHCu6CB99ZCuBAhMalS2nQhVg19dlhCQigjzE6YdFKJFQIML7jm7qthGMWkGfHas/N++EHKZ9s=; gsscgib-w-mvideo=223Dr9So0e8/QK/zdU1xSCWv0VEvYiGgHe9AjzAi0PE0wRtq4s3uZfCM6oiGuJfRcd6ct2pwq/EVSLp98SZTz7YaWgvD4US9T54T0XJgepByWR4VVa2qfXWJT3bWZpz8X0GKV15NThfDqnbAocDnaW0ov8+wPu6gnTjM/eS9rjDjCa4uICiRgtHCu6CB99ZCuBAhMalS2nQhVg19dlhCQigjzE6YdFKJFQIML7jm7qthGMWkGfHas/N++EHKZ9s=; fgsscgib-w-mvideo=12uL4a0ca2c24059e0db9d0dba70fa2be848a899; fgsscgib-w-mvideo=12uL4a0ca2c24059e0db9d0dba70fa2be848a899; __hash_=68dfdcbf2bebacd15767c99ee683a1ae; _ga_BNX5WPP3YK=GS1.1.1701343456.19.0.1701343456.60.0.0; _ga_CFMZTSS5FM=GS1.1.1701343456.19.0.1701343456.0.0.0',
    "referer": "https://www.mvideo.ru/televizory-i-cifrovoe-tv-1/televizory-65?f_category=4k-uhd-televizory-1682&f_tolko-v-nalichii=da&f_skidka=da&f_diagonal=75---81&sort=price_asc",
    "sec-ch-ua": '"Chromium";v="116", "Not)A;Brand";v="24", "YaBrowser";v="23"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sentry-trace": "2246fce8b7274b4daf5f5f823e80d010-8d66260ab8b7d2f1-1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.686 YaBrowser/23.9.5.686 Yowser/2.5 Safari/537.36",
    "x-set-application-id": "31b860fa-d197-47cc-a6a1-f6ccf6f8cbca",
}

listing_params = {
    "categoryId": "65",
    "offset": "0",
    "limit": "24",
    "sort": "price_asc",
    "filterParams": [
        "WyJjYXRlZ29yeSIsIiIsIjRrLXVoZC10ZWxldml6b3J5LTE2ODIiXQ==",
        "WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==",
        "WyJza2lka2EiLCIiLCJkYSJd",
        "WyJkaWFnb25hbCIsIiIsIjc1LS0tODEiXQ==",
    ],
    "doTranslit": "true",
}


def get_data_from_mvideo():
    fin_list = {}
    listing_response = requests.get(
        "https://www.mvideo.ru/bff/products/listing",
        params=listing_params,
        cookies=cookies,
        headers=headers,
    )
    json_data = {
        "productIds": listing_response.json().get("body").get("products"),
        "mediaTypes": [
            "images",
        ],
        "category": True,
        "status": True,
        "brand": True,
        "propertyTypes": [
            "KEY",
        ],
        "propertiesConfig": {
            "propertiesPortionSize": 5,
        },
        "multioffer": False,
    }

    list_response = requests.post(
        "https://www.mvideo.ru/bff/product-details/list",
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    for i in list_response.json().get("body").get("products"):
        fin_list.update({str(i["productId"]): [i["name"]]})

    id_list_to_str = ",".join(
        str(i) for i in listing_response.json()["body"]["products"]
    )

    prices_params = {
        "productIds": id_list_to_str,
        "addBonusRubles": "true",
        "isPromoApplied": "true",
    }

    prices_response = requests.get(
        "https://www.mvideo.ru/bff/products/prices",
        params=prices_params,
        cookies=cookies,
        headers=headers,
    )

    for i in prices_response.json().get("body").get("materialPrices"):
        fin_list[i["productId"]].append(i["price"]["salePrice"])

    collection.delete_many(fin_list)
    collection.insert_one(fin_list)


get_data_from_mvideo()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
