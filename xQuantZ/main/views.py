from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

import tushare as ts



def index(request):
	return HttpResponse(str(ts.get_hist_data('600848')))