__author__ = 'jhonjairoroa87'

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jsonp.renderers import JSONPRenderer
from rest_framework.decorators import api_view

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view()
def multiply(request):
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return Response({'result': first_number * second_number})
    except Exception as e:
        return Response({'result': 'there was an error ' + str(e)})


@api_view()
def divide(request):
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return Response({'result': first_number / second_number})
    except Exception as e:
        return Response({'result': 'there was an error ' + str(e)})

