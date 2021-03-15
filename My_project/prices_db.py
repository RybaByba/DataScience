import sqlite3
from config import db_file, table_price, table_name
from datetime import datetime
from recipe import get_price

create_db = f"""
CREATE TABLE IF NOT EXISTS {table_price}
                    (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     shop_name TEXT NOT NULL,
                     date DATE,
                     price REAL NOT NULL
                    )
"""
conn = sqlite3.connect(db_file)
curs = conn.cursor()
curs.execute(create_db)


def get_last_update_price(shop):

    last_date = curs.execute(f"""
    SELECT max (date) FROM {table_price} WHERE shop_name like '{shop}'
    """).fetchone()[0]
    last_date = datetime.strptime(last_date, "%Y-%m-%d").date()

    return last_date


def write_price_to_db(shop):

    insert_table = f"""
    INSERT INTO {table_price} (shop_name, date, price) VALUES (?,?,?)
    """
    dd = (shop, datetime.now().date(), get_price(shop))
    curs.execute(insert_table, dd)
    conn.commit()

def get_last_price_if_empty(shop_name, category):
    last_price = curs.execute(f"""
    SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop_name}' AND category = '{category}' 
    AND date = (SELECT max(date) AS d FROM {table_name} WHERE date != (SELECT max(date) FROM {table_name})) LIMIT 1
    """).fetchall()[0][0]

    return last_price

def get_last_price(shop_name):
    data = []
    last_prices = []
    last_date = curs.execute(f"""
        SELECT max (date) FROM {table_name} WHERE shop_name like '{shop_name}'
        """).fetchone()[0]

    res = curs.execute(f"""
             SELECT * FROM {table_name} WHERE shop_name like '{shop_name}' AND date = '{last_date}'
             """).fetchall()

    # NOTE: Need tp rewrite this !!!
    for c in range(0,len(res)):
        data.append(dict(zip([c[0] for c in curs.description], res[c])))

    # ----------------
    for d in data:

        if d["price_for_100gr"] == "":
           d["price_for_100gr"] = get_last_price_if_empty(shop_name, d['category'])
        last_prices.append(d)

    return last_prices

print(get_last_price("fora"))