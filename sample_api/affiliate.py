# --*-- coding: utf-8  --*--

import json
import sys
import urllib
import bottlenose
from bs4 import BeautifulSoup

class SearchKeyword:
    def get_amazon(self, keyword):

        """
        AmazonAPI
        :param keyword: iphone
        :return: URLリスト
        """
        ACCESS_KEY = "AKIAIMMBGZ2N3WPQJLRQ"
        SECRET_ACCESS_KEY = "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"
        ASSOCIATE_TAG = "sbps2017-22"


        amazon = bottlenose.Amazon(ACCESS_KEY, SECRET_ACCESS_KEY, ASSOCIATE_TAG, Region="JP")
        response = amazon.ItemSearch(Keywords=keyword, SearchIndex="All")
        soup = BeautifulSoup(response, "lxml")

        contents = soup.find_all("detailpageurl")

        url_list = list()
        for urls in contents:
            url_list.append(str(urls))

        res = json.dumps(url_list, ensure_ascii=False)

        return res


    def get_yahoo(self, keyword):
        """
        YahooAPI
        :param keyword: iphone
        :return: all
        """

        url = 'http://shopping.yahooapis.jp/ShoppingWebService/V1/json/itemSearch?'
        appid = 'dj0zaiZpPVp2YzVCdlpaa3BxTyZzPWNvbnN1bWVyc2VjcmV0Jng9MWM-'
        contents = url + 'appid=' + appid + '&query=' + keyword
        result = urllib.request.urlopen(contents)
        response = json.loads(result.read().decode('utf8'))


        contents = response["ResultSet"]["0"]["Result"]

        res = json.dumps(contents, ensure_ascii=False)

        return res

        '''
        #Tag01_メモ
        params = urllib.parse.urlencode(
            {'appid': appid,
             'query': keyword,})
        contents = urllib.parse.urlencode(url + params)
        #res = response.read()
        #soup = BeautifulSoup(res, "lxml")
        '''



    def get_itunes(self, keyword):
        """
        iTunesAPI
        :param keyword: iphone
        :return: all
        """
        url = 'https://itunes.apple.com/search?'
        contents = url + 'term=' + keyword + '&media=all&country=jp&lang=ja_jp'
        result = urllib.request.urlopen(contents)
        response = json.loads(result.read().decode('utf8'))

        res = json.dumps(response, ensure_ascii=False)

        return res

        '''
        #Tag01_メモ
        params = urllib.parse.urlencode(
            {'term': keyword,
             'media': 'all',
             'country': 'jp',
             'lang': 'ja_jp'})
        response = urllib.parse.urlencode(url + params)
        res = response.read()
        soup = BeautifulSoup(res, "lxml")
        '''


class MyObj(object):
    def __init__(self, s):
        self.s = s
    def __repr__(self):
        return '<MyObj(%s)>' % self.s