from django.shortcuts import render
from django.http import HttpResponse

import urllib
import tushare as ts

def index(request):
	# url = 'http://ichart.finance.yahoo.com/table.csv?g=d&ignore.csv'
	# # url += '$%s'
	# # url += '&d=06&e=30&f=2014'
	url = 'http://ichart.yahoo.com/table.csv?s=GOOG'

	# params = urllib.parse.urlencode({'s':'MSFT', 'a':'05', 'b':1, 'c':2014})
	# connect = urllib.request.urlopen(url % params)
	connect = urllib.request.urlopen(url)
	data = connect.read()
	return HttpResponse(data)