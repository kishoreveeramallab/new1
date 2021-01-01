from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")


class HttpsResponse(object):
    pass


def contact(request):
    return HttpsResponse('hello conatct me on 098765409')