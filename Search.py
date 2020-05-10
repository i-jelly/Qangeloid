# -*- coding:utf-8 -*-
import re
import time
import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://zh.moegirl.org/index.php?search="


    
Header = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
            "cookie": "_ga=GA1.2.470584180.1586164666; __gads=ID=72a82448ce6715a9:T=1586164666:S=ALNI_MYCddajIL4xS4bvEPX7QVVqo_GBaA; _gid=GA1.2.769480504.1586754366; __cfduid=d62e5dccaba009d71e684f0784839dd3a1586754485; _gat=1",
            "referer": "https://mzh.moegirl.org/index.php?search=asdasdas&title=Special:%E6%90%9C%E7%B4%A2&profile=default&fulltext=1&searchToken=ewtploc7i4le4sa8dwskw4avk",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1",}


class moeGirl:

    def __init__(self):
        super().__init__()

    def getSearchContent(self,keywords):
        res = rq.get(url + keywords,headers = Header)
        while(int(res.status_code) != 200):
            if(int(res.status_code) > 400):
                return "爬虫错误"
        page = bs(res.text,"html.parser")
        if(len(page.select('p[class="mw-search-nonefound"]')) > 0):
            return "没有结果"
        result = page.select('div[class="mw-search-result-heading"]')
        times = len(result)
        reply = "结果如下:\n"
        if(times >= 3): 
            times = 3
            reply = "结果如下(过多结果取前三):\n"
        for i in range(times):
            reply = reply + result[i].contents[0]["title"] + "\n" + "https://zh.moegirl.org" + result[i].contents[0]["href"] + "\n"
        return reply


        
        
