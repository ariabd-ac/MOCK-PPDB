from django.shortcuts import render, redirect, HttpResponseRedirect
# from django.http import HttpResponse
from .models import UserSiswa
from .models import DataSiswa

# Create your views here.

def Home(request):
  return render(request, 'home.html')


def Form(request):
  return render(request, 'form.html')

#domain/ppdb/
def Index(request):
  return render(request, 'register/index.html')


def Register(request):
  if request.method == 'POST':
    # save user after input form
    # siswa = UserSiswa(nik=request.POST['nik'],no_kk=request.POST['no_kk'])
    # siswa.save()
    # mungkin setelah input nik & kk akan terdapat validasi,jika lolos maka lanjut isi form pendaftaran
    return redirect('/ppdb/form')
  else:
    return render(request, 'register.html')

def FunLogin(request):
  if request.method == 'POST':
    if UserSiswa.objects.filter(nik=request.POST['nik'], no_kk=request.POST['no_kk']).exists():
      siswa = UserSiswa.objects.get(nik=request.POST['nik'], no_kk=request.POST['no_kk'])
      return render(request, 'register/index.html', {'siswa':siswa})
    else:
      context = {
        'msg' : 'salah ga cocok'
      }
      return render(request, 'login.html', context)

def Login(request):
  return render(request, 'login.html')

def Zonasi(request):
  return render(request, 'zonasi.html')

def Pendaftar(request):
  datasiswa_list=DataSiswa.objects.all()
  data={'dataSiswa':datasiswa_list,'title':'judul'}
  return render(request, 'pendaftar.html',data)