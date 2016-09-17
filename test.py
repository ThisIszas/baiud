#  -*-coding:utf-8-*-
import urllib
import urllib2
import re
import time
import cookielib
import requests
from lxml import etree
from Initial import start
from SaveInfo import save


def change_pn(url, pn):
    search_url = re.sub('pagenum', str(pn), url)
    return search_url


def change_word(word):
    init_search_url = "http://news.baidu.com/ns?word=???&\
    pn=pagenum&cl=2&ct=1&tn=news&rn=20&ie=utf-8&bt=0&et=0&rsv_page=1"
    word_encode = urllib.quote(word)
    search_url = re.sub('\?\?\?', word_encode, init_search_url)
    return search_url


def get_cookies():
    cj = cookielib.LWPCookieJar()
    cookie_support = urllib2.HTTPCookieProcessor(cj)
    opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
    urllib2.install_opener(opener)


def start_2(count, pn):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/52.0.2743.116 Safari/537.36', 'Referer': 'http://news.baidu.com/'}

    word = raw_input("请输入关键字:")
    search_url = change_word(word)
    url = change_pn(search_url, pn)

    response = requests.get(url, headers)
    body = response.text

    all_news = re.findall(u"找到相关新闻约(.*?)篇</", body, re.S)
    temp = all_news[0].split(',')
    news_count = "".join(temp)
    news_count = int(news_count)

    save(count, 0, word)
    save(count, 1, news_count)
    print word + " 总数:" + str(news_count)
    time.sleep(5)
    count += 1
    pn += 20

    start_2(count, pn)


if __name__ == '__main__':
    start()
    get_cookies()
    start_2(1,0)