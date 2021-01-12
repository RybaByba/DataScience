# 1. Вивести курс долару за рік, середнє значення та відхилення
# 2. Вивести середнє значення та відхилення курс долару окремо за кожен місяць.

import datetime
import pickle
import requests
import os
import numpy
from pprint import pprint

pickle_file = "currentcy_data.pikle"
currency_dict = {}
first_date = datetime.date(2020, 1, 1)
last_date = datetime.date(2020, 12, 31)

delta = last_date - first_date + datetime.timedelta(1)


def get_nbu_currencyes(first_date, delta):
    """
    Отримуємо курс НБУ
    :param first_date: дата з якої хочемо отримати курс
    :param delta: різниця днів між початковою і кінцевою датою
    :return: повертає список словарів на кожну дату
    """
    currencyDays = []

    for date in range(delta.days):
        currency_day = first_date + datetime.timedelta(date)
        url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={currency_day.strftime('%Y%m%d')}&json"
        r = requests.get(url)
        data = r.json()[0]
        data['exchangedate'] = datetime.datetime.strptime(data['exchangedate'], "%d.%m.%Y").date()
        currencyDays.append(data)

    return currencyDays


def read_pickle():
    """
    Прочитати файл
    :return: повертає завантажений файл
    """
    with open(pickle_file, 'rb') as f:
        return pickle.load(f)


def write_pickle():
    """
    записує файл (обновлює)
    :return: обновлений файл
    """
    currency_dict.update(
        {
            "nbu_usd": get_nbu_currencyes(first_date, delta),
            "last_date": last_date
        }
    )

    with open(pickle_file, 'wb') as NBU:
        pickle.dump(currency_dict, NBU)

    return currency_dict


def update_pickle(currency_dict):
    first_date = currency_dict['last_date']
    delta = last_date - first_date + datetime.timedelta(1)

    currency_dict["nbu_usd"] += get_nbu_currencyes(first_date, delta)
    currency_dict["last_date"] = last_date

    with open(pickle_file, 'wb') as NBU:
        pickle.dump(currency_dict, NBU)

    return currency_dict


def get_value_for_month(month, currency_dict):
    monts_rates = []

    for day in currency_dict['nbu_usd']:

        if month == day['exchangedate'].month:
            monts_rates.append(day['rate'])

    return monts_rates


if __name__ == '__main__':

    if os.path.exists(pickle_file):  # перевіряємо чи існує файл. якщо існує, визиваємо ф-ю для читання файлу
        print("FILE EXIST! READ FILE!")
        currency_dict = read_pickle()

    else:
        print("FILE IS NOT EXIST!")  # якщо файлу не інує, визиваємо ф-ю для запису у файл
        currency_dict = write_pickle()

    if currency_dict['last_date'] < last_date:  # якщо дата останнього курсу менша поточної, визиваємо ф-ю оновити
        print("UPDATE FILE!!")
        currency_dict = update_pickle(currency_dict)

    mounts_rates = []

    for m in range(1, 13):
        month_data = get_value_for_month(month=m, currency_dict=currency_dict)

        if month_data:
            mounts_rates.append(
                {
                    f"month_{m}": {
                        "average value": round(numpy.mean(month_data), 2),
                        "standard_deviation": round(numpy.std(month_data), 2)
                    }
                }
            )

    pprint(mounts_rates)

    rate_year = [day['rate'] for day in currency_dict['nbu_usd']]
    cc = (f"""rate for year: {rate_year}, 
average value for year: {round(numpy.mean(rate_year), 2)}
standard_deviation for year {round(numpy.std(rate_year), 2)}""")
    print(cc)
