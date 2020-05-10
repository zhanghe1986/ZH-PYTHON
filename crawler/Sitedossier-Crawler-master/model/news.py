#!/usr/bin/env python
# -*- coding: utf-8 -*-

class News(object):

    def __init__(self, title, url, content):
        self.title = title
        self.url = url
        self.content = content

    def set_content(self, content):
        self.content = content

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content