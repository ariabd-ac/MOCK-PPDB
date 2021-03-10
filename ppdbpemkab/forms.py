from django import forms
from django.forms import ModelForm
from .models import DataSiswa

class DataSiswaForm(ModelForm):

  nisn = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan NISN ...."
  }))

  asal_sekolah = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Asal Sekolah ...."
  }))
  
  tahun_lulus = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Thn lulus ...."
  }))
  
  nama_lengkap = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Nama Lengkap ...."
  }))
  
  nik = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan NIK ...."
  }))
  
  tempat_lahir = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Tempat Lahir ...."
  }))
  
  tanggal_lahir = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "date",
    "placeholder" : "Masukan Tempat Lahir ...."
  }))

  email = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "email",
    "placeholder" : "Masukan Email ...."
  }))

  email = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "email",
    "placeholder" : "Masukan Email ...."
  }))

  jenis_kelamin = forms.Select(attrs={ "class" : "form-select", "aria-label" :"Default select example"})

  alamat = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Alamat ...."
  }))

  desa = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan desa ...."
  }))

  kecamatan = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Kecamatan ...."
  }))

  kabupaten = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Kabupaten ...."
  }))

  provinsi = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Provinsi ...."
  }))

  no_kk = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan No KK ...."
  }))

  nama_ayah_kandung = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Nama Ayah ...."
  }))

  agama_ayah_kandung = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Agama Ayah ...."
  }))

  pekerjaan_ayah_kandung = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Pekerjaan Ayah ...."
  }))

  nama_ibu_kandung = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Nama Ibu ...."
  }))

  agama_ibu_kandung = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Agama Ibu ...."
  }))

  pekerjaan_ibu_kandung = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Pekerjaan Ibu ...."
  }))

  alamat_orang_tua = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Alamat OT ...."
  }))

  desa_orang_tua = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Desa OT ...."
  }))

  kecamatan_orang_tua = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Alamat OT ...."
  }))

  kabupaten_orang_tua = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Kabupaten OT ...."
  }))

  provinsi_orang_tua = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Provinsi OT ...."
  }))

  nama_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Nama  Wali ...."
  }))

  agama_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Agama Wali ...."
  }))

  pekerjaan_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Pekerjaan Wali ...."
  }))

  alamat_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Alamat Wali ...."
  }))

  desa_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Desa Wali ...."
  }))

  kecamatan_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Kecamatan Wali ...."
  }))

  kabupaten_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Kabupaten Wali ...."
  }))

  provinsi_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan Provinsi Wali ...."
  }))

  no_kk_wali_murid = forms.CharField(widget=forms.TextInput(attrs={
    "class" : "form-control",
    "type"  : "text",
    "placeholder" : "Masukan No KK ...."
  }))

  
  class Meta:
    model = DataSiswa
    # fields = '__all__'
    exclude = ['p_ijazah', 'p_akte', 'p_no_kk', 'kks', 'pkh', 'kip', 'p_no_kk_wali_murid']

    # widgets = {
   
    # }