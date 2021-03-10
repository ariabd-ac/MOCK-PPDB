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
    nisn = models.CharField(max_length=200, null=True)
    asal_sekolah = models.CharField(max_length=200, null=True)
    tahun_lulus = models.CharField(max_length=200, null=True)
    p_ijazah = models.FileField(upload_to='files/ijazah/', null=True)
    nama_lengkap = models.CharField(max_length=200, null=True)
    nik = models.CharField(max_length=200, null=True)
    tempat_lahir = models.CharField(max_length=200, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    p_akte = models.FileField(upload_to='files/akte/', null=True)
    jenis_kelamin = models.CharField(max_length=200, null=True, choices=JENIS_KELAMIN)
    alamat = models.CharField(max_length=200, null=True)
    desa = models.CharField(max_length=200, null=True)
    kecamatan = models.CharField(max_length=200, null=True)
    kabupaten = models.CharField(max_length=200, null=True)
    provinsi = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    no_kk = models.CharField(max_length=200, null=True)
    p_no_kk = models.FileField(upload_to='files/kk/', null=True)
    kks = models.FileField(upload_to='file/kks/', null=True)
    pkh = models.FileField(upload_to='file/pkh/', null=True)
    kip = models.FileField(upload_to='file/kip/', null=True)
    nama_ayah_kandung = models.CharField(max_length=200, null=True)
    agama_ayah_kandung = models.CharField(max_length=200, null=True)
    pekerjaan_ayah_kandung = models.CharField(max_length=200, null=True)
    nama_ibu_kandung = models.CharField(max_length=200, null=True)
    agama_ibu_kandung = models.CharField(max_length=200, null=True)
    pekerjaan_ibu_kandung = models.CharField(max_length=200, null=True)
    alamat_orang_tua = models.CharField(max_length=200, null=True)
    desa_orang_tua = models.CharField(max_length=200, null=True)
    kecamatan_orang_tua = models.CharField(max_length=200, null=True)
    kabupaten_orang_tua = models.CharField(max_length=200, null=True)
    provinsi_orang_tua = models.CharField(max_length=200, null=True)
    no_kk_wali_murid = models.CharField(max_length=200, null=True)
    p_no_kk_wali_murid = models.FileField(upload_to='file/kk/walimurid/', null=True)
    nama_wali_murid = models.CharField(max_length=200, null=True)
    agama_wali_murid = models.CharField(max_length=200, null=True)
    pekerjaan_wali_murid = models.CharField(max_length=200, null=True)
    alamat_wali_murid = models.CharField(max_length=200, null=True)
    desa_wali_murid = models.CharField(max_length=200, null=True)
    kecamatan_wali_murid = models.CharField(max_length=200, null=True)
    kabupaten_wali_murid = models.CharField(max_length=200, null=True)
    provinsi_wali_murid = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
      return self.nama_lengkap
