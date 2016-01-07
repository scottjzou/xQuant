

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view()
def multiply(request):
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return Response({'function': 'multiply','result': first_number * second_number})
    except Exception as e:
        return Response({'function': 'multiply','result': 'there was an error ' + str(e)})


@api_view()
def divide(request):
    try:
        first_number = int(request.GET.get('a'))
        second_number = int(request.GET.get('b'))
        return Response({'function': 'divide','result': first_number / second_number})
    except Exception as e:
        return Response({'function': 'divide','result': 'there was an error ' + str(e)})

