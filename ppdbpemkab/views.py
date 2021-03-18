from django.shortcuts import render, redirect, HttpResponseRedirect

from django.contrib.auth.models import User,Group
from django.http import HttpResponse
from .models import UserSiswa, DataSiswa
from .forms import DataSiswaForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def Home(request):
  return render(request, 'home.html')

#domain/ppdb/
def Index(request):
  return render(request, 'register/index.html')

def Pendaftar(request):
  datasiswa_list=DataSiswa.objects.all()
  
  data={'dataSiswa':datasiswa_list,'title':'judul'}
  print(data)
  return render(request, 'pendaftar.html',data)

# Siswa
# function - function 
# def FunLogin(request):
#   if(request.method == 'POST'):
#     username=request.POST['username']
#     password=request.POST['password']
#     user=authenticate(username=username,password=password)
#     if(user is not None):
#       login(request,user)
#       print('masukk')
#       return redirect('/ppdb/siswa/dashboard')
#     else:
#       print(user)
#       context={'msg':'Kompbinasi Username dan Password Salah'}
#       return render(request,'login.html',context)
#   return render(request,'login.html')

def LoginSiswa(request):
  if(request.method == 'POST'):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if(user is not None):
      login(request,user)
      print('masukk')
      return redirect('/ppdb/jalur-pendaftaran')
    else:
      print(user)
      context={'msg':'Kompbinasi Username dan Password Salah'}
      return render(request,'login.html',context)
  return render(request,'login.html')


def Register(request):
  if(request.user.groups.filter(name='Siswa').exists()):
    return render(request, './siswa/dashboard.html')
  else:
    # return render(request, 'register.html')
    if request.method == 'POST':
      # save user after input form
      # siswa = UserSiswa(nik=request.POST['nik'],no_kk=request.POST['no_kk'])
      # siswa.save()
      username=request.POST['nik']
      user=User.objects.create_user(username,'',username)
      # user.save()
      groupSiswa=Group.objects.get(name='Siswa')
      user.groups.add(groupSiswa)
      # mungkin setelah input nik & kk akan terdapat validasi,jika lolos maka lanjut isi form pendaftaran
      return redirect('/ppdb/form')
    else:
      return render(request, 'register.html')
      # return redirect('/ppdb/register')

def Form(request):
  if request.method == 'POST':
    form = DataSiswaForm(request.POST)
    # print('posan: ', request.POST)
    if form.is_valid():
      form.save()
      return redirect('/ppdb/jalur-pendaftaran')
  else:
    form = DataSiswaForm()
  # context = {
  #   'form' : form,
  # }
  return render(request, 'form.html', {
    'form': form
  })

def SiswaLogout(request):
  logout(request)
  return redirect('/')


# login page
def Login(request):
  if(request.user.groups.filter(name='Siswa').exists()):
    return render(request, './siswa/dashboard.html')
  else:
    return render(request, 'login.html')
  # return render(request, 'login.html')

def JalurPendaftaran(request):
  if(request.user.groups.filter(name='Siswa').exists()):
    return render(request, './jalur-pendaftaran/index.html')
  else:
    return redirect('/ppdb/login')

def Zonasi(request):
    return render(request, './jalur-pendaftaran/zonasi.html')

def DashboardSiswa(request):
  if(request.user.groups.filter(name='Siswa').exists()):
    return render(request, './siswa/dashboard.html')
  else:
    return redirect('/ppdb/login')








# Operator Page
def Operator(request):
  if(request.user.groups.filter(name='Operator').exists()):
    # print(request.GET['modul'] is None)
    if(request.method == 'GET' and 'modul' in request.GET):
      modulPage=request.GET['modul']
      if(modulPage == 'datapendaftar'):
        datasiswa_list=DataSiswa.objects.all()
        data={'dataSiswa':datasiswa_list,'title':'Data Pendaftar'}
      if(modulPage == 'jurnal'):
        datasiswa_list=DataSiswa.objects.all()
        data={'dataSiswa':datasiswa_list,'title':'Jurnal'}
    else:
      data={'title':'Selamat Datang Dihalaman Operator'}
    return render(request,'operatorpage/index.html',data)
  else:
    return redirect('/ppdb/operatorlogin')

    
    
def OperatorLogin(request):
  if(request.method == 'POST'):
    username=request.POST['username']
    password=request.POST['password']
    user=authenticate(username=username,password=password)
    if(user is not None):
      login(request,user)
      print('masukk')
      return redirect('/ppdb/operator')
    else:
      print(user)
      context={'msg':'Kompbinasi Username dan Password Salah'}
      return render(request,'operatorpage/login.html',context)
  return render(request,'operatorpage/login.html')


# end Operator Page

def Logout(request):
  logout(request)
  return redirect('/ppdb/operator')