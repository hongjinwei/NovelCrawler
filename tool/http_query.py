__author__ = 'BAO'
# -*- coding: utf-8 -*-

import urllib2
import chardet

class HttpQuery:
	def __init__(self):
		pass

	def get_with_auto_decode(self, url):
		try:
			response =  urllib2.urlopen(url)
			content = response.read()
			content_encode = chardet.detect(content)['encoding']
			return content.decode(content_encode)
		except Exception, e:
			print "request error"
			print e
		finally:
			response.close()
		return ""

	def get(self, url, encode='utf8'):
		try:
			response = urllib2.urlopen(url)
			content = response.read().decode(encode)
			return content
		except Exception, e:
			print "request error"
			print e
		finally:
			response.close()
		return ""
