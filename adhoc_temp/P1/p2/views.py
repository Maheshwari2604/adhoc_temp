# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pyscreenshot as pys
from django.shortcuts import render

# Create your views here.

def user_home(request):
    try:
        return render(request, 'p2/videoo.html')
    except:
        print('error')


def click(request):
    try:
        im = pys.grab(bbox=(650,290,1210,640))
        im.save("p1.png")
        return render(request, 'p2/filee.html')
        print("hello")
    except:
        print("error")