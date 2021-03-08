from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.http import HttpResponse
from .models import UserSiswa

# Create your views here.

def Home(request):
  return render(request, 'home.html')


#domain/ppdb/
def Index(request):
  return render(request, 'register/index.html')


def Register(request):
  if request.method == 'POST':
    siswa = UserSiswa(nik=request.POST['nik'],no_kk=request.POST['no_kk'])
    siswa.save()
    return redirect('/ppdb/zonasi')
  else:
    return render(request, 'register.html')

def FunLogin(request):
  if request.method == 'POST':
    if UserSiswa.objects.filter(nik=request.POST['nik'], no_kk=request.POST['no_kk']).exists():
      siswa = UserSiswa.objects.get(nik=request.POST['nik'], no_kk=request.POST['no_kk'])
      return render(request, 'register/index.html', {'siswa':siswa})
    else:
      contex = {
        'msg' : 'salah ga cocok'
      }
      return render(request, 'login.html', context)

def Login(request):
  return render(request, 'login.html')

def Zonasi(request):
  return render(request, 'zonasi.html')