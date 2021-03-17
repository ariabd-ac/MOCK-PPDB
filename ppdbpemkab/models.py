from django.db import models

class UserSiswa(models.Model):
  nik = models.CharField(max_length=16)
  no_kk = models.CharField(max_length=16)


  def __str__(self):
    return self.nik + " " + self.no_kk


# data pendaftaraan siswa
class DataSiswa(models.Model):
    JENIS_KELAMIN = (
                  ('Laki-Laki', 'Laki-Laki'),
                  ('Perempuan', 'Perempuan'),
                  )
    nisn = models.CharField(max_length=200, blank=True)
    asal_sekolah = models.CharField(max_length=200, blank=True)
    tahun_lulus = models.CharField(max_length=200, blank=True)
    # p_ijazah = models.FileField(upload_to='files/ijazah/', blank=True)
    nama_lengkap = models.CharField(max_length=200, blank=True)
    nik = models.CharField(max_length=200, blank=True)
    tempat_lahir = models.CharField(max_length=200, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    # p_akte = models.FileField(upload_to='files/akte/', blank=True)
    jenis_kelamin = models.CharField(max_length=200, blank=True, choices=JENIS_KELAMIN)
    alamat = models.CharField(max_length=200, blank=True)
    desa = models.CharField(max_length=200, blank=True)
    kecamatan = models.CharField(max_length=200, blank=True)
    kabupaten = models.CharField(max_length=200, blank=True)
    provinsi = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    # no_kk = models.CharField(max_length=200, blank=True)
    # p_no_kk = models.FileField(upload_to='files/kk/', blank=True)
    # kks = models.FileField(upload_to='file/kks/', blank=True)
    # pkh = models.FileField(upload_to='file/pkh/', blank=True)
    # kip = models.FileField(upload_to='file/kip/', blank=True)
    nama_ayah_kandung = models.CharField(max_length=200, blank=True)
    agama_ayah_kandung = models.CharField(max_length=200, blnuuank=True)
    pekerjaan_ayah_kandung = models.CharField(max_length=200, blank=True)
    nama_ibu_kandung = models.CharField(max_length=200, blank=True)
    agama_ibu_kandung = models.CharField(max_length=200, blank=True,null=True)
    pekerjaan_ibu_kandung = models.CharField(max_length=200, blank=True)
    alamat_orang_tua = models.CharField(max_length=200, blank=True)
    desa_orang_tua = models.CharField(max_length=200, blank=True)
    kecamatan_orang_tua = models.CharField(max_length=200, blank=True)
    kabupaten_orang_tua = models.CharField(max_length=200, blank=True)
    provinsi_orang_tua = models.CharField(max_length=200, blank=True)
    no_kk_wali_murid = models.CharField(max_length=200, blank=True)
    # p_no_kk_wali_murid = models.FileField(upload_to='file/kk/walimurid/', blank=True)
    nama_wali_murid = models.CharField(max_length=200, blank=True)
    agama_wali_murid = models.CharField(max_length=200, blank=True)
    pekerjaan_wali_murid = models.CharField(max_length=200, blank=True)
    alamat_wali_murid = models.CharField(max_length=200, blank=True)
    desa_wali_murid = models.CharField(max_length=200, blank=True)
    kecamatan_wali_murid = models.CharField(max_length=200, blank=True)
    kabupaten_wali_murid = models.CharField(max_length=200, blank=True)
    provinsi_wali_murid = models.CharField(max_length=200, blank=True)
    # date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
      return self.nama_lengkap


class DataSekolah:
  kode_sekolah=models.CharField(max_length=200,blank=False,primary_key=True)
  nama=models.CharField(max_length=200,blank=False)