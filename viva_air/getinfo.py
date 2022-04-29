import time
import json
import requests
# import redis

url_topstories = "https://hacker-news.firebaseio.com/v0/topstories.json"
response_url_topstories = requests.get(url_topstories)
json_topstories = response_url_topstories.json()

# r = redis.Redis(host="localhost", port=6379, db=0)
# r.flushdb()


info_items = []


def get_info(start, n):
   # r = redis.Redis(host="localhost", port=6379, db=0)
   # r.flushdb()

    list_items = json_topstories[start:n + start]
    # print(list_items)

    for i in list_items:

        url_item = "https://hacker-news.firebaseio.com/v0/item/" + str(i) + ".json"

        response_url_item = requests.get(url_item)
        dict_item = response_url_item.json()
        info_items.append(dict_item)

        json_item = json.dumps(dict_item)

        # r.psetex(i, 5000, json_item)

    return json_topstories, info_items



topstories, info_items = get_info(1, 3)
print(topstories)
print(info_items)

# print(r.keys())


# print(r.dbsize())
#
# time.sleep(3)
#
# print(r.dbsize())

# print(r.get("31033758"))









# print(info_items)
#
# print(type(info_items))
# print(type(info_items[0]))





# r.psetex("Alemania", 2000, "Berlin")
# print(r.get("Alemania"))
# time.sleep(3)
# print(r.get("Alemania"))