from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def chinna(request):
    return HttpResponse(' <i>Vinod Ordinary Mortal Man</i>')

def chrisgayle(request):
    return HttpResponse('<h1> Chrisgayle is king of six hitter</h1>')
