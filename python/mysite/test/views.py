from datetime import datetime

from django.shortcuts import render
from test.models import Test
from test.sub_models.SubTest import SubTest

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the test index.")

def test(request):


    test1 = Test(name=datetime.now())
    test1.save()

    test2 = SubTest(name=datetime.now())
    test2.save()

    return HttpResponse('test')

