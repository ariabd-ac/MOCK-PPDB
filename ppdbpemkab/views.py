from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Home(request):
  return render(request, 'home.html')


#domain/ppdb/
def Index(request):
  return render(request, 'index.html')


def Register(request):
  return render(request, 'register.html',)

def Login(request):
  return render(request, 'login.html')