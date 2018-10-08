from django.http import HttpResponse
from django.shortcuts import render


def frontpage(request):
    return HttpResponse("hei")
