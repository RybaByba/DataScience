
from prices_db import get_last_price


recipe = {
    "pork": 500,
    "potatoes": 500,
    "beets": 500,
    "carrots": 200,
    "cabbage": 300,
    "onions": 200,
    "sour_cream": 200,
    "sunflower_oil": 20,
    "tomato_paste": 90,
}


def get_price(shop_name, recipe):
    last_shop_data = get_last_price(shop_name)

    for name, weight in recipe.items():
        borscht = []

        for item in last_shop_data:

            if item['unit'] == "weight":
                price = item['price_for_100gr']
                result_price = round(price * weight * 0.01, 2)
                borscht.append(result_price)

            elif item['unit'] == "count":

                if item["category"] == "sour_cream":
                    result_price = round(item['price_for_100gr'] * 200/350, 2)
                    borscht.append(result_price)

                elif item["category"] == "sunflower_oil":
                    result_price = round(item['price_for_100gr'] * 20/750, 2)
                    borscht.append(result_price)

                elif item["category"] == "tomato_paste":
                    result_price = round(item['price_for_100gr'] * 90/485, 2)
                    borscht.append(result_price)

        return (round(sum(borscht), 2))



