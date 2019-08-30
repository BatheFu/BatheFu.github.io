from pymongo import MongoClient
import pandas as pd
import numpy as np
import pymysql
import requests
import json

dat = pd.read_csv('dat.csv', encoding="utf-8")
# Connect to the mongoDB


con = MongoClient('localhost', 27107)
db = con['scrapydata']
posts = db['topic']


for i in range(0, 10):
    s = requests.sessions.Session()
    topic_url = dat.iloc[i, :][4]
    article_num = dat.iloc[i, :][1]
    jsonurl = dat.iloc[i, :][-1]
    jsonurl = jsonurl + '/items'
    print(topic_url, '\n', article_num, '\n', jsonurl)
    # Define Headers and refined params
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        'Referer': str(topic_url),

    }
    data = {'sort': 'hot',
            'start': 0,
            'count': int(article_num),
            'status_full_text': 1,
            }
    # Send the requests
    r = s.get(jsonurl, headers=headers, params=data)
    if r.status_code == 200:
        print("Success on Url", topic_url)
    else:
        print("error on processing url{}".format(topic_url))
    # Get the json file
    j = r.json()
    # Get the text
    text = [ele['target']['status']['text'] for ele in j['items']]
    author_id = [ele['target']['status']['author']['id'] for ele in j['items']]
    author_name = [ele['target']['status']['author']['name']
                   for ele in j['items']]
    keys = ['author_id', 'author_name', 'text']
    text_list = list()
    keys = ['author_id', 'author_name', 'text']
    for index in range(len(author_id)):
        values = [author_id[index], author_name[index], text[index]]
        text_dic = dict(zip(keys, values))
        text_list.append(text_dic)

    posts.insert_many(text_list)

    # Configure the MySQL database
#     con = pymysql.connect('localhost', 'scrapy',
#    'scrapy', 'scrapydata')
#     with con:
#         cur = con.cursor()
#         sql = "INSERT INTO topic (article_text) VALUES (%s)"
#         val = str(text)
#         cur.execute(sql, val)
#         con.commit()
# switch to mongoDB
