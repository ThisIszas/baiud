#coding:utf-8
import urllib
import urllib2
import re
import time
import cookielib
import requests
import termcolor
from Initial import start
from SaveInfo import save
from SaveInfo_2 import save2

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


def start_2(count):

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/52.0.2743.116 Safari/537.36', 'Referer': 'http://news.baidu.com/'}

    fi = open(r'C:\Users\Administrator\Desktop\other2\11.txt')
    count_2 = 0
    for each in fi:
        url = re.findall("http://(.*?)\"", each, re.S)
        url = "http://"+url[0]
        print url
        save(count, 2, url)
        response = requests.get(url, headers)
        body = response.text

        word = re.findall("_(.*?)<", body, re.S)
        all_news = re.findall(u"找到相关新闻约(.*?)篇</", body, re.S)
        if len(all_news) == 0:
            all_news = re.findall(u"找到相关新闻(.*?)篇</", body, re.S)
        if len(all_news) > 0:
            try:
                temp = all_news[0].split(',')
                news_count = "".join(temp)
            except Exception, e:
                termcolor.cprint(e, 'red')
                news_count = all_news[0]
        else:
            save2(count_2, 0, 'Error 001')
            save2(count_2, 1, url)
            save2(count_2, 2, count+1)
            termcolor.cprint("    Error 001", 'red')
            save(count, 0, 'error')
            save(count, 1, 'error')
            count += 1
            count_2 += 1
            continue

        if len(word) > 0:
            news_count = int(news_count)
            name = word[0]
            save(count, 0, name)
            save(count, 1, news_count)
            print str(count) + "   " + time.ctime() + " " + name + u" 总数:" + str(news_count)
        else:
            termcolor.cprint("    Error 002", 'red')
            save(count, 0, "word_error")
            save2(count_2, 0, 'Error 002')
            save2(count_2, 1, url)
            save2(count_2, 2, count+1)
            count_2 += 1
        count += 1


if __name__ == '__main__':
    start()
    get_cookies()
    start_2(1)
