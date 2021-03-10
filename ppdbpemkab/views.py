from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from .models import UserSiswa, DataSiswa
from .forms import DataSiswaForm

# Create your views here.

def Home(request):
  return render(request, 'home.html')


# def Form(request):
#   if request.method == 'POST':
#     ds = DataSiswa(
#                   nisn=request.POST['nisn'],
#                   asal_sekolah=request.POST['asalSekolah'],
#                   tahun_lulus=request.POST['tahunLulus'],
#                   nama_lengkap=request.POST['namaLengkap'],
#                   nik=request.POST['nik'],
#                   tempat_lahir=request.POST['tempat_lahir'],
#                   tanggal_lahir=request.POST['tanggal_lahir'],
#                   email=request.POST['email'],
#                   alamat=request.POST['alamat'],
#                   desa=request.POST['desa'],
#                   kecamatan=request.POST['kecamatan'],
#                   kabupaten=request.POST['kabupaten'],
#                   provinsi=request.POST['provinsi'],
#                   )
#     ds.save()
#     # return render(request, 'form.html')
#     return redirect('/')
#   else:
#     return render(request, 'form.html')

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

def JalurPendaftaran(request):
  return render(request, './jalur-pendaftaran/index.html')

def Zonasi(request):
  return render(request, './jalur-pendaftaran/zonasi.html')