# # def get_borscht():
# #
# #     borsch = []
# #
# #     for elem in get_data().items():
# #          current_elem = elem[1]
# #          borsch.append(current_elem["price"])
# #
# #     prices = [
# #                float(borsch[0])*5 +
# #                float(borsch[1])*5 +
# #                float(borsch[2])*5 +
# #                float(borsch[3])*2 +
# #                float(borsch[4])*3 +
# #                float(borsch[5])*2 +
# #                float(borsch[6])*200/350 +
# #                float(borsch[7])*20/750 +
# #                float(borsch[8])*90/485
# #             ]
# #
# #     return prices
# #
# # def get_borsch_data():
# #
# #     borsch_price = {}
# #     borsch_price.update(
# #         {
# #            "shop_name": "novus",
# #            "date": datetime.now().date(),
# #            "price": get_borscht()
# #         }
# #     )
# #     return borsch_price
# #
# # print(get_borsch_data())




# pork = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "pork"
    #     """).fetchall()[0][0]
    #
    # potatoes = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "potatoes"
    #     """).fetchall()[0][0]
    #
    # beets = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "beets"
    #     """).fetchall()[0][0]
    #
    # carrots = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "carrots"
    #     """).fetchall()[0][0]
    #
    # cabbage = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "cabbage"
    #     """).fetchall()[0][0]
    #
    # onions = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "onions"
    #     """).fetchall()[0][0]
    #
    # sour_cream = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "sour_cream"
    #     """).fetchall()[0][0]
    #
    # sunflower_oil = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "sunflower_oil"
    #     """).fetchall()[0][0]
    #
    # tomato_paste = curs.execute(f"""
    #     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #     AND category = "tomato_paste"
    #     """).fetchall()[0][0]

    # price_dict = {
    #     "pork": pork,
    #     "potatoes": potatoes,
    #     "beets": beets,
    #     "carrots": carrots,
    #     "cabbage": cabbage,
    #     "onions": onions,
    #     "sour_cream": sour_cream,
    #     "sunflower_oil": sunflower_oil,
    #     "tomato_paste": tomato_paste
    # }
    # for v in price_dict.values():
    #     if v != '':
    #         print(v)
    #     else:
    #         print("!!!!")

print(get_index_borscht("fora"))
    # price = (pork * 5
    #         + potatoes * 5
    #         + beets * 5
    #         + carrots * 2
    #         + cabbage * 3
    #         + onions * 2
    #         + sour_cream * 200/350
    #         + sunflower_oil * 20/750
    #         + tomato_paste * 90/485)
    #
    # return (round(price, 2))


# def get_last_update_price(shop):
#
#     last_date = curs.execute(f"""
#     SELECT max (date) FROM {table_price} WHERE shop_name like '{shop}'
#     """).fetchone()[0]
#     last_date = datetime.strptime(last_date, "%Y-%m-%d").date()
#
#     return last_date
#
#
# def write_price_to_db(shop):
#
#     insert_table = f"""
#     INSERT INTO {table_price} (shop_name, date, price) VALUES (?,?,?)
#     """
#     dd = (shop, datetime.now().date(), get_index_borscht(shop))
#     curs.execute(insert_table, dd)
#     conn.commit()


# pp = curs.execute(f"""
#     SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}' """).fetchall()

# _________________________________________FOR RECIPE________________________________________________
# try:
#     price_for_100gr = [x['price_for_100gr'] for x in last_shop_data if x['category'] == name and x['unit'] == "weight"][0]
#
# except IndexError:
#     price_for_100gr = [x['price_for_100gr'] for x in last_shop_data if x['category'] == name and x['unit'] == "count"][0]
#
# result_price = round(price_for_100gr * weight * 0.01, 2)
#
# print(f" {name} -> {weight} -> {price_for_100gr} - {result_price}" )
# # exit()

# for item in last_shop_data:
#     pprint(last_shop_data)






 # last_date = curs.execute(f"""
    #     SELECT max (date) FROM {table_name} WHERE shop_name like '{shop}'
    #     """).fetchone()[0]
    #
    # all_prices = curs.execute(f"""
    #          SELECT price_for_100gr FROM {table_name} WHERE shop_name like '{shop}' AND date = '{last_date}'
    #          """).fetchall()
    # #
    # def list_change(lstlst):
    #     all = []
    #
    #     for lst in lstlst:
    #         all.extend(lst)
    #
    #     return all

    # for elem in list_change(all_prices):
    #     if elem == "":
    #         borscht = curs.execute(f"""
    #                 SELECT price FROM {table_price} WHERE shop_name like '{shop}' AND date = (SELECT max(date) FROM {table_price})
    #         """).fetchone()[0]
    #     else:
    #          borscht = list_change(all_prices)[0] * 5 +\
    #                    list_change(all_prices)[1] * 5 +\
    #                    list_change(all_prices)[2] * 5 + \
    #                    list_change(all_prices)[3] * 2 + \
    #                    list_change(all_prices)[4] * 3 + \
    #                    list_change(all_prices)[5] * 2 + \
    #                    list_change(all_prices)[6] * 200/350 + \
    #                    list_change(all_prices)[7] * 20/750 + \
    #                    list_change(all_prices)[8] * +90/485
    #
#     # return borscht
#
# print(get_index_borscht("fora"))
#
#
