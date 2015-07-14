__author__ = 'BAO'
# -*- coding: utf-8 -*-

from tool.http_query import HttpQuery


url = "http://www.chenxuanyi.cn/python-char-coding.html"
_http = HttpQuery()
print _http.get(url)