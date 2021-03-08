from django.db import models

class UserSiswa(models.Model):
  nik = models.CharField(max_length=16)
  no_kk = models.CharField(max_length=16)


  def __str__(self):
    return self.nik + " " + self.no_kk


# data pendaftaraan siswa
class DataSiswa(models.Model):
    nisn = models.CharField(max_length=200)
    asal_sekolah = models.CharField(max_length=200)
    tahun_lulus = models.CharField(max_length=200)
    nama_lengkap = models.CharField(max_length=200)
    nik = models.CharField(max_length=200)
    tempat_lahir = models.CharField(max_length=200)
    tanggal_lahir = models.DateTimeField('date published')
    filename_akte = models.CharField(max_length=200)
    jenis_kelamin = models.BooleanField()
    alamat = models.CharField(max_length=200)
    desa = models.CharField(max_length=200)
    kecamatan = models.CharField(max_length=200)
    kabupaten = models.CharField(max_length=200)
    provinsi = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    no_kk_keluarga = models.CharField(max_length=200)
    filename_kk_keluarga = models.CharField(max_length=200)
    is_kks = models.BooleanField()
    is_pkh = models.BooleanField()
    is_kkp = models.BooleanField()
    nama_ayah_kandung = models.CharField(max_length=200)
    agama_ayah_kandung = models.CharField(max_length=200)
    pekerjaan_ayah_kandung = models.CharField(max_length=200)
    nama_ibu_kandung = models.CharField(max_length=200)
    agama_ibu_kandung = models.CharField(max_length=200)
    pekerjaan_ibu_kandung = models.CharField(max_length=200)
    alamat_orang_tua = models.CharField(max_length=200)
    desa_orang_tua = models.CharField(max_length=200)
    kecamatan_orang_tua = models.CharField(max_length=200)
    kabupaten_orang_tua = models.CharField(max_length=200)
    provinsi_orang_tua = models.CharField(max_length=200)
    no_kk_wali_murid = models.CharField(max_length=200)
    filename_kk_wali_murid = models.CharField(max_length=200)
    nama_wali_murid = models.CharField(max_length=200)
    agama_wali_murid = models.CharField(max_length=200)
    pekerjaan_wali_murid = models.CharField(max_length=200)
    alamat_wali_murid = models.CharField(max_length=200)
    desa_wali_murid = models.CharField(max_length=200)
    kecamatan_wali_murid = models.CharField(max_length=200)
    kabupaten_wali_murid = models.CharField(max_length=200)
    provinsi_wali_murid = models.CharField(max_length=200)