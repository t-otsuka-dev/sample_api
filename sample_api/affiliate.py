# --*-- coding: utf-8  --*--

import json
import urllib
import bottlenose
from bs4 import BeautifulSoup

class SearchKeyword:
    def get_amazon(self, keyword):
        """
        AmazonAPI
        """
        ACCESS_KEY = "AKIAIMMBGZ2N3WPQJLRQ"
        SECRET_ACCESS_KEY = "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"
        ASSOCIATE_TAG = "sbps2017-22"


        amazon = bottlenose.Amazon(ACCESS_KEY, SECRET_ACCESS_KEY, ASSOCIATE_TAG, Region="JP")
        result = amazon.ItemSearch(Keywords=keyword, SearchIndex="All", ResponseGroup="Small, Offers")
        soup = BeautifulSoup(result, "lxml")
        items = soup.findAll('item')

        url_list = {}
        i = 0
        for item in items:
            if item.find('points') == None:
                point = '0'
            else:
                point = item.find('points').text

            if item.find('amount') == None:
                price = ''
                price_point = point
            else:
                price = item.find('amount').text
                price_point = str(int(item.find('amount').text)+int(point))

            url_list[str(i)] = { "Title":item.find('title').text,
                                 "Url":item.find('detailpageurl').text,
                                 "Price":price,
                                 "Point":point,
                                 "PricePoint":price_point
                                 }
            i = i + 1

        return url_list


    def get_yahoo(self, keyword):
        """
        YahooAPI
        """
        url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch?'
        appid = 'dj0zaiZpPVp2YzVCdlpaa3BxTyZzPWNvbnN1bWVyc2VjcmV0Jng9MWM-'
        contents = url + 'appid=' + appid + '&query=' + urllib.parse.quote(keyword)
        result = urllib.request.urlopen(contents)
        response = json.loads(result.read().decode('utf8'))
        items = response["ResultSet"]["0"]["Result"]
        url_list = {}
        i = 0

        for k, v in items.items():
            if k == str(i):
                if v["Point"]["Amount"] == None:
                    point = '0'
                else:
                    point = v["Point"]["Amount"]

                url_list[str(i)] = { "Title":v["Name"],
                                     "Url":v["Url"],
                                     "Price":v["Price"]["_value"],
                                     "Point":point,
                                     "PricePoint": str(int(v["Price"]["_value"]) + int(v["Point"]["Amount"]))
                                     }
                i = i + 1

        return url_list


    def get_itunes(self, keyword):
        """
        iTunesAPI
        """
        url = 'https://itunes.apple.com/search?'
        contents = url + 'term=' + urllib.parse.quote(keyword) + '&media=all&country=jp&lang=ja_jp'
        result = urllib.request.urlopen(contents)
        response = json.loads(result.read().decode('utf8'))
        items = response["results"]
        url_list = {}
        i = 0
        for item in items:
            if item["collectionName"] == None:
                continue
            else:
                title = item["collectionName"]

            if item["collectionViewUrl"] == None:
                continue
            else:
                urls = item["collectionViewUrl"]

            if item["collectionPrice"] == None:
                continue
            elif '-' in str(item["collectionPrice"]):
                continue
            else:
                price = round(int(item["collectionPrice"]))
                point = round(int(item["collectionPrice"])*0.07)
                price_point = str(int(item["collectionPrice"])+point)

            url_list[str(i)] = { "Title":str(title),
                                 "Url":str(urls),
                                 "Price":str(price),
                                 "Point":str(point),
                                 "PricePoint": str(price_point)
            }
            i = i + 1

        return url_list


class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s