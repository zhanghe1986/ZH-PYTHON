#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import os
import urllib.request as urllib2
import argparse
from bs4 import BeautifulSoup
from model.news import News


class CrawlerNewsContent(object):

    def __init__(self, news):
        self.news = news

    def _get_soup(self, url):
        req = urllib2.Request(
            url=url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'}
        )
        content = urllib2.urlopen(req).read()
        return BeautifulSoup(content)

    def _get_item(self, soup):
        content = ''
        p_item_list = soup.findAll('p')
        for p_item in p_item_list:
            if p_item.find('span'):
                span_item_list = p_item.findAll('span')
                for span_item in span_item_list:
                    if span_item and str(span_item.string) != 'None':
                        content = content + str(span_item.string) + '\n'
        self.news.set_content(content)

    def start(self):
        self.soup = self._get_soup(self.news.get_url())
        self._get_item(self.soup)


class CrawlerNews(object):

    def __init__(self, args):
        self.first_url = args.url
        self.next_url = self.first_url
        self.output = args.output
        self.dns = args.dns
        self.news_list = []

    def _get_soup(self, url):
        req = urllib2.Request(
            url=url,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4'}
        )
        content = urllib2.urlopen(req).read()
        return BeautifulSoup(content)

    def _get_item(self, soup):
        li_item_list = soup.findAll('li')
        for li_item in li_item_list:
            if li_item.find('div'):
                if li_item.find('div').find('h4'):
                    href = li_item.find('div').find('h4').find('a').get('href')
                    news = News(str(li_item.find('div').find('h4').find('a').string), self.dns + href.replace('../', ''), '')
                    self.news_list.append(news)

    def _get_next_page(self, soup):
        next_url_exist = False
        next_page_text = '下页'

        temp_list = self.next_url.split('/')
        pre_first_url = temp_list[0]
        for i in range(1, len(temp_list) - 1):
            pre_first_url = pre_first_url + '/' + temp_list[i]

        span_item_list = soup.findAll('span')
        for span_item in span_item_list:
            if span_item.find('a'):
                if str(span_item.find('a').string) == next_page_text:
                    next_url_exist = True
                    self.next_url = pre_first_url + '/' + span_item.find('a').get('href')
                    break

        if next_url_exist:
            self.soup = self._get_soup(self.next_url)
        else:
            self.soup = None

    def write_file(self, output):
        if not os.path.exists(output):
            os.mkdir(output)

        if not os.path.exists(os.path.join(output, 'news')):
            os.mkdir(os.path.join(output, 'news'))

        for news in self.news_list:
            title = news.get_title()\
                .replace('|', ' ')\
                .replace('<', ' ')\
                .replace('>', ' ')\
                .replace('"', ' ')\
                .replace('?', ' ')\
                .replace('*', ' ')\
                .replace(':', ' ')\
                .replace('\\', ' ')\
                .replace('/', ' ')
            title += '.txt'
            with open(os.path.join(output, 'news', title), 'w', encoding='utf-8') as f:
                f.write(news.get_content())

    def start(self):
        self.soup = self._get_soup(self.first_url)
        self._get_item(self.soup)
        while True:
            self._get_next_page(self.soup)
            if not self.soup:
                break
            self._get_item(self.soup)

        for news in self.news_list:
            print(news.get_title())
            crawler_news_content = CrawlerNewsContent(news)
            crawler_news_content.start()

        self.write_file(self.output)


def get_args():
    parser = argparse.ArgumentParser(description='A crawler for sitedossier.com')
    parser.add_argument('-dns', type=str, required=False, default='https://www.westlake.edu.cn/')
    parser.add_argument('-url', type=str, required=False, default='https://www.westlake.edu.cn/zjxh/xwdt/xyxx.htm')
    parser.add_argument('-output', type=str, required=False, default='C:/Users/lenovo/Desktop/西湖大学')

    args = parser.parse_args()
    return args


def main():
    args = get_args()
    crawler = CrawlerNews(args)
    crawler.start()


if __name__ == '__main__':
    main()
