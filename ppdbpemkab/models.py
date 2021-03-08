from django.db import models

class UserSiswa(models.Model):
  nik = models.CharField(max_length=16)
  no_kk = models.CharField(max_length=16)


  def __str__(self):
    return self.nik + " " + self.no_kk

